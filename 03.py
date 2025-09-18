from pandas import Series

#data - [10,20,30]
# s = Series(data)
# print(s)

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

data =[1000,2000,3000]
s = Series(data)

# print('s.iloc[0] = ',s.iloc[0])
# print('s.iloc[1] = ',s.iloc[1])
# print('s.iloc[2] = ',s.iloc[2])
# print('s.iloc[-1] = ',s.iloc[-1])

# print(s.loc[0])
# print(s.loc[1])
# print(s.loc[2])
# print(s.loc[-1]) #에러

data = [1000,2000,3000]
index = ['메로나', '구구콘', '하겐다즈']
s = Series(data=data, index=index)

print(s.iloc[0])
print(s.loc['메로나'])
print(s.loc['구구콘'])

