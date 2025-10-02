# from pandas import DataFrame

# data = [
#     {"cd":"A060310", "nm":"3S", "open":2920, "close":2800},
#     {"cd":"A095570", "nm":"AJ네트웍스", "open":1920, "close":1900},
#     {"cd":"A006840", "nm":"AK홀딩스", "open":2020, "close":2010},
#     {"cd":"A054620", "nm":"APS홀딩스", "open":3120, "close":3200}
# ]
# df = DataFrame(data=data)
# df = df.set_index('cd')
# # print(df)

# cond = df['open'] >= 2000
# print(df[cond])

# # qurey 메서드는 해당 조건에 맞는 행을 반환
# print(df.query("nm == '3S'")) # 조건을 주려면 그 대상에 작은 따옴표(')를 사용해야함

# print(df.query("open > close"))

# print(df.query("nm in ['3S', 'AK홀딩스']"))

# print(df.query("cd == 'A060310'"))

# name = "AJ네트웍스"
# print(df.query('nm == @name')) # @ 를 사용해서 외부 변수를 사용할 수 있음


# from pandas import DataFrame

# data = [
#     [1416, 1416, 2994, 1755],
#     [6.42, 17.63, 21.09, 13.93],
#     [1.10, 1.49, 2.06, 1.88]
# ]

# columns = ["2018/12", "2019/12", "2020/12", "2021/12(E)"]
# index = ["DPS", "PER", "PBR"]

# df = DataFrame(data=data, index=index, columns=columns)
# print(df)

# print(df.filter(items=["2018/12"]))

# print(df.filter(items=["PER"], axis=0)) # axis=0 은 행(x축)을 의미, axis=1 은 열(y축)을 의미

# print(df.filter(regex="2020")) # 정규식을 사용해서 2020 이 포함된 열을 찾고 싶을 때

# print(df.filter(regex="R$", axis=0)) # 'r'로 끝나는 모든 행을 찾고 싶을 때

# print(df.filter(regex="\d{4}")) # 4자리 숫자가 포함된 모든 열을 찾고 싶을 때

# print(df.filter(regex="\d{4}/\d{2}$")) # '4자리 숫자/2자리 숫자'로 끝나는 모든 열을 찾고 싶을 때

# from pandas import DataFrame

# data = [
#     ["037730", "3R", 1510],
#     ["036360", "3SOFT", 1790],
#     ["005670", "ACTS", 1185]
# ]

# columns = ["종목코드", "종목명", "현재가"]
# df = DataFrame(data=data, columns=columns)
# df.set_index("종목코드", inplace=True)
# print(df)

# print(df.sort_values("현재가")) # 오름차순 정렬
# print(df.sort_values(by="현재가")) # by 파라미터를 사용해도 동일한 함수
# print(df.sort_values("현재가", ascending=False)) # 내림차순 정렬

# print(df['현재가'].rank()) # rank() 함수로 순위 출력
# df['순위'] = df['현재가'].rank() # rank() 함수로 순위 열 추가
# import pandas as pd

# idx1 = pd.Index([1, 2, 3])
# idx2 = pd.Index([2, 3, 4])

# print(type(idx1))

# print(idx1.union(idx2)) # 합집합
# print(idx1.intersection(idx2)) # 교집합 
# print(idx1.difference(idx2)) # 차집합

# from pandas import DataFrame

# data = [
#     ["2차전지(생산)", "SK이노베이션", 10.19, 1.29],
#     ["해운", "팬오션", 21.23, 0.95],
#     ["시스템반도체", "티엘아이", 35.97, 1.12],
#     ["해운", "HMM", 21.52, 3.20],
#     ["시스템반도체", "아이에이", 37.32, 3.55],
#     ["2차전지(생산)", "LG화학", 83.06, 3.75]
# ]

# columns = ["테마", "종목명", "PER", "PBR"]
# df = DataFrame(data=data, columns=columns)
# print(df)

# df1 = df[df["테마"] == "2차전지(생산)"]
# print(df1)
# # df2 = df[df["테마"] == "해운"]
# # df3 = df[df["테마"] == "시스템반도체"]

# mean1 = df1["PER"].mean() #df1의 PER의 평균
# mean2 = df2["PER"].mean()
# mean3 = df3["PER"].mean()

# import pandas as pd 

# data = [mean1, mean2, mean3]
# index = ["2차전지(생산)", "해운", "시스템반도체"]
# s = pd.Series(data=data, index=index)
# # print(s)

# df.groupby("테마").get_group("2차전지(생산)") # groupby는 컬럼 명이 들어감 

# temp = df[["테마", "PER", "PBR"]].groupby("테마").get_group("2차전지(생산)")
# # print(temp)

# temp = df.groupby("테마")[ ["PER", "PBR"] ].get_group("2차전지(생산)")
# # print(temp)

# df.groupby("테마")["PER"].mean()
# df.groupby("테마")[["PER", "PBR"]].mean()
# df.groupby("테마").agg({"PER": max, "PBR": min})

# import numpy as np

# df.groupby("테마").agg({"PER": [min, max], "PBR": [np.std, np.var]})

from pandas import DataFrame
import pandas as pd

# data = {
#     '종가': [113000, 111500],
#     '거래량': [555850, 282163]
# }

# index = ["2019-06-21", "2019-06-20"]
# df1 = DataFrame(data=data, index=index)
# # print(df1)

# data = {
#     '시가': [112500, 110000],
#     '고가': [115000, 112000],
#     '저가': [111500, 109000]
# }
# df2 = DataFrame(data=data, index=index)
# # print(df2)

# df = pd.concat([df1, df2], axis=1)
# # print(df)

# 정렬순서 = ['시가', '고가', '저가', '종가', '거래량']
# df = df[정렬순서]
# print(df)

# data = {
#     '종가': [113000, 111500],
#     '거래량': [555850, 282163]
# }

# index = ["2019-06-21", "2019-06-20"]
# df1 = DataFrame(data=data, index=index)
# # print(df1)

# data = {
#     '시가': [112500, 110000],
#     '고가': [115000, 112000],
#     '저가': [111500, 109000]
# }

# index = ["2019-06-20", "2019-06-19"]
# df2 = DataFrame(data=data, index=index)
# # print(df2)

# df = pd.concat([df1, df2], axis=1)
# # print(df)

# df = pd.concat([df1, df2], axis=1, join='inner') #inner = 교집합
# print("inner = ",df)

# df = pd.concat([df1, df2], axis=1, join='outer') #outer = 합집합, 기본값은 outer 로 되어있음
# print("outer =",df)

# from pandas import DataFrame
# import pandas as pd

# # 첫번째 데이터프레임
# data = {
#     '종가': [113000, 111500],
#     '거래량': [555850, 282163]
# }
# index = ["2019-06-21", "2019-06-20"]
# df1 = DataFrame(data, index=index)

# # 두번째 데이터프레임
# data = {
#     '종가': [110000, 483689],
#     '거래량': [109000, 791946]
# }
# index = ["2019-06-19", "2019-06-18"]
# df2 = DataFrame(data, index=index)

# # df = df1.append(df2)
# # print(df)

# df = pd.concat([df1, df2])
# print(df)

from pandas import DataFrame
import pandas as pd

# # 첫 번째 데이터프레임
# data = [
#     ["전기전자", "005930", "삼성전자", 74400],
#     ["화학", "051910", "LG화학", 896000],
#     ["전기전자", "000660", "SK하이닉스", 101500]
# ]

# columns = ["업종", "종목코드", "종목명", "현재가"]
# df1 = DataFrame(data=data, columns=columns)

# # 두 번째 데이터프레임
# data = [
#     ["은행", 2.92],
#     ["보험", 0.37],
#     ["화학", 0.06],
#     ["전기전자", -2.43]
# ]

# columns = ["업종", "등락률"]
# df2 = DataFrame(data=data, columns=columns)

# # print(pd.merge(left=df1, right=df2, on='업종'))

# print(pd.merge(left=df1, right=df2, how='inner', on='업종')) # 교집합
# print(pd.merge(left=df1, right=df2, how='outer', on='업종')) # 합집합

# from pandas import DataFrame
# import pandas as pd

# # 첫 번째 데이터프레임
# data = [
#     ["전기전자", "005930", "삼성전자", 74400],
#     ["화학", "051910", "LG화학", 896000],
#     ["서비스업", "035720", "카카오", 121500]
# ]

# columns = ["업종", "종목코드", "종목명", "현재가"]
# df1 = DataFrame(data=data, columns=columns)

# # 두 번째 데이터프레임
# data = [
#     ["은행", 2.92],
#     ["보험", 0.37],
#     ["화학", 0.06],
#     ["전기전자", -2.43]
# ]

# columns = ["업종", "등락률"]
# df2 = DataFrame(data=data, columns=columns)

# df = pd.merge(left=df1, right=df2, how='left', on='업종')
# df

# df = pd.merge(left=df1, right=df2, how='right', on='업종')
# df

# 첫 번째 데이터프레임
# data = [
#     ["전기전자", "005930", "삼성전자", 74400],
#     ["화학", "051910", "LG화학", 896000],
#     ["서비스업", "035720", "카카오", 121500]
# ]

# columns = ["업종", "종목코드", "종목명", "현재가"]
# df1 = DataFrame(data=data, columns=columns)

# # 두 번째 데이터프레임
# data = [
#     ["은행", 2.92],
#     ["보험", 0.37],
#     ["화학", 0.06],
#     ["전기전자", -2.43]
# ]

# columns = ["항목", "등락률"]
# df2 = DataFrame(data=data, columns=columns)

# df = pd.merge(left=df1, right=df2, left_on='업종', right_on='항목')
# print(df)

# # 첫 번째 데이터프레임
# data = [
#     ["전기전자", "005930", "삼성전자", 74400],
#     ["화학", "051910", "LG화학", 896000],
#     ["서비스업", "035720", "카카오", 121500]
# ]

# columns = ["업종", "종목코드", "종목명", "현재가"]
# df1 = DataFrame(data=data, columns=columns)
# df1 = df1.set_index("업종")

# # 두 번째 데이터프레임
# data = [
#     ["은행", 2.92],
#     ["보험", 0.37],
#     ["화학", 0.06],
#     ["전기전자", -2.43]
# ]

# columns = ["항목", "등락률"]
# df2 = DataFrame(data=data, columns=columns)
# df2 = df2.set_index("항목")

# print(df1.join(other=df2)) # 업종과 항목이 같은 행끼리 결합

data = [
    ["2017", "삼성", 500],
    ["2017", "LG", 300],    
    ["2017", "SK하이닉스", 200],
    ["2018", "삼성", 600],
    ["2018", "LG", 400],
    ["2018", "SK하이닉스", 300],    
]

columns = ["연도", "회사", "시가총액"]
df = DataFrame(data=data, columns=columns)
# print(df)

df_mean = df.groupby("연도")["시가총액"].mean().to_frame()
df_mean.columns = ['시가총액평균']
# print(df_mean)

df = df.join(df_mean, on='연도')
# print(df)

import numpy as np

# np.where(조건, 참, 거짓), 조건에 부합하면 참 아니면 거짓
df['규모'] = np.where(df['시가총액'] >= df['시가총액평균'], "대형주", "중/소형주") 
print(df)
