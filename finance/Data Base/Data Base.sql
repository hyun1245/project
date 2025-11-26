DESC EMP;

DESC DEPT;

DESC SALGRADE;

-- 테이블 데이터 조회 → BASIC

-- 전체 조회 
SELECT * FROM EMP;
select * from ALL_tables;
select * from ALL_ALL_TABLES;
SELECT * FROM ALL_OBJECTS WHERE OBJECT_TYPE = 'TABLE';

-- DB User Table
select * from user_tables;
SELECT * FROM TABS;
SELECT * FROM USER_OBJECTS WHERE OBJECT_TYPE = 'TABLE';

-- DB Columns
SELECT * FROM COLS;
SELECT * FROM ALL_TAB_COLUMNS;
-- SELECT * FROM COLUMNS_VALUE WHERE OBJECT_VALUE = 'TABLE';

SELECT EMPNO, ENAME, DEPTNO
    FROM EMP;

-- 테이블 데이터 조회 → DISTINCT

SELECT DISTINCT DEPTNO -- 중복된 데이터 제거후 조회
    FROM EMP;

SELECT DISTINCT JOB, DEPTNO -- JOB, DEPTNO 컬럼의 중복된 데이터 제거후 조회
    FROM EMP;

-- 테이블 데이터 조회 → ALL

SELECT ALL JOB, DEPTNO
    FROM EMP;

-- 테이블 조회 → 연산식

SELECT ENAME, SAL, SAL*12+COMM, COMM -- null 은 지정되지않은 값이므로 연산을 해도 null 로 나옴 
    FROM EMP;

SELECT ENAME, SAL, SAL*12+COMM AS ANNSAL, COMM -- 별칭(AS) 사용 -> 이름 변경 
    FROM EMP;

-- 테이블 조회 → ORDER BY

SELECT *
    FROM EMP
ORDER BY SAL; -- SAL 컬럼 기준 오름차순 정렬(Default = ASC)

SELECT *
    FROM EMP
ORDER BY SAL DESC; -- 내림차순 → DESC

SELECT *
    FROM EMP
-- ORDER BY DEPTNO ASC, SAL DESC; -- DEPTNO 오름차순, SAL 내림차순
ORDER BY DEPTNO DESC, SAL ASC; -- ORDER BY 는 여러개 적용가능, 먼저 오는 변수 적용후 다음변수 후적용

-- 테이블 조회 → 실습문제

SELECT DISTINCT JOB
    FROM EMP;
 
SELECT EMPNO AS EMPLOYEE_NO, ENAME AS EMPLOYEE_NAME, MGR AS MANAGER, SAL AS SALARY, COMM AS COMMISSION, DEPTNO AS DEPARTMENT_NO
    FROM EMP
ORDER BY DEPARTMENT_NO DESC, EMPLOYEE_NAME ASC;

-- 조건문 사용 → WHERE

SELECT *
    FROM EMP;

SELECT *
    FROM EMP
    WHERE DEPTNO = 30; -- DEPTNO가 30인 사원 조회

-- 조건문 사용 → AND, OR

SELECT * 
    FROM EMP
    WHERE DEPTNO  = 30
        AND JOB = 'SALESMAN'; -- DEPTNO가 30이고 JOB이 SALESMAN인 사원 조회

SELECT *
    FROM EMP
    WHERE DEPTNO = 30
        OR JOB = 'CLERK'; -- DEPTNO가 30이거나 JOB이 CLERK인 사원 조회

-- 조건문 사용 → 산술 연산자

SELECT *
    FROM EMP
    WHERE SAL * 12 = 36000; -- 연봉이 36000인 사원 조회 = (SAL = 3000)
    -- WHERE SAL * 12 < 36000; -- 연봉이 36000미만인 사원 조회(SAL < 3000)

-- 조건문 사용 → 대소 비교 연산자

SELECT *
    FROM EMP
    WHERE SAL >= 3000; -- SAL이 3000이상인 사원 조회

SELECT * 
    FROM EMP
    WHERE ENAME >= 'F'; -- 사원 이름의 첫문자가 F와 같거나 F보다 뒤에있는 것만 검색

-- 조건문 사용 → 등가 비교 연산자

SELECT * 
    FROM EMP
    WHERE SAL != 3000; -- SAL이 3000이 아닌 사원 조회

SELECT * 
    FROM EMP
    WHERE SAL <> 3000; -- SAL이 3000이 아닌 사원 조회

SELECT *
    FROM EMP
    WHERE SAL ^= 3000; -- SAL이 3000이 아닌 사원 조회

-- 조건문 사용 → 논리 부정 연산자

SELECT *
    FROM EMP
    WHERE NOT SAL = 3000; -- SAL이 3000이 아닌 사원 조회

-- 조건문 사용 → IN 연산자

SELECT *
    FROM EMP
    WHERE JOB = 'MANAGER'
        OR JOB = 'SALESMAN'
        OR JOB = 'CLERK'; -- JOB이 MANAGER, SALESMAN, CLERK인 사원 조회

SELECT *
    FROM EMP
    WHERE JOB IN('MANAGER', 'SALESMAN', 'CLERK'); -- IN 연산자 사용

SELECT *
    FROM EMP
    WHERE JOB != 'MANAGER'
        AND JOB <> 'SALESMAN'
        AND JOB ^= 'CLERK'; -- JOB이 MANAGER, SALESMAN, CLERK가 아닌 사원 조회

SELECT *
    FROM EMP
    WHERE JOB NOT IN('MANAGER', 'SALESMAN', 'CLERK'); -- NOT IN 연산자 사용

-- 조건문 사용 → BETWEEN A AND B 연산자

SELECT *
    FROM EMP 
    WHERE SAL >= 2000
    AND SAL <= 3000; -- SAL이 2000이상 3000이하인 사원 조회

SELECT *
    FROM EMP
    WHERE SAL BETWEEN 2000 AND 3000; -- SAL이 2000이상 3000이하인 사원 조회

SELECT *
    FROM EMP
    WHERE SAL NOT BETWEEN 2000 AND 3000; -- SAL이 2000미만 또는 3000초과인 사원 조회

-- 조건문 사용 → LIKE 연산자와 와일드카드

SELECT *
    FROM EMP
    WHERE ENAME LIKE 'S%'; -- ENAME이 S로 시작하는 사원 조회

SELECT *
    FROM EMP
    WHERE ENAME LIKE '_L%'; -- ENAME의 두번째 글자가 L인 사원 조회

SELECT *
    FROM EMP
    WHERE ENAME LIKE '%AM%'; -- ENAME에 AM이 포함된 사원 조회

SELECT *
    FROM EMP
    WHERE ENAME NOT LIKE '%AM%'; -- ENAME에 AM이 포함되지 않은 사원 조회

-- 조건문 사용 → IS NULL 연산자

SELECT ENAME, SAL, SAL*12+COMM AS ANNSAL, COMM
    FROM EMP;

SELECT *
    FROM EMP
    WHERE COMM = NULL; -- COMM이 NULL인 사원 조회 (잘못된 방법)

SELECT *
    FROM EMP
    WHERE COMM IS NULL; -- COMM이 NULL인 사원 조회 (올바른 방법)

SELECT * 
    FROM EMP
    WHERE MGR IS NOT NULL; -- MGR이 NULL이 아닌 사원 조회

SELECT *
    FROM EMP
    WHERE SAL > NULL 
        AND COMM IS NULL; -- SAL이 NULL보다 크고 COMM이 NULL인 사원 조회 (잘못된 방법)

SELECT *
    FROM EMP
    WHERE SAL > NULL
        OR COMM IS NULL; -- SAL이 NULL보다 크거나 COMM이 NULL인 사원 조회 (옳은 방법)

-- 조건문 사용 → UNION 집합 연산자

SELECT EMPNO, ENAME, DEPTNO
    FROM EMP
    WHERE DEPTNO = 10
UNION
SELECT EMPNO, ENAME, DEPTNO
    FROM EMP
    WHERE DEPTNO = 20;

-- 조건문 사용 → INTERSECT/MINUS 집합 연산자

SELECT EMPNO, ENAME, DEPTNO
    FROM EMP
INTERSECT -- EMP 테이블에서 DEPTNO의 교집합이 10인 사원의 교집합 조회
SELECT EMPNO, ENAME, DEPTNO
    FROM EMP
    WHERE DEPTNO = 10; -- DEPTNO가 10인 사원 조회


SELECT EMPNO, ENAME, DEPTNO
    FROM EMP
MINUS -- EMP 테이블 전체에서 DEPTNO가 10인 사원 제외
SELECT EMPNO, ENAME, DEPTNO
    FROM EMP
    WHERE DEPTNO = 10; -- DEPTNO가 10인 사원 조회

-- 다중행 함수 → SUM 함수

SELECT SUM(SAL)
    FROM EMP; -- SAL 컬럼의 합계 조회

SELECT ENAME, SUM(SAL)
    FROM EMP; -- 오류 발생(다중행 함수 사용시 단독사용 또는 GROUP BY 절과 함께 사용)

SELECT SUM(COMM) -- SUM 함수는 NULL 값을 무시함
    FROM EMP; -- COMM 컬럼의 합계 조회 (NULL 값은 무시됨)

SELECT ENAME, SAL, SAL*12+COMM AS ANNSAL, COMM
    FROM EMP;

SELECT SUM(DISTINCT SAL),
       SUM(ALL SAL),
       SUM(SAL)
    FROM EMP; -- DISTINCT, ALL 키워드 사용 가능 (ALL은 기본값)

-- 다중행 함수 → COUNT 함수

SELECT COUNT(*)
    FROM EMP; -- EMP 테이블의 행 개수 조회

SELECT COUNT(*)
    FROM EMP
    WHERE DEPTNO = 30; -- DEPTNO가 30인 사원의 행 개수 조회

SELECT COUNT(DISTINCT SAL), -- SAL 컬럼의 중복되지 않은 개수 조회
        COUNT(ALL SAL),
        COUNT(SAL) -- 옵션을 지정 하지 않으면 ALL이 기본
    FROM EMP; -- SAL 컬럼의 개수 조회 (NULL 값은 무시됨)  

SELECT COUNT(COMM)
    FROM EMP;

SELECT COUNT(COMM)
    FROM EMP
    WHERE COMM IS NOT NULL; -- COMM이 NULL이 아닌 사원의 개수 조회

-- 다중행 함수 → MAX/MIN 함수

SELECT MAX(SAL)
    FROM EMP
    WHERE DEPTNO = 10; -- DEPTNO가 10인 사원의 SAL 최대값 조회

SELECT MIN(SAL)
    FROM EMP
    WHERE DEPTNO = 10; -- DEPTNO가 10인 사원의 SAL 최소값 조회

SELECT MAX(HIREDATE)
    FROM EMP
    WHERE DEPTNO = 20; -- DEPTNO가 20인 사원의 최근 입사일 조회

SELECT MIN(HIREDATE)
    FROM EMP
    WHERE DEPTNO = 20; -- DEPTNO가 20인 사원의 가장 오래된 입사일 조회

-- 다중행 함수 → AVG 함수

SELECT AVG(SAL)
    FROM EMP
    WHERE DEPTNO = 30; -- DEPTNO가 30인 사원의 SAL 평균값 조회

SELECT AVG(DISTINCT SAL)
    FROM EMP
    WHERE DEPTNO = 30; -- DEPTNO가 30인 사원의 SAL 중복되지 않은 평균값 조회

-- GROUP BY 절 → 기본

SELECT AVG(SAL), DEPTNO
    FROM EMP
    GROUP BY DEPTNO; -- DEPTNO별 SAL 평균값 조회

SELECT DEPTNO, JOB, AVG(SAL) -- 집계함수와 일반 함수를 함께 사용할 때는 GROUP BY 절 사용
    FROM EMP
GROUP BY DEPTNO, JOB -- DEPTNO, JOB별 그룹화
ORDER BY DEPTNO, JOB; -- DEPTNO, JOB별 SAL 평균값 조회

-- SELECT DEPTNO, JOB, AVG(SAL) -- 검증
--     FROM EMP
-- WHERE JOB = 'CLERK'
--     AND DEPTNO = 10
-- GROUP BY DEPTNO, JOB
-- ORDER BY DEPTNO, JOB;

-- GROUP BY 절 → 유의점

SELECT ENAME, DEPTNO, AVG(SAL)
    FROM EMP
GROUP BY DEPTNO; -- 오류 발생(SELECT 절의 ENAME 컬럼이 GROUP BY 절에 포함되지 않음)

-- HAVING 절 → 기본

SELECT DEPTNO, JOB, AVG(SAL)
    FROM EMP
GROUP BY DEPTNO, JOB
    HAVING AVG(SAL) > 2000 -- 그룹화된 결과에 조건 적용
ORDER BY DEPTNO, JOB;

--유의점
SELECT DEPTNO, JOB, AVG(SAL)
    FROM EMP
    WHERE AVG(SAL) >= 2000 -- 오류 발생(WHERE 절에서는 다중행 함수를 사용할 수 없음)
GROUP BY DEPTNO, JOB   
ORDER BY DEPTNO, JOB; -- WHERE 절은 출력 대상 행을 제한, HAVING 절은 출력 대상 그룹을 제한

-- 실습문제

SELECT DEPTNO, AVG(SAL) AS AVG_SAL, MAX(SAL) AS MAX_SAL, MIN(SAL) AS MIN_SAL, COUNT(*) AS CNT
    FROM EMP
GROUP BY DEPTNO
ORDER BY DEPTNO;

SELECT JOB, COUNT(*)
    FROM EMP
GROUP BY JOB
    HAVING COUNT(*) >= 3
ORDER BY JOB;

SELECT HIREDATE AS HIRE_YEAR, COUNT(*) AS CNT, DEPTNO
    FROM EMP
GROUP BY HIREDATE, DEPTNO
ORDER BY HIREDATE, DEPTNO;

SELECT COMM AS EXIST_COMM, COUNT(*) AS CNT
    FROM EMP
GROUP BY COMM
ORDER BY COMM;

-- ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ
-- Types of Join in SQL
-- Inner Join → 교집합
-- Left Join
-- Right Join
-- Full Outer Join → 합집합

-- 조인문의 기본 예시 → 기본 형태: 카티널 프로덕트(집합의 곱셈으로 만들어짐)
SELECT *
    FROM EMP, DEPT
ORDER BY EMPNO;

-- 조인문의 기본 예시 → 조건식을 사용한 조인
SELECT *
    FROM EMP, DEPT
    WHERE EMP.DEPTNO = DEPT.DEPTNO -- 테이블을 구분하기위해 (테이블명.컬럼명) 으로 명시   
ORDER BY EMPNO;

-- 조인문 → 별칭 설정
SELECT *
    FROM EMP E, DEPT D -- 별칭 설정 (테이블명 뒤에 별칭 지정)
    WHERE E.DEPTNO = D.DEPTNO -- 별칭 사용 (테이블명 대신 별칭 사용)
ORDER BY EMPNO;

-- 조인문 → 등가조인/내부조인(INNER JOIN)
SELECT E.EMPNO, E.ENAME, D.DEPTNO, D.DNAME, D.LOC
    FROM EMP E, DEPT D 
    WHERE E.DEPTNO = D.DEPTNO
ORDER BY D.DEPTNO, E.EMPNO;

SELECT E.EMPNO, E.ENAME, D.DEPTNO, D.DNAME, D.LOC
    FROM EMP E, DEPT D 
    WHERE E.DEPTNO = D.DEPTNO
    AND SAL >= 3000;

-- 조인의 종류 → 비등가 조인
SELECT *
    FROM EMP E, SALGRADE S
    WHERE E.SAL BETWEEN S.LOSAL AND S.HISAL;

-- 조인의 종류 → 자체 조인
SELECT E1.EMPNO, E1.ENAME, E1.MGR, 
    E2.EMPNO AS MGR_EMPNO,
    E2.ENAME AS MGR_ENAME
    FROM EMP E1, EMP E2
    WHERE E1.MGR = E2.EMPNO;

-- 조인의 종류 → 외부 조인
SELECT E1.EMPNO, E1.ENAME, E1.MGR, 
    E2.EMPNO AS MGR_EMPNO,
    E2.ENAME AS MGR_ENAME
    FROM EMP E1, EMP E2
    WHERE E1.MGR = E2.EMPNO(+) -- E1 테이블을 기준으로 E2 테이블의 일치하는 행이 없으면 NULL로 표시
ORDER BY E1.EMPNO;

SELECT E1.EMPNO, E1.ENAME, E1.MGR, 
    E2.EMPNO AS MGR_EMPNO,
    E2.ENAME AS MGR_ENAME
    FROM EMP E1, EMP E2
    WHERE E1.MGR(+) = E2.EMPNO -- E2 테이블을 기준으로 E1 테이블의 일치하는 행이 없으면 NULL로 표시
ORDER BY E1.EMPNO;

-- 표준 SQL 조인 → Natural Join (INNER JOIN 과 결과는 같다)
SELECT E.EMPNO, E.ENAME, E.JOB, E.MGR, E.HIREDATE, 
    E.SAL, E.COMM, DEPTNO, D.DNAME, D.LOC
    FROM EMP E NATURAL JOIN DEPT D
ORDER BY DEPTNO, E.EMPNO;

-- 표준 SQL 조인 → JOIN USING
SELECT E.EMPNO, E.ENAME, E.JOB, E.MGR, E.HIREDATE, 
    E.SAL, E.COMM, DEPTNO, D.DNAME, D.LOC
    FROM EMP E JOIN DEPT D USING (DEPTNO)
    WHERE SAL >= 3000
ORDER BY DEPTNO, E.EMPNO;

-- 표준 SQL 조인 → JOIN ON
SELECT E.EMPNO, E.ENAME, E.JOB, E.MGR, E.HIREDATE,
    E.SAL, E.COMM, E.DEPTNO, D.DNAME, D.LOC
    FROM EMP E JOIN DEPT D ON (E.DEPTNO = D.DEPTNO) -- 조인 조건을 ON 절에 명시
    WHERE SAL >= 3000
ORDER BY E.DEPTNO, EMPNO;

-- 표준 SQL 조인 → LEFT OUTER JOIN
SELECT E1.EMPNO, E1.ENAME, E1.MGR,
    E2.EMPNO AS MGR_EMPNO,
    E2.ENAME AS MGR_ENAME
    FROM EMP E1 LEFT OUTER JOIN EMP E2 ON (E1.MGR = E2.EMPNO) -- E1 테이블을 기준으로 E2 테이블의 일치하는 행이 없으면 NULL로 표시
ORDER BY E1.EMPNO;

-- 표준 SQL 조인 → RIGHT OUTER JOIN
SELECT E1.EMPNO, E1.ENAME, E1.MGR,
    E2.EMPNO AS MGR_EMPNO,
    E2.ENAME AS MGR_ENAME
    FROM EMP E1 RIGHT OUTER JOIN EMP E2 ON (E1.MGR = E2.EMPNO) -- E2 테이블을 기준으로 E1 테이블의 일치하는 행이 없으면 NULL로 표시
ORDER BY E1.EMPNO, MGR_EMPNO;

-- 표준 SQL 조인 → FULL OUTER JOIN
SELECT E1.EMPNO, E1.ENAME, E1.MGR,
    E2.EMPNO AS MGR_EMPNO,
    E2.ENAME AS MGR_ENAME
    FROM EMP E1 FULL OUTER JOIN EMP E2 ON (E1.MGR = E2.EMPNO) -- 양쪽 테이블 모두 일치하는 행이 없으면 NULL로 표시
ORDER BY E1.EMPNO;

-- ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ
-- 서브쿼리의 기본 예시 → Before
SELECT SAL
    FROM EMP
    WHERE ENAME = 'JONES';

SELECT *
    FROM EMP
    WHERE SAL > 2975;

-- 서브쿼리의 기본 예시 → After
SELECT *
    FROM EMP
    WHERE SAL > (SELECT SAL
                    FROM EMP
                    WHERE ENAME = 'JONES');

-- 날짜형 데이터
SELECT *
    FROM EMP
    WHERE HIREDATE < (SELECT HIREDATE
                        FROM EMP
                        WHERE ENAME = 'SCOTT');

-- 함수의 사용
SELECT E.EMPNO, E.ENAME, E.SAL, D.DEPTNO, D.DNAME, D.LOC
    FROM EMP E, DEPT D
    WHERE E.DEPTNO = D.DEPTNO
        AND E.DEPTNO = 20
        AND E.SAL > (SELECT AVG(SAL)
                        FROM EMP);

-- IN 연산자
SELECT *
    FROM EMP
    WHERE DEPTNO IN(20, 30); -- 부서번호가 20, 30인 사원 조회

SELECT *
    FROM EMP
    WHERE SAL IN (SELECT MAX(SAL)
                    FROM EMP
                    GROUP BY DEPTNO); -- 각 부서별 최대 SAL을 가진 사원 조회    

-- ANY, SOME 연산자
SELECT *
    FROM EMP
    WHERE SAL > ANY (SELECT SAL 
                        FROM EMP
                        WHERE DEPTNO = 30) -- DEPTNO가 30인 사원 중 SAL보다 큰 사원 조회
ORDER BY SAL, EMPNO;
                
-- ALL 연산자
SELECT *
    FROM EMP
    WHERE SAL > ALL (SELECT SAL
                        FROM EMP
                        WHERE DEPTNO = 30); -- DEPTNO가 30인 사원 중 SAL보다 큰 사원 조회

-- EXISTS 연산자
SELECT *
    FROM EMP 
    WHERE EXISTS (SELECT DNAME
                    FROM DEPT
                    WHERE DEPTNO = 10); -- DEPTNO가 10인 부서가 존재하면 모든 사원 조회

SELECT *
    FROM EMP 
    WHERE EXISTS (SELECT DNAME
                    FROM DEPT
                    WHERE DEPTNO = 50); -- DEPTNO가 50인 부서가 존재하지 않으면 아무 사원도 조회되지 않음

-- 다중열 서브 쿼리
SELECT *
    FROM EMP
    WHERE (DEPTNO, SAL) IN (SELECT DEPTNO, MAX(SAL)
                            FROM EMP
                            GROUP BY DEPTNO); -- 각 부서별 최대 SAL을 가진 사원 조회

-- FROM 절 서브 쿼리/ InIine View
SELECT E10.EMPNO, E10.ENAME, D.DNAME, D.LOC
    FROM (SELECT * FROM EMP WHERE DEPTNO = 10) E10,
         (SELECT * FROM DEPT) D
WHERE E10.DEPTNO = D.DEPTNO;

-- WITH 절 서브 쿼리/ InIine View
WITH
    E10 AS (SELECT * FROM EMP WHERE DEPTNO = 10),
    D AS (SELECT * FROM DEPT)
SELECT E10.EMPNO, E10.ENAME, D.DNAME, D.LOC
    FROM E10, D
WHERE E10.DEPTNO = D.DEPTNO;

-- SELECT 절 서브 쿼리
SELECT EMPNO, ENAME, JOB, SAL,
        (SELECT GRADE
            FROM SALGRADE
            WHERE E.SAL BETWEEN LOSAL AND HISAL) AS SALGRADE,
        DEPTNO,
        (SELECT DNAME
            FROM DEPT
            WHERE E.DEPTNO = DEPT.DEPTNO) AS DNAME
    FROM EMP E;

-- 연습문제
SELECT E.JOB, E.EMPNO, E.ENAME, E.SAL, D.DEPTNO, D.DNAME
    FROM EMP E JOIN DEPT D ON (E.DEPTNO = D.DEPTNO)
    WHERE JOB = 'SALESMAN'
        AND E.SAL > (SELECT AVG(SAL)
                        FROM EMP
                        WHERE JOB = 'SALESMAN');