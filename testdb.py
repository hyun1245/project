import asyncio
import aiomysql
import pymysql
# 기존 database.py 파일에서 설정 값을 그대로 가져옵니다.
from database import MYSQL_HOST, MYSQL_PORT, MYSQL_USER, MYSQL_PASSWORD, MYSQL_DB

async def test_connection():
    """데이터베이스 연결을 테스트하고 결과를 출력합니다."""
    print("--- 데이터베이스 연결 테스트 시작 ---")
    print(f"Host: {MYSQL_HOST}")
    print(f"Port: {MYSQL_PORT}")
    print(f"User: {MYSQL_USER}")
    print(f"Database: {MYSQL_DB}")

    try:
        conn = await aiomysql.connect(
            host=MYSQL_HOST,
            port=MYSQL_PORT,
            user=MYSQL_USER,
            password=MYSQL_PASSWORD,
            db=MYSQL_DB,
            connect_timeout=10  # 10초 이상 응답 없으면 실패 처리
        )
        print("\n[성공] 데이터베이스에 성공적으로 연결되었습니다!")

        async with conn.cursor() as cursor:
            await cursor.execute("SELECT 1")
            result = await cursor.fetchone()
            print(f"[성공] 간단한 쿼리 실행에 성공했습니다. (결과: {result})")

        conn.close()

    except pymysql.err.OperationalError as e:
        print(f"\n[실패] 데이터베이스 연결 오류가 발생했습니다: {e}")
        error_code = e.args[0]
        if error_code == 1045:
            print("\n>>> 'Access Denied (1045)' 오류입니다. 인증에 실패했습니다.")
            print("   1. database.py의 MYSQL_USER, MYSQL_PASSWORD가 정확한지 다시 확인하세요.")
            print("   2. MySQL 서버가 다른 컴퓨터(리눅스 VM 등)에 있다면, MYSQL_HOST를 '127.0.0.1'이 아닌 해당 컴퓨터의 IP 주소로 변경해야 합니다.")
            print("   3. MySQL에 해당 사용자가 외부 IP에서 접속할 수 있도록 권한이 부여되었는지 확인하세요. (예: 'hyeon'@'%')")
        elif error_code == 2003:
            print("\n>>> 'Can't connect to MySQL server (2003)' 오류입니다. 서버를 찾을 수 없습니다.")
            print("   1. database.py의 MYSQL_HOST IP 주소와 MYSQL_PORT 번호가 올바른지 확인하세요.")
            print("   2. 해당 IP 주소의 컴퓨터에서 MySQL 서버가 실제로 실행 중인지 확인하세요.")
            print("   3. 방화벽이 MySQL 포트(기본 3306)를 차단하고 있지 않은지 확인하세요.")
        elif error_code == 1049:
            print(f"\n>>> 'Unknown database ({error_code})' 오류입니다. 데이터베이스를 찾을 수 없습니다.")
            print(f"   1. MySQL 서버에 '{MYSQL_DB}' 데이터베이스가 존재하는지 확인하세요.")
            print(f"   2. 만약 없다면, 'CREATE DATABASE {MYSQL_DB};' 명령어로 데이터베이스를 생성해주세요.")
        else:
            print(f"\n>>> 예상치 못한 OperationalError 입니다. (오류 코드: {error_code})")

    except Exception as e:
        print(f"\n[실패] 예상치 못한 오류가 발생했습니다: {e}")

if __name__ == "__main__":
    asyncio.run(test_connection())
