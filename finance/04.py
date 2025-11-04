# from pandas import DataFrame

# data = [
#     ["037730", "3R", 1510, 7.36],
#     ["036360", "3SOFT", 1790, 1.65],
#     ["005670", "ACTS", 1185, 1.28]
# ]

# columns = ["종목코드", "종목명", "현재가", "등락률"]
# df = DataFrame(data=data, columns=columns) #파라미터를 명시해주는 습관을 들여야 오류가 안생김 
# print(df)

# from pandas import DataFrame

# data = [
#     ["037730", "3R", 1510, 7.36],
#     ["036360", "3SOFT", 1790, 1.65],
#     ["005670", "ACTS", 1185, 1.28]
# ]

# columns = ["종목코드", "종목명", "현재가", "등락률"]
# df = DataFrame(data=data, columns=columns)
# #set_index 로 지정하게 되면 그 해당 항목이 인덱스를 표시하는 기준이됨
# df = df.set_index("종목코드")
# print(df)

# from pandas import DataFrame

# data = [
#     ["037730", "3R", 1510, 7.36],
#     ["036360", "3SOFT", 1790, 1.65],
#     ["005670", "ACTS", 1185, 1.28]
# ]

# columns = ["종목코드", "종목명", "현재가", "등락률"]
# df = DataFrame(data=data, columns=columns)
# df.set_index("종목코드", inplace=True) #inplace = True 로 지정하게 되면 원본이 바뀜
# print(df)

from pandas import DataFrame

# data = [
#     ["3R", 1510, 7.36],
#     ["3SOFT", 1790, 1.65],
#     ["ACTS", 1185, 1.28]
# ]

# index = ["037730", "036360", "005760"]
# columns = ["종목명", "현재가", "등락률"]
# df = DataFrame(data=data, index=index, columns=columns)
# index.name 으로 인덱스의 이름을 지정할 수 있음
# df.index.name = "종목코드"
# print(df)
# print(df["현재가"])

# print(df.현재가)

## colunm indexing

from pandas import DataFrame

# data = [
#     ["3R", 1510, 7.36],
#     ["3SOFT", 1790, 1.65],
#     ["ACTS", 1185, 1.28]
# ]

# index = ["037730", "036360", "005760"]
# columns = ["종목명", "현재가", "등락률"]
# df = DataFrame(data=data, index=index, columns=columns)
# print(df['현재가'])

# s = df['현재가']
# print(s.index)
# print(s.values)

# list = ["현재가","등략률"]
# print(df[list])

# print(df[["현재가","등락률"]])


## row indexing

# data = [
#     ["3R", 1510, 7.36],
#     ["3SOFT", 1790, 1.65],
#     ["ACTS", 1185, 1.28]
# ]

# index = ["037730", "036360", "005760"]
# columns = ["종목명", "현재가", "등락률"]
# df = DataFrame(data=data, index=index, columns=columns)
# print(df)

# df.loc["037730"]

# print(df.iloc[0])
# print(df.iloc[-1])

# print(df.loc[["037730","036360"]])
# print(df.iloc[[0,2]])

# from pandas import DataFrame

# data = [
#     ["3R", 1510, 7.36],
#     ["3SOFT", 1790, 1.65],
#     ["ACTS", 1185, 1.28]
# ]

# index = ["037730", "036360", "005760"]
# columns = ["종목명", "현재가", "등락률"]
# df = DataFrame(data=data, index=index, columns=columns)

# print(df.iloc[0])
# print(df.loc['037730'])

# 행번호로 행 선택 후 시리즈 인덱싱 
# print(df.iloc[0].iloc[1])            # 시리즈 행번호
# print(df.iloc[0].loc["현재가"])        # 시리즈 인덱스 
# print(df.iloc[0]["현재가"])            # 시리즈 인덱스

# 인덱스로 행 선택 후 시리즈 인덱싱 
# print(df.loc["037730"].iloc[1])      # 시리즈 행번호
# print(df.loc["037730"])  # 시리즈 인덱스

# print(df.loc["037730"].loc["현재가"])  # 시리즈 인덱스 
# print(df.loc["037730"]["현재가"])      # 시리즈 인덱스

# from pandas import DataFrame

# data = [
#     ["3R", 1510, 7.36],
#     ["3SOFT", 1790, 1.65],
#     ["ACTS", 1185, 1.28]
# ]

# index = ["037730", "036360", "005760"]
# columns = ["종목명", "현재가", "등락률"]
# df = DataFrame(data=data, index=index, columns=columns)

# 괄호가 2개이면 Series 형태가 아닌 DataFrame 형태로 나옴
# print(df.loc[["037730", "036360"]]) 
# print(df.iloc[[0, 1]])

# print(df.loc[["037730", "036360"], ["종목명", "현재가"]]) #DataFrame
# print(df.iloc[ [0, 1], [0, 1] ])

# from pandas import DataFrame

# data = [
#     ["3R", 1510, 7.36],
#     ["3SOFT", 1790, 1.65],
#     ["ACTS", 1185, 1.28]
# ]

# index = ["037730", "036360", "005760"]
# columns = ["종목명", "현재가", "등락률"]
# df = DataFrame(data=data, index=index, columns=columns)
# # print(df)

# cond = df['현재가'] >= 1400

# # print("cond = ", cond)

# # print(df.loc[cond])

# cond = df['현재가'] >= 1400
# # print(df.loc[cond]["현재가"])

# # print(df.loc[cond, "현재가"])

# # & 연산자를 사용할때는 괄호로 묶어줘야함
# cond = (df['현재가'] >= 1400) & (df['현재가'] < 1700) #파이썬에서는 and 이지만 pandas에서는 & 로 사용
# print(df.loc[cond])
# # print(df.loc[~cond]) # ~ 는 not 의 의미

# from pandas import DataFrame

# data = [
#     ["3R", 1510, 7.36],
#     ["3SOFT", 1790, 1.65],
#     ["ACTS", 1185, 1.28]
# ]

# index = ["037730", "036360", "005760"]
# columns = ["종목명", "현재가", "등락률"]
# df = DataFrame(data=data, index=index, columns=columns)

# # print(df)

# from pandas import Series 

# s = Series(data=[1600, 1600, 1600], index=df.index) # 열을 하나 추가하는 코드
# df['목표가'] = s # 열의 이름이 '목표가' 로 추가됨
# # print(df)

# df["괴리율"] = (df["목표가"] - df["현재가"]) / df['현재가']
# # print(df)

from pandas import DataFrame
import pandas as pd

data = [
    ["3R", 1510, 7.36],
    ["3SOFT", 1790, 1.65],
    ["ACTS", 1185, 1.28]
]

index = ["037730", "036360", "005760"]
columns = ["종목명", "현재가", "등락률"]
df = DataFrame(data=data, index=index, columns=columns)
# print(df)

from pandas import Series 

# s = Series(data=["LG전자", 60000, 3.84], index=df.columns) # 행을 하나더 추가
# df.loc["066570"] = s
# print(df)

# s = Series(data=["LG전자", 60000, 3.84], index=df.columns, name="066570") #name 으로 행이름 지정
# new_df = pd.concat([df, s.to_frame().T]) # to_frame() 으로 DataFrame 으로 변환후 .T 로 전치
# print(new_df)

# new_df = df.drop("현재가", axis=1) # axis=1 은 열(y축)을 의미, axis=0 은 행(x축)을 의미
# print(df)
# print(new_df)

# print(df.columns)
# print(df.index)

# df.columns = ['name', 'close', 'fluctuation']
# df.index.name = 'code'
# print(df)

# df.rename(columns={'종목명': 'code'}, inplace=True) #특정 열의 이름만 바꾸고 싶을때, inplace=True 로 원본에 반영
# print(df)

from pandas import DataFrame

# "" 가 포함된것은 문자열로 지정
data = [
    ["1,000", "1,100", '1,510'],
    ["1,410", "1,420", '1,790'],
    ["850", "900", '1,185'],
]
columns = ["03/02", "03/03", "03/04"]
df = DataFrame(data=data, columns=columns)
# print(df)

def remove_comma(x):
    return int(x.replace(',', '')) # , 를 제거하고 정수형으로 변환

df['03/02'] = df['03/02'].map(remove_comma) # map 함수는 시리즈의 각 원소에 함수를 적용
df['03/03'] = df['03/03'].map(remove_comma)
df['03/04'] = df['03/04'].map(remove_comma)

# print(df)

# df = df.applymap(remove_comma) # applymap 함수는 전체 데이터의 연산 적용 
# dictory 구조로 묶어 데이터 타입변경
# df = df.astype({'03/02': 'int32', '03/03': 'int32', '03/04': 'int32'}) # astype 으로 데이터 타입 변환
# # print(df)
# print(df.dtypes) #각 열의 데이터 타입 확인

# from pandas import DataFrame

# data = [
#     {"cd":"A060310", "nm":"3S", "close":"2,920"},
#     {"cd":"A095570", "nm":"AJ네트웍스", "close":"6,250"},
#     {"cd":"A006840", "nm":"AK홀딩스", "close":"29,700"},
#     {"cd":"A054620", "nm":"APS홀딩스", "close":"19,400"}
# ]
# df = DataFrame(data=data)
# print(df)

# df['cd'] = df['cd'].str[1:] # .str 로 문자열 내부 수정가능(해당코드는 1번째 문자부터 끝까지)
# print(df)

# df['close'] = df['close'].str.replace(',', '') # .str.replace 로 문자열 치환
# df['close'] = df['close'].astype('int64') # astype 으로 데이터 타입 변환
# print(df)

import math
math.sqrt((5-1)**2 -(10-7)**2)
