from pandas import Series

data - [10,20,30]
# 레이블(label)이 붙은 1차원 배열
s = Series(data)
print(s)

import numpy as np

# data = np.arange(S)
#s = Series(data)
#print(s)

# data = ["시가","고가"]
# s = Series(data)
# print(s)

#broadcasting -> 뒤축이  1이면 된다.


# s = Series(['samsung', 81000])
# print(s)

# data = [1000, 2000, 3000]
# s = Series(data)
# print('s.index:',s.index)
# print('s.index.to_list):',s.index.to_list())

# data = [1000, 2000, 3000] 
# s = Series(data)
# s.index = ["메로나", "구구콘", "하겐다즈"]
# print(s)


# data = [1000, 2000, 3000]
# index = ["메로나", "구구콘", "하겐다즈"]

# #컨트롤 + 마우스를 클릭하면 해당함수의 소스를 분석할 수 있다.
# #명시적으로 index를 지정
# s = Series(data = data_1, index = index) 
# print(s) 

# k = [1000, 2000, 3000]
# v = ["메로나", "구구콘", "하겐다즈"]

# s = Series(data=v, index=k)
# print(s)


#전부 구조가 동일
# s = Series(data, index)
# s = Series(data, index=index)
# s = Series(data = data, index = index)
# s = Series(index = index, data = data)

# data = [1000, 2000, 3000]
# index = ['메로나', '구구콘', '하겐다즈']
# s = Series(data=data, index=index)

# print("s = ", s)

# s2 = s.reindex(["메로나", "비비빅", "구구콘"])
# print('s2 = ',s2)

# price = [42500,42550,41800,42550,42650]
# date = ["2019-a05-31", "2019-05-30", "2019-05-29", "2019-05-28", "2019-05-27"]
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

# print(s.index)
# print(s.index.dtype)

# print(s.values)

# data =[1000,2000,3000]
# s = Series(data)

# print('s.iloc[0] = ',s.iloc[0])
# print('s.iloc[1] = ',s.iloc[1])
# print('s.iloc[2] = ',s.iloc[2])
# print('s.iloc[-1] = ',s.iloc[-1])

# print(s.loc[0])
# print(s.loc[1])
# print(s.loc[2])
# print(s.loc[-1]) #에러

# data = [1000,2000,3000]
# index = ['메로나', '구구콘', '하겐다즈']
# s = Series(data=data, index=index)

# print(s.iloc[0]) #행기반 
# print(s.loc['메로나']) #인덱스 기반
# print(s.loc['구구콘'])

# print(s['메로나'])
# print(s[0])

# data = [1000,2000,3000]
# index = ['메로나', '구구콘', '하겐다즈']
# s = Series(data=data, index=index)

# print(s.iloc[0:2])

# data = [1000,2000,3000]
# index = ['메로나', '구구콘', '하겐다즈']
# s = Series(data=data, index=index)

# print(s.loc['메로나':'구구콘'])

# #시험문제
# data = [1000,2000,3000]
# index = ['메로나', '구구콘', '하겐다즈']
# s = Series(data=data, index=index)

# indices = [0,2]
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
# print(s)

# s.loc['비비빅'] = 500  #값 추가
# print(s)

# print(s.drop('메로나')) #Series.drop -> 특정 index를 제거
# print('s = ',s)


# s = s.drop('메로나')
# print(s)

# 철수 = Series([10,20,30], index = ["NAVER", "SKT", "KT"])
# 영희 = Series([10,30,20], index = ["SKT","NAVER", "KT"])
# 가족 = 철수 + 영희
# print(가족)

# print(철수 * 30)

# high = Series([42800, 42700, 42050, 42950, 43000])
# low = Series([42150, 42150, 41300, 42150, 42350])

# diff = high - low
# print(diff)

# print(diff.max())

# date = ["6/1", "6/2", "6/3", "6/4", "6/5"]
# high = Series([42800, 42700, 42050, 42950, 43000], index=date)
# low = Series([42150, 42150, 41300, 42150, 42350] , index=date)
# diff = high - low
# # print(diff)

# max_idx = 0
# max_val = 0

# for i in range(len(diff)):
#     if diff[i] > max_val:
#         max_val = diff.iloc[i]
#         max_idx = i

# print(max_idx)
# print(diff.index[max_idx]) 
# 
# print(diff.idxmax()) #최대값의 index를 반환
# print(diff.idxmin()) #최소값의 index를 반환

# date = ["6/1", "6/2", "6/3", "6/4", "6/5"]
# high = Series([42800, 42700, 42050, 42950, 43000], index=date)
# low = Series([42150, 42150, 41300, 42150, 42350] , index=date)
# profit = ((high - low)/ low) * 100
# # print(profit)

# print(profit.cumprod()) #누적 수익률

# print(profit.cumprod().iloc[-1]) # iloc[-1] -> 가장 최근의 값

# data = {
#     "삼성전자": "전기,전자",
#     "LG전자": "전기,전자",
#     "현대차": "운수장비",
#     "NAVER": "서비스업",
#     "카카오": "서비스업"
# }
# s = Series(data)
 
# print(s.value_counts()) #각각의 값이 몇개씩 있는지

# from pandas import Series
# s= Series(['1,234','5,678','9,876'])
# print(int(s))

# def remove_comma(x):
#     return int(x, 'in function')
#     return x

# s = Series(['1,234','5,678','9,876'])
# result = s.map(remove_comma)
# print(result)

# from pandas import Series

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

# from pandas import Series

# data = [42500, 42550, 41800, 42550, 42650]
# index = ['2019-05-31', '2019-05-30', '2019-05-29', '2019-05-28', '2019-05-27']
# s = Series(data=data, index=index)
# cond = s > 42000
# print(cond)

# print(s[cond])

# close = [42500, 42550, 41800, 42550, 42650]
# open = [42600, 42200, 41850, 42550, 42500]
# index = ['2019-05-31', '2019-05-30', '2019-05-29', '2019-05-28', '2019-05-27']

# open = Series(data=open, index=index)
# close = Series(data=close, index=index)

# cond = close > open
# print(cond)

# cond = close > open
# print(close[cond])

# print(close[close > open])

# print(close.index[close > open])
# print(close[close > open].index)

# close = [42500, 42550, 41800, 42550, 42650]
# open = [42600, 42200, 41850, 42550, 42500]
# index = ['2019-05-31', '2019-05-30', '2019-05-29', '2019-05-28', '2019-05-27']

# open = Series(data=open, index=index)
# close = Series(data=close, index=index)
# diff = close - open
# print(diff[close > open])

# from pandas import Series

# data = [3.1, 2.0, 10.1, 5.1]
# index = ['000010', '000020', '000030', '000040']
# s = Series(data=data, index=index)
# print(s)

# # 정렬 (오름차순)
# s1 = s.sort_values()
# print('오름 =',s1)

# # 정렬 (내림차순)
# s2 = s.sort_values(ascending=False)
# print('내림 =',s2)

# data = [3.1,2.0,10.1,3.1]
# index = ['000010', '000020', '000030', '000040']
# s = Series(data = data, index = index)

# print('오름차순 = ',s.rank())

# print('내림차순 = ',s.rank(ascending=False, method='min'))