# import pandas as pd

# ts = pd.to_datetime("2021-01-02")
# # print(type(ts))
# # print(ts)

# ts = pd.to_datetime("2021-01-02 09:00:00")
# # print(ts)

# ts = pd.to_datetime("20210102 090000")
# # print(ts)

# # print(pd.to_datetime("06/07/20", format="%d/%m/%y"))

# ts = pd.to_datetime("2021-08-14")
# # print(ts.year) 
# # print(ts.month)
# # print(ts.day)
# # print(ts.hour)
# # print(ts.minute)
# # print(ts.second)

# ts = pd.to_datetime("2021-08-14")
# # print(ts.weekday()) # 5 (Saturday), 파이썬에서는 월요일이 0 부터 시작 

# # print(ts.strftime("%Y-%m-%d"))

# diff = pd.Timedelta(days=100, hours=2, minutes=30, seconds=30 )
# # print(diff)

# # print(ts + diff)

# candidates = [ "2021-01-01", "2021-01-02", "2021-01-03"]
# idx = pd.to_datetime(candidates)
# # print(idx)

# # print(idx[0])
# # print(idx[0:2])

# # print(idx.year)
# # print(idx.month)
# # print(idx.day)

# # day = 1760675165 / 60 / 60 / 24
# # year = day / 365
# # print(year)

# dt = pd.to_datetime(1760675165, unit='s')
# # print(dt)


# data = [
#     {'시가': 100, '고가': 110, '저가': 90, '종가': 105}, 
#     {'시가': 100, '고가': 112, '저가': 80, '종가':  95}, 
#     {'시가':  99, '고가': 115, '저가': 70, '종가':  85}, 
#     {'시가':  70, '고가':  80, '저가': 60, '종가':  75}, 
# ]

# df = pd.DataFrame(data, index=['20200615', '20200616', '20200717', '20200718'])

# cond = df.index.str[:6] == "202006" #.str 속성은 문자열 관련 메서드를 사용할 수 있게 해줌
# # print(cond)
# # print(df.loc[ cond ])

# df.index = pd.to_datetime(df.index)
# # print(df)

# # print(df.loc[ "2020-06" ]) #dataframe에서 날짜 인덱스로 슬라이싱 가능

# df['date'] = df.index
# # print(type(df['date']))
# # print(type(df['date'].iloc[0]))
# # print(df.date)

# import pandas as pd

# # df = pd.read_excel("data.xlsx" , index_col=0)
# # print(df.head(3))

# df.index = pd.to_datetime(df.index)
# df = df.sort_index()
# # print(df)

# df = pd.read_excel("data/ss_ex_1.xlsx" , parse_dates=['일자'])
# df = df.sort_values('일자')
# # print(df)

# # print(df['일자'].dt.quarter)

# df = df[['일자', '시가', '저가', '고가', '종가']].copy()
# df['year'] = df['일자'].dt.year
# df['month'] = df['일자'].dt.month
# # print(df.head())

# gb = df.groupby(['year', 'month'])
# gb.get_group( (2021, 2) ).head( )


# how = {
#     "시가": 'first',
#     "저가": min,
#     "고가": max,
#     "종가": 'last'
# }
# # print(gb.agg(how))

# # print(df.groupby( pd.Grouper(key='일자', freq='m') ).agg(how))

# import pandas as pd
# df = pd.read_excel("data/ss_ex_1.xlsx" , index_col=0)
# df.index = pd.to_datetime(df.index)
# df = df.sort_index()

# # print(df["거래량"].shift(1))

# df["전일거래량"] = df["거래량"].shift(1)
# # print(df[ ['거래량', '전일거래량'] ])

# df["전일거래량"] = df["거래량"].shift(1)
# cond = df["거래량"] > df["전일거래량"]
# # print(df[cond])

# # print("상승일:", len(df[cond]))
# # print("영업일:", len(df))

# # print(df['거래량'].diff( ))

# cond = df['거래량'].diff() > 0
# # print(len(df[cond]))

# yeild = df['종가'] / df['종가'].shift(6)
# cond = yeild >= 1.03 
# # print(len(df[cond]))

# # print(cond.shift(1))

# cond_modified = cond.shift(1).fillna(False)
# s = df.loc[cond_modified, '종가'] / df.loc[cond_modified, '시가']
# # print(s.cumprod().iloc[-1])

# import pandas as pd

# df = pd.read_excel("data/ss_ex_1.xlsx", index_col=0)
# df.index = pd.to_datetime(df.index)
# df = df.sort_index()[["종가"]]

# df['종가D-1'] = df['종가'].shift(1)
# df['종가D-2'] = df['종가'].shift(2)
# df['ma3'] = (df['종가'] + df['종가D-1'] + df['종가D-2']) / 3
# # print(df.head())

# df['rolling3'] = df['종가'].rolling(3).mean()
# # print(df.head()) 

# df = pd.read_excel("data/ss_ex_1.xlsx", index_col=0)
# df.index = pd.to_datetime(df.index)

# df['ma5'] = df['종가'].rolling(5).mean().shift(1)

# cond = df['ma5'] < df['시가']
# # print("상승일:", len(df[cond]))
# # print("영업일:", len(df))

# from pandas import Series

# data  = [84200, 84900, 83200, 82100, 82600]
# index = ["2021-02-15", "2021-02-16", "2021-02-17", "2021-02-18", "2021-02-19"]

# s = Series(data, index)
# # print(s.ewm(span=3, adjust=False).mean())

# import pandas as pd

# df = pd.read_excel("data/ss_ex_1.xlsx", index_col=0)
# df.index = pd.to_datetime(df.index)
# df = df.sort_index()[['시가', '저가', '고가', '종가', '거래량']]
# # print(df.head())

# # df.resample('M').first() # 월별 첫 거래일(월말 기준)
# # df.resample('MS').first() # 월별 첫 거래일(월초 기준)
# # resample 메서드는 월(M), 시(H), 분(T), 초(S), 일(D) 등 다양한 빈도를 지원

# how = {
#    "시가": "first",
#    "종가": "last",
#    "고가": max,
#    "저가": min,
#    "거래량": sum,
# }

# # print(df.resample('MS').apply(how))

# # print(df.resample('3D').apply(how).head())#3일단위로 resampling(결측치는 휴장일 때문)

# temp = df.resample('3D').apply(how)
# # temp.index = temp.index + pd.to_timedelta("2D")
# print(temp.dropna().head())

# print(df.resample('3D', offset='1D').apply(how)) 

import pandas as pd

data = {'삼성전자': [52200, 52300, 52900, 52000, 51700], 
           'LG전자': [68200, 67800, 68800, 67500, 66300]}
df = pd.DataFrame(data=data)
# print(df.pct_change())

# print(df / df.shift(2) - 1)

# print(df.shift(1))
# print(df.shift(2))

# print(df.pct_change(periods=2)) # [df / df.shift(2) - 1]와 동일

# yeild = df.pct_change(periods=2) + 1
# print(yeild.cumprod())

df = pd.read_excel("data/ss_ex_1.xlsx", index_col=0, usecols=[0, 1, 4])
df.index = pd.to_datetime(df.index)
df = df.sort_index()
print(df.head())

# 'q' : 데이터를 분기 말일 기준으로 그룹화
df_quarter = df['시가'].resample('q').first().to_frame() 
# print(df_quarter)

# print(df['시가'].groupby(pd.Grouper(freq='q')).first().to_frame())

df_quarter['quarter'] = df_quarter.index.quarter # 분기 정보 추가
df['quarter'] = df.index.quarter
# print(df.head())
# print(df_quarter)

df_daily = df[['종가', 'quarter']].reset_index()
r = pd.merge(left=df_daily, right=df_quarter, on='quarter')
# print(r)

r['수익률'] = r['종가'] / r['시가']
r = r.set_index(['quarter', '일자']) #quarter 별로 그룹화됨 
# print(r)


