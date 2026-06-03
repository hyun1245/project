from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
import asyncio
import random
import aiomysql
from aiomysql.cursors import DictCursor
from database import init_db, MYSQL_HOST, MYSQL_PORT, MYSQL_USER, MYSQL_PASSWORD, MYSQL_DB
from datetime import datetime, timedelta
from typing import List

app = FastAPI()

class ConnectionManager:
    def __init__(self):
        self.active_connections: List[WebSocket] = []

    async def connect(self, websocket: WebSocket):
        await websocket.accept()
        self.active_connections.append(websocket)

    def disconnect(self, websocket: WebSocket):
        self.active_connections.remove(websocket)

    async def broadcast_json(self, data: dict):
        for connection in self.active_connections:
            await connection.send_json(data)

manager = ConnectionManager()

# 프론트엔드 개발 서버의 주소를 origins 목록에 추가해야 합니다.
origins = [
    "http://localhost",
    "http://localhost:3000",  # 예: React 기본 포트
    "http://localhost:5173",  # 예: Vite 기본 포트
    "http://localhost:8080",  # 예: Vue.js 기본 포트
    # 실제 프로덕션 환경의 프론트엔드 도메인도 추가해야 합니다.
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,       # origins 목록에 있는 출처의 요청을 허용
    allow_credentials=True,    # 쿠키를 포함한 요청을 허용
    allow_methods=["*"],       # 모든 HTTP 메소드(GET, POST 등)를 허용
    allow_headers=["*"],       # 모든 HTTP 헤더를 허용
)

# 애플리케이션 시작 시 DB 초기화
@app.on_event("startup")
async def startup_event():
    await init_db()

# 2. 실시간 상태 전송을 위한 WebSocket
@app.websocket("/ws/dashboard")
async def websocket_endpoint(websocket: WebSocket):
    await manager.connect(websocket)

    async def get_dashboard_data():
        """DB에서 모든 대시보드 데이터를 가져와 통합된 딕셔너리로 반환합니다."""
        async with aiomysql.connect(host=MYSQL_HOST, port=MYSQL_PORT, user=MYSQL_USER, password=MYSQL_PASSWORD, db=MYSQL_DB, cursorclass=DictCursor) as conn:
            async with conn.cursor() as cursor:
                # DictCursor를 사용하여 결과를 딕셔너리처럼 접근할 수 있습니다.

                # 1. 통계 데이터 계산
                # MySQL의 UNIX_TIMESTAMP 함수를 사용하여 시간 차이를 초 단위로 계산합니다.
                await cursor.execute("SELECT UNIX_TIMESTAMP(end_time) - UNIX_TIMESTAMP(start_time) as stay FROM orders WHERE is_paid = 1 AND end_time IS NOT NULL")
                avg_stay_minutes_val = await cursor.fetchall()
                avg_stay_minutes = (sum(row['stay'] for row in avg_stay_minutes_val) / len(avg_stay_minutes_val) / 60) if avg_stay_minutes_val else 0

                # 이제 'rate' 키로 안전하게 접근할 수 있습니다.
                await cursor.execute("SELECT SUM(CASE WHEN status = 'OCCUPIED' THEN 1 ELSE 0 END) * 100 / COUNT(*) as rate FROM tables")
                occupancy_rate_val = await cursor.fetchone()
                occupancy_rate = occupancy_rate_val['rate'] if occupancy_rate_val else 0

                bottleneck_query = """
                    SELECT menu_name, AVG(UNIX_TIMESTAMP(served_at) - UNIX_TIMESTAMP(ordered_at)) as lead_time
                    FROM order_items WHERE served_at IS NOT NULL
                    GROUP BY menu_name ORDER BY lead_time DESC LIMIT 1
                """
                await cursor.execute(bottleneck_query)
                bottleneck_row = await cursor.fetchone()
                bottleneck_menu = f"{bottleneck_row['menu_name']} ({round(bottleneck_row['lead_time']/60)}분)" if bottleneck_row else "N/A"

                stats_data = {
                    "avg_stay_minutes": round(avg_stay_minutes, 1),
                    "occupancy_rate": round(float(occupancy_rate), 1),
                    "peak_time": "21:00 - 22:00",
                    "bottleneck_menu": bottleneck_menu
                }

                # 2. 테이블 상태 데이터 가져오기
                await cursor.execute("SELECT id, table_number, status FROM tables ORDER BY id")
                tables_rows = await cursor.fetchall()
                tables_data = [dict(row) for row in tables_rows]

                # 3. 주문 준비 현황 데이터 생성
                prep_query = """
                    SELECT oi.menu_name, t.table_number
                    FROM order_items oi
                    JOIN orders o ON oi.order_id = o.id
                    JOIN tables t ON o.table_id = t.id
                    WHERE oi.served_at IS NULL
                """
                await cursor.execute(prep_query)
                prep_rows = await cursor.fetchall()
                preparation_data = [{'menu': row['menu_name'], 'table': row['table_number'], 'status': '준비중'} for row in prep_rows]

                # 4. 최근 주문 현황 데이터 생성
                recent_orders_query = """
                    SELECT o.id, t.table_number, o.is_paid,
                           (SELECT COUNT(*) FROM order_items WHERE order_id = o.id AND served_at IS NOT NULL) as served_count,
                           (SELECT COUNT(*) FROM order_items WHERE order_id = o.id) as total_count
                    FROM orders o
                    JOIN tables t ON o.table_id = t.id
                    ORDER BY o.start_time DESC LIMIT 5
                """
                await cursor.execute(recent_orders_query)
                recent_orders_rows = await cursor.fetchall()
                recent_orders_data = []
                for row in recent_orders_rows:
                    status = "주문 접수"
                    if row['is_paid']:
                        status = "결제 완료"
                    elif row['served_count'] == row['total_count'] and row['total_count'] > 0:
                        status = "서빙 완료"
                    recent_orders_data.append({'id': row['id'], 'details': f"테이블 {row['table_number']}", 'status': status})

                return {"stats": stats_data, "tables": tables_data, "preparation_status": preparation_data, "recent_orders": recent_orders_data}

    try:
        # --- 첫 연결 시 즉시 데이터 전송 ---
        await manager.broadcast_json(await get_dashboard_data())

        # --- 5초마다 실제 매장 흐름을 시뮬레이션하고 데이터 전송 ---
        while True:
            await asyncio.sleep(5)
            async with aiomysql.connect(host=MYSQL_HOST, port=MYSQL_PORT, user=MYSQL_USER, password=MYSQL_PASSWORD, db=MYSQL_DB, cursorclass=DictCursor) as conn:
                async with conn.cursor() as cursor:
                    # 시뮬레이션: 3가지 이벤트 중 하나를 무작위로 실행
                    event_type = random.choice(['new_order', 'payment', 'cleaning'])

                    if event_type == 'new_order':
                        # 비어있는 테이블에 새 주문 생성 (MySQL의 RAND() 함수 사용)
                        await cursor.execute("SELECT id FROM tables WHERE status = 'EMPTY' ORDER BY RAND() LIMIT 1")
                        empty_table = await cursor.fetchone()
                        if empty_table:
                            await cursor.execute("UPDATE tables SET status = 'OCCUPIED' WHERE id = %s", (empty_table['id'],))
                            # 실제라면 여기서 orders, order_items에 데이터가 추가됩니다.
                            # 지금은 init_db에서 생성된 데이터로 충분하므로 상태만 변경합니다.

                    elif event_type == 'payment':
                        # 사용 중인 테이블을 결제 처리하고 'DIRTY'로 변경
                        await cursor.execute("SELECT id FROM tables WHERE status = 'OCCUPIED' ORDER BY RAND() LIMIT 1")
                        occupied_table = await cursor.fetchone()
                        if occupied_table:
                            await cursor.execute("UPDATE tables SET status = 'DIRTY' WHERE id = %s", (occupied_table['id'],))
                            await cursor.execute("SELECT id FROM orders WHERE table_id = %s AND is_paid = 0", (occupied_table['id'],))
                            order_to_pay = await cursor.fetchone()
                            if order_to_pay:
                                await cursor.execute("UPDATE orders SET is_paid = 1, end_time = %s WHERE id = %s", (datetime.now(), order_to_pay['id']))

                    elif event_type == 'cleaning':
                        # 더러운 테이블을 청소하여 'EMPTY'로 변경
                        await cursor.execute("SELECT id FROM tables WHERE status = 'DIRTY' ORDER BY RAND() LIMIT 1")
                        dirty_table = await cursor.fetchone()
                        if dirty_table:
                            await cursor.execute("UPDATE tables SET status = 'EMPTY' WHERE id = %s", (dirty_table['id'],))

                await conn.commit()

            # 변경된 데이터를 다시 전송
            await manager.broadcast_json(await get_dashboard_data())
    except WebSocketDisconnect:
        manager.disconnect(websocket)
        print("클라이언트 연결이 끊어졌습니다.")
    except Exception as e:
        print(f"오류 발생: {e}")
    finally:
        manager.disconnect(websocket)
        print("WebSocket 연결 종료")


# 프론트엔드 파일들을 서비스하기 위한 StaticFiles 마운트
# 이 코드는 다른 모든 API 라우트 뒤에 위치해야 합니다.
app.mount("/", StaticFiles(directory="static", html=True), name="static")