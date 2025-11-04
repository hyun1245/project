import pandas as pd

df_13 = pd.read_excel('data/20210913.xlsx', index_col=0)
df_14 = pd.read_excel('data/20210914.xlsx', index_col=0)

# print(df_13.head())

# print(df_len(df_13))
# print(df_len(df_14))

df_13 = df_13[df_13['시가'] != 0]
df_14 = df_14[df_14['시가'] != 0]

idx = df_14.index.difference(df_13.index)
# print(idx)
# print(df_14.loc[idx[0], '종목명'])

전일비교시가총액 = df_13['시가총액'].sum()
전일기준시가총액 = df_13['시가총액'].sum()
증감률 = (전일비교시가총액 + df_14.loc[idx[0], '시가총액']) / 전일비교시가총액
당일기준시가총액 = 증감률 * 전일기준시가총액
당일비교시가총액 = df_14['시가총액'].sum()
# print(당일비교시가총액 / 당일기준시가총액)

intersect_idx = df_14.index.intersection(df_13.index)
t_13 = df_13.loc[intersect_idx]
t_14 = df_14.loc[intersect_idx]
cond = t_13['상장주식수'] != t_14['상장주식수']
#False 로 나오면 상장 주식수가 변경된 종목이 존재함 이라는 의미
# print(cond.all()) 

# print(t_14.loc[cond, '상장주식수'] - t_13.loc[cond, '상장주식수'])

주식수증가액 = (t_14.loc[cond, '상장주식수'] - t_13.loc[cond, '상장주식수']) * t_13.loc[cond, '종가']

전일비교시가총액 = df_13['시가총액'].sum()
전일기준시가총액 = df_13['시가총액'].sum()
증감률 = (전일비교시가총액 + df_14.loc[idx[0], '시가총액'] + 주식수증가액.sum()) / 전일비교시가총액
당일기준시가총액 = 증감률 * 전일기준시가총액
당일비교시가총액 = df_14['시가총액'].sum()
# print(당일비교시가총액 / 당일기준시가총액)


import pandas as pd
df = pd.read_excel('data/20210914.xlsx', index_col=0)
df = df[['종목명', '종가', '시가총액']]
# print(df.head())

df = pd.read_excel('data/20210914.xlsx', index_col=0, usecols=[0, 1, 2, 10])
# print(df.head())

df['비중'] = df['시가총액'] / df['시가총액'].sum() * 100
# print(df.sort_values('시가총액', ascending=False).head())


import numpy as np

kospi = pd.read_excel("data/kospi.xlsx")
samsung = pd.read_excel("data/samsung.xlsx")

data = [ kospi['종가'], samsung['종가'] ]
df = pd.concat(data, axis=1, keys=["kospi", "samsung"])
# print(df.head())

df.plot.scatter(x='samsung', y='kospi')

#print(df.corr())

import pandas as pd 

kospi = pd.read_excel("data/kospi.xlsx", index_col=0, parse_dates=True)
# print(kospi.head())

# print(kospi['종가'].max())
# print(kospi['종가'].min())

cond = kospi['종가'] == kospi['종가'].max()
# print(kospi.loc[cond])

# print(kospi['종가'].idxmax()) #가장 높은 날짜
# print(kospi['종가'].idxmin()) #가장 낮은 날짜

kospi = pd.read_excel("data/kospi.xlsx", index_col=0, usecols=[0, 1])
kospi["변동폭"] = kospi["종가"] - kospi["종가"].shift(1)
kospi.sort_values('변동폭').iloc[:5]

# print(kospi["변동폭"].nlargest(n=5)) #바로 위 코드의 결과와 동일 
# print(kospi["변동폭"].nsmallest(n=5))

kospi = pd.read_excel("data/kospi.xlsx", usecols=[0, 1, 4, 5, 6, 7], parse_dates=[0])
how = {
    '시가' : 'first',
    '고가' : max,
    '저가' : min,
    '종가' : 'last',
    '거래량' : sum
}
df = kospi.groupby( pd.Grouper(key='일자', freq='m') ).agg(how)
# print(df.head())


kospi = pd.read_excel("data/kospi.xlsx", usecols=[0, 1], index_col=0, parse_dates=True)
kospi = kospi.sort_index()

threshold = 2300
cond = kospi['종가'] >= threshold
# print(kospi.loc[cond, '종가'].iloc[0])
# print(kospi.loc[cond, '종가'].index[0])

# for threshold in range(2300, 3100, 100):
#     cond = kospi['종가'] >= threshold
#     print(threshold, kospi.loc[cond, '종가'].iloc[0], kospi.loc[cond, '종가'].index[0])

# data = [ ]
# for threshold in range(2300, 3100, 100):
#     cond = kospi['종가'] > threshold
#     data.append( (f'{threshold} 포인트 돌파', kospi.index[cond][0], kospi.loc[cond, '종가'].iloc[0]) )

# df = pd.DataFrame(data, columns=['이벤트', '일자', '지수'])
# print(df)


# import pandas as pd
# kospi = pd.read_excel("data/kospi.xlsx", usecols=[0, 1], index_col=0, parse_dates=True)
# kospi = kospi.sort_index()
# 수익률 = kospi.iloc[-1, 0]/kospi.iloc[0, 0]
# print( (수익률 - 1) * 100 )

# diff = (kospi.index[-1] - kospi.index[0])
# 투자기간 = diff.days / 365
# cagr = 수익률 ** (1/투자기간) -1
# print(cagr * 100)

# ss = pd.read_excel("data/samsung.xlsx", usecols=[0, 1], index_col=0, parse_dates=True)
# ss = ss.sort_index()
# 수익률 = ss.iloc[-1, 0]/ss.iloc[0, 0]
# diff = (ss.index[-1] - ss.index[0])
# 투자기간 = diff.days / 365
# cagr = 수익률 ** (1/투자기간) -1
# print(cagr * 100)

# kospi_return = kospi['종가']/kospi.iloc[0, 0]
# ss_return = ss['종가']/ss.iloc[0, 0]

# df = pd.concat([kospi_return, ss_return], axis=1, keys=["kospi", "samsung"])
# df.index.name = ''
# df.plot(figsize=(12, 5))

import pandas as pd

kospi = pd.read_excel("data/kospi2000.xlsx", index_col=0)
kospi['전고점'] = kospi['Close'].cummax()
kospi['DD'] = (1 - kospi['Close'] / kospi['전고점']) * 100
# print(kospi.head())

MDD = kospi['DD'].max()
# print(MDD)

import matplotlib.pyplot as plt 
    
plt.rc("axes", unicode_minus=False)   # y축 음수처리

fig = plt.figure(figsize=(14, 6))
ax1 = fig.add_subplot(2, 1, 1)
ax2 = fig.add_subplot(2, 1, 2)

ax1.plot(kospi.index, kospi["Close"], label="close")
ax2.plot(kospi.index, kospi["DD"] * -1, label="Drawdown")
ax2.fill_between(kospi.index, kospi["DD"] * -1, alpha=0.1) # 색상채우기

ax1.grid()
ax2.grid()

ax1.legend(loc='best')
ax2.legend(loc='best')
plt.show()