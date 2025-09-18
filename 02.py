#import numpy as np # 패키지를 설치할때 아나콘다의 open terminal에서 pip install numpy 입력
#data = [1,2,3]
#arr = np.array(data)
#print(arr)
#print(type(arr)) 

# data = [1,2,3]

# result = [10]
# for i in data:
#     result.append(i*10)
#     print("for result = ",result)

# print("final result = ",result)

# import numpy as np
# arr = np.array(data)
# result = arr * 10
# print("fianal result = ",result)

# import numpy as np
# arr = np.arange(20).reshape(4, 5)
# print(arr)
# print(arr[:3])

# result =[]
# for row in arr:
#     row_01 = [row[0], row[1]]
#     result.append(row_01)
#     print("result = ",result)

# print("final result = ",result)

# print(arr[:,:2]) # 4개의 행을 전부 가져오고 2번째 까지의 열을 가져온다

# print(arr[0:4, 2:5]) # 0~4행 , #3~5열 
# print(arr[:4, 2:])

# a = np.array([1,2,3])
# b = np.array([2,3,4])

# print("a = ",a)
# print("b = ",b) 

# print("a + b = ", a + b)
# print("a * b = ", a * b)
# print("a % b = ", a % b)

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
# # print(arr[0] * 3 + arr[1]  * 2)

# weight = np.array([3, 2]).reshape(2, 1)
# print("weight = ",weight)   
# print((weight * arr).sum(axis=0)) # axis = 0 이면 x축 , axix = 1 이면 y 축

# arr = np.array( [10, 20, 30] )
# print(arr > 10)

# arr = np.array([10, 20, 30])
# cond = [False, True, True]
# print(arr[ cond ])

# arr = np.array([10, 20, 30])
# cond0 = arr > 10
# print("cond0 = ",cond0)
# cond1 = arr < 30
# print("cond1 = ",cond1)
# print("cond0 & cond1 = ", cond0 & cond1) # and
# print(arr[cond0 & cond1])

# arr = np.array([10, 20, 30])
# arr = np.where( arr > 10, 1, 0) # 조건문 10 초과이면 1 아니면 0 
# print(arr)

# arr = np.arange(8).reshape(4, 2)
# print("arr = ",arr)

# print(arr.sum(axis=0)) # 열끼리 더함
# print(arr.sum(axis=1)) # 행끼리 더함

# np.random.randint(46, size=(2, 5))
# print(np.random.randint(46, size=(2, 5)))

a = np.arange(4)
print("a = ",a)
b = np.arange(4, 8)
print("b = ",b) 
print("np.vstack([a,b}) =",np.vstack([a, b]))
print("np.hstack([a,b}) = ",np.vstack([a, b]))


# gpt 의 작동 
# 인코더(Bert) + 디코더(GPT, AI) = Transformer
# true/false -> 범주형
# 0,1,2, -> 정수형
# 0.1, 0.2, 0.3 -> 실수형
# 양자화 -> 기존의 0~8까지 썻던 메모리를 0~4 로 줄임으로서 메모리는 절반으로 절약하고 
#           속도는 비슷하게 유지 함
# 슬라이싱 -> 데이터를 잘라서 가져올 수 있는 방법
