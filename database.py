import aiomysql
from datetime import datetime, timedelta
import random

# --- MySQL 연결 정보 ---
# 사용자의 실제 환경에 맞게 수정해야 합니다.
MYSQL_HOST = '127.0.0.1'  # Linux에 설치된 MySQL 서버 IP 주소
MYSQL_PORT = 3306
MYSQL_USER = 'hyeon'      # MySQL 사용자 이름
MYSQL_PASSWORD = '1111' # MySQL 비밀번호
MYSQL_DB = 'project'     # 미리 생성된 데이터베이스 이름

async def init_db():
    """데이터베이스를 초기화하고 샘플 데이터를 생성합니다."""
    # MySQL에 연결합니다.
    async with aiomysql.connect(host=MYSQL_HOST, port=MYSQL_PORT, user=MYSQL_USER, password=MYSQL_PASSWORD, db=MYSQL_DB) as conn:
        async with conn.cursor() as cursor:
            # 기존 테이블 삭제 (외래 키 제약 조건 임시 비활성화)
            await cursor.execute("SET FOREIGN_KEY_CHECKS = 0;")
            await cursor.execute("DROP TABLE IF EXISTS order_items")
            await cursor.execute("DROP TABLE IF EXISTS orders")
            await cursor.execute("DROP TABLE IF EXISTS tables")
            await cursor.execute("SET FOREIGN_KEY_CHECKS = 1;")

            # 테이블 생성 (MySQL 호환 구문으로 수정)
            # InnoDB 엔진을 사용해야 외래 키가 동작합니다.
            await cursor.execute("""
                CREATE TABLE tables (
                    id INTEGER PRIMARY KEY AUTO_INCREMENT,
                    table_number VARCHAR(255),
                    status VARCHAR(20) DEFAULT 'EMPTY', -- EMPTY, OCCUPIED, DIRTY
                    capacity INTEGER
                ) ENGINE=InnoDB
            """)
            await cursor.execute("""
                CREATE TABLE orders (
                    id INTEGER PRIMARY KEY AUTO_INCREMENT,
                    table_id INTEGER,
                    customer_count INTEGER,
                    start_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    end_time TIMESTAMP NULL,
                    total_price INTEGER,
                    is_paid BOOLEAN DEFAULT FALSE,
                    FOREIGN KEY (table_id) REFERENCES tables(id)
                ) ENGINE=InnoDB
            """)
            await cursor.execute("""
                CREATE TABLE order_items (
                    id INTEGER PRIMARY KEY AUTO_INCREMENT,
                    order_id INTEGER,
                    menu_name VARCHAR(255),
                    ordered_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    served_at TIMESTAMP NULL,
                    FOREIGN KEY (order_id) REFERENCES orders(id)
                ) ENGINE=InnoDB
            """)

            # --- 샘플 데이터 대량 생성 ---
            menu_list = ['스테이크', '파스타', '피자', '샐러드', '리조또', '감바스']
            menu_prices = {'스테이크': 35000, '파스타': 18000, '피자': 22000, '샐러드': 12000, '리조또': 19000, '감바스': 25000}

            # 1. 테이블 20개 생성 (다양한 상태와 인원)
            num_tables = 20
            for table_id in range(1, num_tables + 1):
                status = random.choice(['EMPTY', 'OCCUPIED', 'DIRTY'])
                await cursor.execute(
                    "INSERT INTO tables (id, table_number, status, capacity) VALUES (%s, %s, %s, %s)",
                    (table_id, f"T{table_id}", status, random.choice([2, 4, 6]))
                )

                # 'OCCUPIED' 상태인 테이블에 대해 주문 및 주문 항목 생성
                if status == 'OCCUPIED':
                    now = datetime.now()
                    start_time = now - timedelta(minutes=random.randint(10, 60))
                    customer_count = random.randint(1, 4)

                    await cursor.execute(
                        "INSERT INTO orders (table_id, customer_count, start_time, is_paid) VALUES (%s, %s, %s, %s)",
                        (table_id, customer_count, start_time, False)
                    )
                    order_id = cursor.lastrowid

                    total_price = 0
                    num_items = random.randint(1, 4)
                    for _ in range(num_items):
                        menu_name = random.choice(menu_list)
                        total_price += menu_prices[menu_name]
                        ordered_at = start_time + timedelta(minutes=random.randint(1, 10))

                        # 일부 항목은 서빙 완료 처리
                        served_at = None
                        if random.random() > 0.3: # 70% 확률로 서빙 완료
                            served_at = ordered_at + timedelta(minutes=random.randint(5, 20))

                        await cursor.execute(
                            "INSERT INTO order_items (order_id, menu_name, ordered_at, served_at) VALUES (%s, %s, %s, %s)",
                            (order_id, menu_name, ordered_at, served_at)
                        )
                    await cursor.execute("UPDATE orders SET total_price = %s WHERE id = %s", (total_price, order_id))

        await conn.commit()