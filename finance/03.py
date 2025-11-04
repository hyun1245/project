from pandas import Series

# data = [10,20,30]
# # 레이블(label)[행 번호]이 붙은 1차원 배열
# s = Series(data)
# print(s)

import numpy as np

data = np.arange(3) #3보다 작은 정수 (0,1,2)를 1차원으로 배열 
# print(data)
s = Series(data)
# print(s)

# data = ["시가","고가"]
# s = Series(data)
# print(s)

#broadcasting -> 뒤축이  1이면 된다.


# s = Series(['samsung', 81000])
# print(s)

data = [1000, 2000, 3000]
# pandas의 Series 객체로 변환. 인덱스는 기본값인 0, 1, 2 자동 생성됨.
s = Series(data) 
# print(s)

# Series의 인덱스 정보를 출력. 기본은 RangeIndex(start=0, stop=3, step=1)
# print('s.index:',s.index)

# 인덱스를 리스트로 변환하여 출력. [0, 1, 2]가 반환됨  
# print('s.index.to_list():',s.index.to_list())

# data = [1000, 2000, 3000] 
# s = Series(data)
# s.index = ["메로나", "구구콘", "하겐다즈"]
# print(s)
# print(s.index)


# data = [1000, 2000, 3000]
# index = ["메로나", "구구콘", "하겐다즈"]

# #컨트롤 + 마우스를 클릭하면 해당함수의 소스를 분석할 수 있다.
# #명시적으로 index를 지정
# s = Series(data = data, index = index) 
# print(s) 

k = [1000, 2000, 3000]
v = ["메로나", "구구콘", "하겐다즈"]

s = Series(data=v, index=k)
# print(s)


#전부 구조가 동일
# s = Series(data, index)
# s = Series(data, index=index)
# s = Series(data = data, index = index)
# s = Series(index = index, data = data)

data = [1000, 2000, 3000]
index = ['메로나', '구구콘', '하겐다즈']
s = Series(data=data, index=index)

# print("s = ", s)

# reindex는 Series의 인덱스를 변경하거나 재배열할 때 사용한다.
# 존재하지 않는 인덱스를 지정하면 NaN으로 표시
s2 = s.reindex(["메로나", "비비빅", "구구콘"])
# print('s2 = ',s2)

# price = [42500,42550,41800,42550,42650]
# date = ["2019-05-31", "2019-05-30", "2019-05-29", "2019-05-28", "2019-05-27"]
# #default Series(data, index)
# s = Series(price, date)
# print(s) 

# data = {
#     "2019-05-31": 42500,
#     "2019-05-30": 42550,
#     "2019-05-29": 41800,
#     "2019-05-28": 42550,
#     "2019-05-27": 42650
# }
# s = Series(data)
# print(s)

# print(s.index) # index 출력
# print(s.index.dtype) # index 의 데이터 타입 출력

# print(s.values) # data 출력

# data =[1000,2000,3000]
# s = Series(data)

# print(s)

# # 인덱싱이기 떄문에 인덱스의 값만 가져옴

# # s.iloc ->  data 기반(인덱스 라벨과 상관없이 데이터가 저장된 순서(위치)를 기준으로 선택)
# print('s.iloc[0] = ',s.iloc[0])
# print('s.iloc[1] = ',s.iloc[1])
# print('s.iloc[2] = ',s.iloc[2])
# print('s.iloc[-1] = ',s.iloc[-1]) # 끝에서부터 값을 가져오는 방법 -1
# print('s.iloc[-2] = ',s.iloc[-2]) # 끝에서부터 두번째 값을 가져오는 방법 -2

# s.loc -> 인덱스 기반(인덱스(라벨)을 이용해 선택, 문자열 인덱스도 가능)
# print(s.loc[0])
# print(s.loc[1])
# print(s.loc[2])
# print(s.loc[-1]) #에러(위치 기반인 s.iloc은 인식 할 수있지만 s.loc는 인식 못함)

# data = [1000,2000,3000]
# index = ['메로나', '구구콘', '하겐다즈']
# s = Series(data=data, index=index)

# print(s.iloc[0]) #행기반 
# print(s.loc['메로나']) #인덱스 기반
# print(s.loc['구구콘'])

# print(s['메로나'])
# print(s[0]) #경고 발생 가능, 위치가 아닌 라벨로 작동 

# data = [1000,2000,3000]
# index = ['메로나', '구구콘', '하겐다즈']
# # s = Series(data=data, index=index) # 출력결과는 오른쪽이 인덱스 왼쪽이 값이다
# s = Series(data = index, index = data)
# print(s)
# print(s.iloc[0:2])

# data = [1000,2000,3000]
# index = ['메로나', '구구콘', '하겐다즈']
# s = Series(data=data, index=index)

# print(s.loc['메로나':'구구콘'])

#시험문제
data = [1000,2000,3000]
index = ['메로나', '구구콘', '하겐다즈']
s = Series(data=data, index=index)

indices = [0,2]
# print('s.iloc[indices] =',s.iloc[indices])
# print('s.iloc[[0,2]] =',s.iloc[[0,2]])

# data = [1000,2000,3000]
# Index = ['메로나', '구구콘', '하겐다즈']
# s = Series(data=data, index=Index) 

# indices = ['메로나', '하겐다즈']
# print('s.loc[indices] =',s.loc[indices])
# print('s.loc[["메로나", "하겐다즈"]] =',s.loc[['메로나', '하겐다즈']])

data = [1000,2000,3000]
index = ['메로나', '구구콘', '하겐다즈']
s = Series(data=data, index=index)

# s.loc['메로나'] = 500 #값수정
# s.iloc[0] = 500 #값수정
# print(s)

# s.loc['비비빅'] = 500  #값 추가
# print(s)

# print(s.drop('메로나')) #Series.drop -> 특정 index를 제거
# print('s = ',s)


# s = s.drop('메로나') # drop은 원본에 영향을 주지 않음
# print(s)

철수 = Series([10,20,30], index = ["NAVER", "SKT", "KT"])
영희 = Series([10,30,20], index = ["SKT","NAVER", "KT"])
가족 = 철수 + 영희
# print(가족) # 인덱스 기준으로 더함 자동으로 내림차순 정렬

# print(철수 * 30)

# high = Series([42800, 42700, 42050, 42950, 43000])
# low = Series([42150, 42150, 41300, 42150, 42350])

# diff = high - low
# print(diff)

# print(diff.max()) #최대값
# print(diff.min()) #최소값

# 인덱스로 사용할 날짜 리스트
# date = ["6/1", "6/2", "6/3", "6/4", "6/5"]
# # date를 인덱스로 하는 고가(high)와 저가(low) 시리즈 생성
# high = Series([42800, 42700, 42050, 42950, 43000], index=date)
# low = Series([42150, 42150, 41300, 42150, 42350] , index=date)
# diff = high - low
# print(diff)

# 최대 변동폭과 해당위치를 찾기 위해 for문 사용
# max_idx = 0
# max_val = 0

# for i in range(len(diff)):
#     if diff[i] > max_val:
#         max_val = diff.iloc[i]
#         max_idx = i
        # print("max_val =", max_val, ", max_idx =", max_idx)
# max_val = diff.iloc[i], max_idx = i: 만약 현재 값이 더 크다면, 
# max_val을 새로운 최대값으로 업데이트하고, 그 위치 i를 max_idx에 저장합니다.

# print(max_idx)
# print(diff.index[max_idx]) 


# print(diff.idxmax()) #최대값의 index를 반환
# print(diff.idxmin()) #최소값의 index를 반환

# date = ["6/1", "6/2", "6/3", "6/4", "6/5"]
# high = Series([42800, 42700, 42050, 42950, 43000], index=date)
# low = Series([42150, 42150, 41300, 42150, 42350] , index=date)
# profit = ((high - low)/ low) * 100
# print(profit)

# print(profit.cumprod()) #누적 수익률(누적 곱)[수익률을 복리로 적용]

# print(profit.cumprod().iloc[-1]) # iloc[-1] -> 가장 최근의 값

# data = {
#     "삼성전자": "전기,전자",
#     "LG전자": "전기,전자",
#     "현대차": "운수장비",
#     "NAVER": "서비스업",
#     "카카오": "서비스업"
# }
# s = Series(data)
 
# print(s.value_counts()) #각각의 값(data)이 몇개씩 있는지

from pandas import Series
s= Series(['1,234','5,678','9,876'])
# int() -> 단일 숫자나 문자열 값을 정수로 변환하는 함수
# 하지만 Series 객체는 여러개의 값을 담고있는 자료구조 로서 에러를 발생 시킴
# print(s.str.replace(",","").astype('int64')) #문자열의 모든 쉼표(,)를 제거
# print(s.apply(lambda x: int(x.replace(",","")))) #람다함수 이용
# print(int(s)) #정수형으로 변환 

# 함수를 정의할때 사용
# x 값과 , in function 이라는 문자열을 출력하고
# x 값을 반환하는 함수
# def remove_comma(x):
#     print(x, 'in function')
#     return x

# s.map(함수)는 "s의 모든 요소(element)를 하나씩 꺼내서, 
# 지정된 '함수'에 입력값으로 넣고, 함수가 반환하는 결과값으로 대체하라"는 의미
# 이과정을 Mapping 이라고함
# s = Series(['1,234','5,678','9,876'])
# result = s.map(remove_comma)
# print(result)

from pandas import Series

# # 문자열 x를 입력받아, x 안에 있는 모든 쉼표(,)를 제거한 후,
# # 정수형(int)로 변환하여 반환하는 함수
# # .replace("old", "new") -> 문자열에서 old를 new로 바꿔주는 함수
# def remove_comma(x) :
#     return int(x.replace(",", "")) 

# s = Series(["1,234", "5,678", "9,876"])
# result = s.map(remove_comma)
# print(result)

# def is_greater_than_5000(x):
#     if x > 5000:
#         return "크다"
#     else:
#         return "작다"

# s = Series([1234, 5678, 9876])
# s = s.map(is_greater_than_5000)
# print(s)

from pandas import Series

# data = [42500, 42550, 41800, 42550, 42650]
# index = ['2019-05-31', '2019-05-30', '2019-05-29', '2019-05-28', '2019-05-27']
# s = Series(data=data, index=index)
# # cond = s > 42000: 이 코드는 s Series의 모든 요소에 대해 > 42000이라는 비교 연산을 수행
# cond = s > 42000
# # cond 시리즈는 s와 동일한 인덱스를 가지며,
# # 각 인덱스에 해당하는 값이 42000을 초과하는지에 대한 True/False 값을 가집니다.
# print(cond)

# ## 불리언 인덱싱(True와 False로 이루어진 불리언(Boolean) 값들을 사용하여 데이터를 걸러내는 방식)의 핵심
# #  s[cond] -> Series인 cond에서  값이 True인 위치에 해당하는 요소들만 선택
# print(s[cond])

# close = [42500, 42550, 41800, 42550, 42650] #종가
# open = [42600, 42200, 41850, 42550, 42500] #시가
# index = ['2019-05-31', '2019-05-30', '2019-05-29', '2019-05-28', '2019-05-27']

# open = Series(data=open, index=index)
# close = Series(data=close, index=index)

# cond = close > open #종가가 시가보다 큰지
# print(cond)

# cond = close > open
# print(close[cond]) #종가가 시가보다 큰날의 종가를 출력

# print(close[close > open]) # print(close[cond])와 동일한 함수

# print(close.index[close > open]) # print(close[close > open].index) 와 동일한 함수
# print(close[close > open].index) #종가가 시가보다 큰날의 index 를 출력
# print(close[close > open].values) #종가가 시가보다 큰날의 data(종가) 를 출력

# close = [42500, 42550, 41800, 42550, 42650]
# open = [42600, 42200, 41850, 42550, 42500]
# index = ['2019-05-31', '2019-05-30', '2019-05-29', '2019-05-28', '2019-05-27']

# open = Series(data=open, index=index)
# close = Series(data=close, index=index)
# diff = close - open
# print(diff[close > open]) #종가가 시가보다 큰날의 변동폭의 차 를 출력

from pandas import Series

data = [3.1, 2.0, 10.1, 5.1]
index = ['000010', '000020', '000030', '000040']
s = Series(data=data, index=index)
print(s)

# 정렬 (오름차순)
s1 = s.sort_values()
print('오름 =',s1)

# 정렬 (내림차순)
s2 = s.sort_values(ascending=False) #ascending=False 내림차순
print('내림 =',s2)

data = [3.1,2.0,10.1,3.1]
index = ['000010', '000020', '000030', '000040']
s = Series(data = data, index = index)
print(s)

print('오름차순 = ',s.rank())

print('내림차순 = ',s.rank(ascending=False, method='min'))