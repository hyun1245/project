# # 패키지를 설치할때 아나콘다의 open terminal에서 pip install numpy 입력
# import numpy as np 

# data = [1,2,3]
# #numpy 배열로 변환하는 array 함수
# arr = np.array(data)
# print(arr)
# #arr 의 데이터 타입을 출력하는 코드
# print(type(arr)) 

# data = [1,2,3]

# result = [10]
# for i in data:
#     result.append(i*10) #기존 리스트 마지막 항목에 i*10 을 추가
#     print("for result = ",result)

# print("final result = ",result)

# import numpy as np
# arr = np.array(data)
# result = arr * 10
# print("fianal result = ",result)

# import numpy as np
# arr = np.arange(20).reshape(4, 5) # 0~19 까지의 숫자를 4행 5열로 변환
# print(arr)
# print(arr[:3])

# # result 를 [] 라는 공백으로 지정하고 row_01 이라는 변수를 만들어 
# # 이안에 row의 각 0,1 번째 해당하는 값을 총 행의 개수인 4번 반복하여 리스트를 구성한다
# result =[]
# for row in arr:
#     row_01 = [row[0], row[1]]
#     result.append(row_01)
#     print("result = ",result)

# print("final result = ",result)

# print(arr[:,:2]) # 4개의 행을 전부 가져오고 2번째 까지의 열을 가져온다

# print(arr[0:4, 2:5]) # 0~3행 , #2~4열 
# print(arr[:4, 2:])

import numpy as np
# a = np.array([1,2,3])
# b = np.array([2,3,4])

# print("a = ",a)
# print("b = ",b) 

# print("a + b = ", a + b)
# print("a * b = ", a * b)
# print("a % b = ", a / b)

# print("a + 10 = ", a + 10)

# high = [92700, 92400, 92100, 94300, 92300]
# low = [90000, 91100, 91700, 92100, 90900]

# arr_high = np.array(high)
# arr_low = np.array(low)

# arr_diff = arr_high - arr_low
# print(arr_diff)

# arr_high_x3 = arr_high * 3
# arr_low_x2 = arr_low * 2
# print("arr_high_x3 + arr_low_x2 ", arr_high_x3 + arr_low_x2)

# data = [
#     [92700, 92400, 92100, 94300, 92300],
#     [90000, 91100, 91700, 92100, 90900]
# ]
# arr = np.array(data)
# print("arr = ",arr)
# 첫번째 행의 값 * 3 + 두번째 행의 값 * 2
# print(arr[0] * 3 + arr[1]  * 2) 

# weight = np.array([3, 2]).reshape(2, 1)
# print("weight = ",weight)
# # axis = 0 이면 행방향(x축)[각 열의 합계] , axix = 1 이면 열방향(y축)[각 행의 합계]   
# print((weight * arr).sum(axis=0)) 

# arr = np.array( [10, 20, 30] )
# #조건에 맞는값은 True, 아니면 False
# print(arr > 10)

# arr = np.array([10, 20, 30])
# cond = [False, True, True]
# #arr(cond) 는 arr 에서 cond 가 True 인 값만 출력
# print(arr[ cond ])

# arr = np.array([10, 20, 30])
# cond0 = arr > 10 # 10 초과의 값은 True
# print("cond0 = ",cond0)
# cond1 = arr < 30 # 30 미만의 값은 True
# print("cond1 = ",cond1)
# print("cond0 & cond1 = ", cond0 & cond1) # and 둘다 조건 복합 적용 (10 < arr < 30)
# print(arr[cond0 & cond1])

# arr = np.array([10, 20, 30])
# arr = np.where( arr > 10, 1, 0) # 조건문 10 초과이면 1 아니면 0 
# print(arr)

# arr = np.arange(8).reshape(4, 2) # 0~7 까지의 숫자를 4행 2열로 변환
# print("arr = ",arr)

# print(arr.sum(axis=0)) # 열끼리 더함(각 값을 행으로 재배열)
# print(arr.sum(axis=1)) # 행끼리 더함(각 값을 열로 재배열)

# np.random.randint(46, size=(2, 5)) # 0~45 까지의 숫자중에서 2행 5열로 랜덤하게 추출
# print(np.random.randint(46, size=(2, 5)))

# a = np.arange(4) # 0~3 까지의 숫자를 1차원 배열로 생성
# print("a = ",a) # a =  [0 1 2 3]
# b = np.arange(4, 8) # 4~7 까지의 숫자를 1차원 배열로 생성
# print("b = ",b) # b =  [4 5 6 7]
# print("np.vstack([a,b}) =",np.vstack([a, b])) # 수직방향으로 쌓기
# print("np.hstack([a,b}) = ",np.hstack([a, b])) # 수평방향으로 쌓기


# gpt 의 작동 
# 인코더(Bert) + 디코더(GPT, AI) = Transformer
# true/false -> 범주형
# 0,1,2, -> 정수형
# 0.1, 0.2, 0.3 -> 실수형
# 양자화 -> 기존의 0~8까지 썻던 메모리를 0~4 로 줄임으로서 메모리는 절반으로 절약하고 
#           속도는 비슷하게 유지 함
# 슬라이싱 -> 데이터를 잘라서 가져올 수 있는 방법

# 수정이 안되야되는 로그 데이터는 튜플로 적용 