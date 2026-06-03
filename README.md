# 실시간 레스토랑 대시보드 백엔드

FastAPI와 WebSocket을 사용하여 레스토랑 운영 현황을 실시간으로 모니터링하는 대시보드 백엔드 프로젝트입니다. 테이블 상태, 주문 현황, 주요 통계 지표 등을 웹소켓을 통해 클라이언트에 지속적으로 전송하여 동적인 대시보드를 구현할 수 있습니다.

## 🚀 주요 기능

*   **실시간 데이터 전송**: WebSocket을 사용하여 대시보드 데이터를 5초마다 클라이언트로 푸시합니다.
*   **핵심 지표 시각화**: 평균 고객 체류 시간, 테이블 점유율, 병목 현상 메뉴 등 주요 통계를 제공합니다.
*   **테이블 상태 관리**: 'EMPTY', 'OCCUPIED', 'DIRTY' 상태를 실시간으로 추적합니다.
*   **주문 및 서빙 현황**: 준비 중인 메뉴와 최근 주문 목록을 동적으로 업데이트합니다.
*   **현실적인 데이터 시뮬레이션**: 신규 주문, 결제, 테이블 정리 등 실제 매장 활동을 시뮬레이션하여 데이터베이스를 지속적으로 업데이트합니다.
*   **비동기 처리**: `FastAPI`와 `aiomysql`을 사용하여 모든 데이터베이스 작업을 비동기적으로 처리하여 높은 성능을 보장합니다.

## 🛠️ 기술 스택

*   **Backend**: Python, FastAPI, Uvicorn
*   **Database**: MySQL
*   **Async Driver**: `aiomysql`
*   **Real-time Communication**: WebSockets

## 📋 사전 요구 사항

*   Python 3.8+
*   MySQL Server

## ⚙️ 설치 및 설정

1.  **리포지토리 클론:**
    ```bash
    git clone <your-repository-url>
    cd <repository-directory>
    ```

2.  **가상 환경 생성 및 활성화:**
    ```bash
    python -m venv venv
    # Windows
    venv\Scripts\activate
    # macOS / Linux
    source venv/bin/activate
    ```

3.  **필요한 라이브러리 설치:**
    프로젝트 루트에 포함된 `requirements.txt` 파일을 사용하여 필요한 모든 라이브러리를 설치합니다.
    ```bash
    pip install -r requirements.txt
    ```

4.  **데이터베이스 설정:**
    *   MySQL에 접속하여 데이터베이스를 생성합니다.
        ```sql
        CREATE DATABASE project CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
        ```
    *   사용자를 생성하고 권한을 부여합니다. (프로젝트의 `hyeon`/`1111` 자격 증명을 사용하거나 원하는 대로 변경)
        ```sql
        CREATE USER 'hyeon'@'%' IDENTIFIED BY '1111';
        GRANT ALL PRIVILEGES ON project.* TO 'hyeon'@'%';
        FLUSH PRIVILEGES;
        ```
    *   `c:\project\database.py` 파일의 MySQL 연결 정보를 자신의 환경에 맞게 수정합니다.
        ```python
        MYSQL_HOST = '127.0.0.1'  # MySQL 서버 IP
        MYSQL_PORT = 3306
        MYSQL_USER = 'hyeon'      # 생성한 사용자 이름
        MYSQL_PASSWORD = '1111' # 생성한 비밀번호
        MYSQL_DB = 'project'     # 생성한 데이터베이스 이름
        ```

## ▶️ 실행하기

1.  **(선택 사항) 데이터베이스 연결 테스트:**
    `testdb.py` 스크립트를 실행하여 MySQL 서버와의 연결을 확인합니다.
    ```bash
    python c:\project\testdb.py
    ```
    연결에 성공하면 `[성공] 데이터베이스에 성공적으로 연결되었습니다!` 메시지가 출력됩니다. 실패 시 출력되는 안내에 따라 문제를 해결하세요.

2.  **백엔드 서버 실행:**
    Uvicorn을 사용하여 FastAPI 애플리케이션을 실행합니다. 애플리케이션이 시작되면 `database.py`의 `init_db` 함수가 자동으로 실행되어 테이블을 생성하고 샘플 데이터를 삽입합니다.
    ```bash
    uvicorn project:app --reload
    ```

3.  **애플리케이션 확인:**
    *   서버가 정상적으로 실행되면 `http://127.0.0.1:8000` 주소로 접속할 수 있습니다.
    *   WebSocket 연결은 `ws://127.0.0.1:8000/ws/dashboard` 엔드포인트를 통해 이루어집니다.
    *   `static` 폴더에 프론트엔드 빌드 파일을 위치시키면 `http://127.0.0.1:8000`에서 바로 대시보드를 확인할 수 있습니다.

## 📂 프로젝트 구조

*   `project.py`: 메인 FastAPI 애플리케이션 로직, WebSocket 통신 및 데이터 시뮬레이션 담당.
*   `database.py`: 데이터베이스 초기화(테이블 생성 및 샘플 데이터 삽입) 로직 담당.
*   `testdb.py`: 데이터베이스 연결을 테스트하기 위한 유틸리티 스크립트.
*   `requirements.txt`: 프로젝트 파이썬 의존성 목록.
*   `static/`: 프론트엔드 파일 (HTML, CSS, JS)을 위치시키는 디렉토리.