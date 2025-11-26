import re

# 1. 휴대폰 번호 유효성 검사 (010-XXXX-XXXX 형식)
def check_phone_number(number):
    # '01'로 시작하며, 0~9 중 하나의 숫자가 온 뒤, 
    # '-'로 구분된 3~4자리 숫자, 다시 '-'로 구분된 4자리 숫자가 오는 패턴
    # re.match는 문자열의 시작부터 패턴 일치 여부를 확인합니다.
    pattern = r'^01[0|1|6|7|8|9]-\d{3,4}-\d{4}$'
    if re.match(pattern, number):
        return f"'{number}'은(는) 유효한 휴대폰 번호 입니다."
    else:
        return f"'{number}'은(는) 유효하지 않은 휴대폰 번호입니다."

# 2. 주민등록번호 유효성 검사 (앞 6자리 - 뒤 7자리 형식)
def check_resident_id(id_number):
    # ^: 문자열의 시작
    # \d{6}: 6자리 숫자
    # -: 하이픈
    # [1-4]: 1, 2, 3, 또는 4 중 하나의 숫자 (성별 구분자)
    # \d{6}: 뒤따르는 6자리 숫자
    # $: 문자열의 끝
    pattern = r'^\d{6}-[1-4]\d{6}$'
    if re.match(pattern, id_number):
        return f"'{id_number}'은(는) 유효한 주민등록번호 형식입니다."
    else:
        return f"'{id_number}'은(는) 유효하지 않은 주민등록번호 형식입니다."

# 3. 이메일 주소 유효성 검사 (문자+숫자@도메인.최상위도메인 형식)
def check_email(email):
    # ^[a-zA-Z0-9._%+-]+: @ 앞 부분 (영문 대소문자, 숫자, 특수문자 허용)
    # @: @ 기호
    # [a-zA-Z0-9.-]+: 도메인 부분 (영문, 숫자, 하이픈, 점 허용)
    # \.[a-zA-Z]{2,}: . 이후 2글자 이상 (최상위 도메인)
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if re.match(pattern, email):
        return f"'{email}'은(는) 유효한 이메일 형식입니다."
    else:
        return f"'{email}'은(는) 유효하지 않은 이메일 형식입니다."

# --- 실행 예시 ---
print(check_phone_number("010-1234-5678"))
print(check_phone_number("02-123-4567"))

print(check_resident_id("900101-1234567"))
print(check_resident_id("001231-5999999"))

print(check_email("test.user123@google.co.kr"))
print(check_email("invalid-email@.com"))