# # from pandas import DataFrame

# # data = [
# #     {"cd":"A060310", "nm":"3S", "open":2920, "close":2800},
# #     {"cd":"A095570", "nm":"AJ네트웍스", "open":1920, "close":1900},
# #     {"cd":"A006840", "nm":"AK홀딩스", "open":2020, "close":2010},
# #     {"cd":"A054620", "nm":"APS홀딩스", "open":3120, "close":3200}
# # ]
# # df = DataFrame(data=data)
# # df = df.set_index('cd')
# # # print(df)

# # cond = df['open'] >= 2000
# # print(df[cond])

# # # qurey 메서드는 해당 조건에 맞는 행을 반환
# # print(df.query("nm == '3S'")) # 조건을 주려면 그 대상에 작은 따옴표(')를 사용해야함

# # print(df.query("open > close"))

# # print(df.query("nm in ['3S', 'AK홀딩스']"))

# # print(df.query("cd == 'A060310'"))

# # name = "AJ네트웍스"
# # print(df.query('nm == @name')) # @ 를 사용해서 외부 변수를 사용할 수 있음


# # from pandas import DataFrame

# # data = [
# #     [1416, 1416, 2994, 1755],
# #     [6.42, 17.63, 21.09, 13.93],
# #     [1.10, 1.49, 2.06, 1.88]
# # ]

# # columns = ["2018/12", "2019/12", "2020/12", "2021/12(E)"]
# # index = ["DPS", "PER", "PBR"]

# # df = DataFrame(data=data, index=index, columns=columns)
# # print(df)

# # print(df.filter(items=["2018/12"]))

# # print(df.filter(items=["PER"], axis=0)) # axis=0 은 행(x축)을 의미, axis=1 은 열(y축)을 의미

# # print(df.filter(regex="2020")) # 정규식을 사용해서 2020 이 포함된 열을 찾고 싶을 때

# # print(df.filter(regex="R$", axis=0)) # 'r'로 끝나는 모든 행을 찾고 싶을 때

# # print(df.filter(regex="\d{4}")) # 4자리 숫자가 포함된 모든 열을 찾고 싶을 때

# # print(df.filter(regex="\d{4}/\d{2}$")) # '4자리 숫자/2자리 숫자'로 끝나는 모든 열을 찾고 싶을 때

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

# # print(df.sort_values("현재가")) # 오름차순 정렬
# # print(df.sort_values(by="현재가")) # by 파라미터를 사용해도 동일한 함수
# # print(df.sort_values("현재가", ascending=False)) # 내림차순 정렬

# print(df['현재가'].rank()) # rank() 함수로 순위 출력
# df['순위'] = df['현재가'].rank() # rank() 함수로 순위 열 추가
# print(df)

# import pandas as pd

# idx1 = pd.Index([1, 2, 3])
# idx2 = pd.Index([2, 3, 4])

# # print(idx1)
# # print(type(idx1)) #type 함수로 객체의 타입 확인

# print(idx1.union(idx2)) # 합집합
# print(idx1.intersection(idx2)) # 교집합 
# print(idx1.difference(idx2)) # 차집합

from pandas import DataFrame

data = [
    ["2차전지(생산)", "SK이노베이션", 10.19, 1.29],
    ["해운", "팬오션", 21.23, 0.95],
    ["시스템반도체", "티엘아이", 35.97, 1.12],
    ["해운", "HMM", 21.52, 3.20],
    ["시스템반도체", "아이에이", 37.32, 3.55],
    ["2차전지(생산)", "LG화학", 83.06, 3.75]
]

columns = ["테마", "종목명", "PER", "PBR"]
df = DataFrame(data=data, columns=columns)
# print(df)

# df1 = df[df["테마"] == "2차전지(생산)"] #2차전지(생산) 테마만 선택
# print(df1)
# df2 = df[df["테마"] == "해운"] #해운 테마만 선택
# print(df2)
# df3 = df[df["테마"] == "시스템반도체"] #시스템반도체 테마만 선택

# mean1 = df1["PER"].mean() #df1의 PER의 평균
# print("2차전지(생산) PER 평균:", mean1)
# mean2 = df2["PER"].mean()
# print("해운 PER 평균:", mean2)
# mean3 = df3["PER"].mean()
# print("시스템반도체 PER 평균:", mean3)

# import pandas as pd 

# data = [mean1, mean2, mean3]
# index = ["2차전지(생산)", "해운", "시스템반도체"]
# s = pd.Series(data=data, index=index)
# print(s)

# print(df.groupby("테마")) # groupby 객체 출력
# print(df.groupby("테마").get_group("2차전지(생산)"))# groupby는 컬럼 명이 들어감 

# #데이터 프레임에서 '테마', 'PER', 'PBR' 열만 선택한 후, '테마'로 그룹화하여 '2차전지(생산)' 그룹을 가져오기
# temp = df[["테마", "PER", "PBR"]].groupby("테마").get_group("2차전지(생산)")
# print(temp)


# temp = df.groupby("테마")[ ["PER", "PBR"] ].get_group("2차전지(생산)")
# # print(temp)

# print(df.groupby("테마")["PER"].mean())
# print(df.groupby("테마")[["PER", "PBR"]].mean())
# # .agg는 groupby 와 함께 사용하는 집계함수로 per,pbr 의 최대와 최소를 구할 수 있음
# print(df.groupby("테마").agg({"PER": "max", "PBR": "min"}))

import numpy as np

# PER에는 최소값과 최대값을, PBR에는 표준편차와 분산을 구함
# df.groupby("테마").agg({"PER": ["min", "max"], "PBR": ['std', 'var']})

from pandas import DataFrame
import pandas as pd

data = {
    '종가': [113000, 111500],
    '거래량': [555850, 282163]
}

index = ["2019-06-21", "2019-06-20"]
df1 = DataFrame(data=data, index=index)
# print(df1)

data = {
    '시가': [112500, 110000],
    '고가': [115000, 112000],
    '저가': [111500, 109000]
}
df2 = DataFrame(data=data, index=index)
# print(df2)

# df = pd.concat([df1, df2], axis=1)
# # print(df)

# 정렬순서 = ['시가', '고가', '저가', '종가', '거래량']
# df = df[정렬순서]
# # print(df)

# df = pd.concat([df1, df2], axis=1, join='inner') #inner = 교집합
# print("inner = ",df)

# df = pd.concat([df1, df2], axis=1, join='outer') #outer = 합집합, 기본값은 outer 로 되어있음
# print("outer =",df)

# df = df1.append(df2) # 업데이트후 제거됨
# print(df)

# df = pd.concat([df1, df2]) # default axis=0
# print(df)

# from pandas import DataFrame
# import pandas as pd

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

# print(pd.merge(left=df1, right=df2, on='업종')) #업종을 기준으로 결합, 기본값은 inner(교집합)

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
# print(df1)

# # 두 번째 데이터프레임
# data = [
#     ["은행", 2.92],
#     ["보험", 0.37],
#     ["화학", 0.06],
#     ["전기전자", -2.43]
# ]

# columns = ["업종", "등락률"]
# df2 = DataFrame(data=data, columns=columns)
# print(df2)

# df = pd.merge(left=df1, right=df2, how='left', on='업종')
# print(df)

# df1 = pd.merge(left=df1, right=df2, how='right', on='업종')
# print(df1)

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

# 첫 번째 데이터프레임
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
# print(df2)

# print(df1.join(other=df2)) # 업종과 항목이 같은 행끼리 결합

# data = [
#     ["2017", "삼성", 500],
#     ["2017", "LG", 300],    
#     ["2017", "SK하이닉스", 200],
#     ["2018", "삼성", 600],
#     ["2018", "LG", 400],
#     ["2018", "SK하이닉스", 300],    
# ]

# columns = ["연도", "회사", "시가총액"]
# df = DataFrame(data=data, columns=columns)
# # print(df)

# df_mean = df.groupby("연도")["시가총액"].mean().to_frame() #연도별로 그룹화해서 시가총액의 평균을 데이터 프레임으로 바꾼다
# df_mean.columns = ['시가총액평균']
# # print(df_mean)

# df = df.join(df_mean, on='연도')
# print(df)

# import numpy as np

# # np.where(조건, 참, 거짓), 조건에 부합하면 참 아니면 거짓
# df['규모'] = np.where(df['시가총액'] >= df['시가총액평균'], "대형주", "중/소형주") 
# print(df)

from pandas import DataFrame
import pandas as pd

data = [
    ["영업이익", "컨센서스", 1000, 1200],
    ["영업이익", "잠정치", 900, 1400],
    ["당기순이익", "컨센서스", 800, 900],
    ["당기순이익", "잠정치", 700, 800]
]

df = DataFrame(data=data)
df = df.set_index([0, 1])
print(df)

df.index.names = ["재무연월", ""]
df.columns = ["2020/06", "2020/09"]
print(df)

# # print(df.loc["영업이익"])

# # print(df.loc[ ("영업이익", "컨센서스") ])

# # print(df.iloc[0])

# # print(df.loc[("영업이익", "컨센서스"), "2020/06"])

# # print(df.loc[(slice(None), "컨센서스"),:])

a = [1, 2, 3, 4, 5]

print(a[0:5:2])
print(a[slice(0, 5, 2)])

# a = [1, 2, 3, 4, 5]
# b = [3, 4, 5, 6, 7]

# s = slice(0, 5, 2)
# # print(a[ s ])
# # print(b[ s ])


# a = [1, 2, 3, 4, 5]

# # print(a[:])
# # print(a[slice(None)])
# # print(a[ : : ])
# # print(a[slice(None, None)])

# # print(df.loc[ (slice(None), '컨센서스'), :])

# idx = pd.IndexSlice
# # print(df.loc[idx[:, "컨센서스"], :])

# from pandas import DataFrame

# data = [
#     [100, 900, 800, 700],
#     [1200, 1400, 900, 800]
# ]

# columns = [
#     ['영업이익', '영업이익', '당기순이익', '당기순이익'],
#     ['컨센서스', '잠정치', '컨센서스', '잠정치']
# ]

# index = ["2020/06", "2020/09"]

# df = DataFrame(data=data, index=index, columns=columns)
# # print(df)

# import pandas as pd

# level_0 = ["영업이익", "당기순이익"]
# level_1 = ["컨센서스", "잠정치"]

# idx = pd.MultiIndex.from_product([level_0, level_1])
# # print(idx)

# from pandas import DataFrame

# data = [
#     [100, 900, 800, 700],
#     [1200, 1400, 900, 800]
# ]

# columns = [
#     ['영업이익', '영업이익', '당기순이익', '당기순이익'],
#     ['컨센서스', '잠정치', '컨센서스', '잠정치']
# ]

# index = ["2020/06", "2020/09"]

# df = DataFrame(data=data, index=index, columns=columns)
# # print(df)

# # print(df.stack()) 

# # print(df.stack(level=0)) # stack 을 하면 할수록 행이 늘어남

# # print(df.stack().stack())

# # print(df.stack().unstack()


data = [
    [1000, 1100, 900, 1200, 1300],
    [800, 2000, 1700, 1500, 1800]
]
index = ['자본금', '부채']
columns = ["2020/03", "2020/06", "2020/09", "2021/03", "2021/06"]
df = DataFrame(data, index, columns)
# print(df)

df_stacked = df.stack().reset_index()
print(df_stacked)

# # print(df_stacked['level_1'].str.split('/')) # 문자열을 '/' 기준으로 나눔

# df_split = DataFrame( list(df_stacked['level_1'].str.split('/')) )
# # print(df_split)

# df_merged = pd.concat( [df_stacked, df_split], axis=1 )
# df_merged.columns = ['계정', "년월", "금액", "연도", "월"]
# # print(df_merged)

# df_group = df_merged.groupby(["계정", "연도"]).sum()
# # print(df_group)

# df_unstack = df_group.unstack()
# # print(df_unstack)


# from pandas import DataFrame
# import pandas as pd

# data = [
#     ["2021-08-12", "삼성전자", 77000],
#     ["2021-08-13", "삼성전자", 74400],
#     ["2021-08-12", "LG전자", 153000],
#     ["2021-08-13", "LG전자", 150500],
#     ["2021-08-12", "SK하이닉스", 100500],
#     ["2021-08-13", "SK하이닉스", 101500]
# ]
# columns = ["날짜", "종목명", "종가"]
# df = DataFrame(data=data, columns=columns)
# # print(df)

# # print(pd.pivot(data=df, index="날짜", columns="종목명", values="종가"))

# # print(df.groupby(["날짜", "종목명"]).mean().unstack())

# # print(pd.pivot(data=df, index="종목명", columns="날짜", values="종가"))


# from pandas import DataFrame

# data = [
#     ["005930", "삼성전자", 75800, 76000, 74100, 74400],
#     ["035720", "카카오", 147500, 147500, 144500, 146000],
#     ["000660", "SK하이닉스", 99600, 101500, 98900, 101500]
# ]

# columns = ["종목코드", "종목명", "시가", "고가", "저가", "종가"]
# df = DataFrame(data=data, columns=columns)
# # print(df)



# from pandas import DataFrame

# data = [
#     ["3R", 1510, 7.36],
#     ["3SOFT", 1790, 1.65],
#     ["ACTS", 1185, 1.28]
# ]

# index = ["037730", "036360", "005760"]
# columns = ["종목명", "현재가", "등락률"]
# df = DataFrame(data=data, index=index, columns=columns)
# df.index.name = '종목코드'
# # print(df)

# # print(df.to_csv("data.csv")) # csv 파일로 저장
# # print(df.to_excel("data.xlsx")) # 엑셀 파일로 저장



# from pandas import DataFrame

# data = {
#     "종목명": ["3R", "3SOFT", "ACTS"],
#     "현재가": [1510, 1790, 1185],
#     "등락률": [7.36, 1.65, 1.28],
# }

# df = DataFrame(data, index=["037730", "036360", "005760"])
# print(df)

# #참고 -> NOSQL -> ** Hadoop ** 
