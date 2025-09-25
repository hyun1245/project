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

from pandas import DataFrame

data = [
    ["3R", 1510, 7.36],
    ["3SOFT", 1790, 1.65],
    ["ACTS", 1185, 1.28]
]

index = ["037730", "036360", "005760"]
columns = ["종목명", "현재가", "등락률"]
df = DataFrame(data=data, index=index, columns=columns)

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