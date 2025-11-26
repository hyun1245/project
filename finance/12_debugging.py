import pandas as pd 

df_factor = pd.read_excel(
    "data/data_kosdaq_20210401_per.xlsx",
    index_col = 0,
    usecols = [0,1,6,8] # 종목코드, 종목명, PER, PBR
)
# print(df_factor.head())

# print(df_factor.info()) # 데이터 프레임 정보 확인

import numpy as np

df_factor.replace('-', np.nan, inplace = True) # '-' 값을 NaN으로 변환
# print(df_factor.head())

# print(df_factor.info()) # 데이터 프레임 정보 확인

import pandas as pd
df = pd.read_excel("data/data_kosdaq_20210401_sise.xlsx", index_col=0)
df_volume = df[['거래량']]
# print(df_volume.shape)
# print(df_volume.head())

df2 = df_factor.join(df_volume)
# print(df2.head())
# print(df2.shape)

import pandas as pd

df_change = pd.read_excel("data/data_kosdaq_change_2021.xlsx", index_col=0, usecols=[0,5])
# print(df_change.head())

# print(df_change.info())

df3 = df2.join(df_change)
# print(df3.head())
# print(df3.shape)

cond = df3['거래량'] !=0
df4 = df3[cond].copy()
# print(df4.shape)

df5 = df4.sort_values(by="PER", ascending=True)
df5.reset_index(inplace = True)
# print(df5)

low_per30 = df5.iloc[:30]
# print(low_per30['등락률'].mean())

import pandas as pd
df5['group'] = pd.cut(df5.index, bins = 20, labels = False)
# print(df5.head())

df6 = df5.groupby(by = "group")[['등락률']].mean()
# print(df6)

import matplotlib.pyplot as plt
import platform

if platform.system() == 'Darwin' : 
    plt.rc('font', family = 'AppleGothic')
else :
    plt.rc('font', family = 'Malgun Gothic')

fig = plt.figure(figsize = (12,8))
ax = fig.add_subplot(1,1,1)

ax.bar(df6.index, df6['등락률'], width = 0.5)
plt.title("PER 그룹별 수익률")
plt.xlabel("PER 그룹")
plt.ylabel("수익률")
# plt.show()

# print(df4)

cond = (df4['PER'] >= 2.5) & (df4['PER'] <= 10)
df5 = df4[cond].copy()
# print(df5)

df6 = df5.sort_values(by = 'PER')[:30]
# print(df6.describe())

# print(df6[df6['등락률'] == df6['등락률'].min()])

from pykrx import stock
import pandas as pd

df1 = stock.get_market_cap_by_ticker("20100104")
df1 = df1[["종가", "시가총액"]]
df1.columns = ["시가", "시가총액"]
df1 = df1.sort_values("시가총액")
df1["group"] = pd.cut(df1.reset_index().index, bins = 3, labels = ['소형주', '중형주', '대형주'])
# print(df1.head())
# print(df1.tail())

df2 = stock.get_market_fundamental_by_ticker("20100104")
df2 = df2[["PER", "PBR"]]
# print(df2.head())

df3 = stock.get_market_ohlcv_by_ticker("20101231", alternative=True)
df3 = df3[['종가']]
# print(df3.head())

t0 = pd.merge(left = df1, right = df2, left_index = True, right_index = True)
df = pd.merge(left = t0, right = df3, left_index = True, right_index = True)
# print(t0.head())
# print(df.head())

df = df.query('PER ! = 0')
df['수익률'] = df['종가'] / df['시가']
cond = (df['PER'] >= 2.5) & (df['PER'] <= 10)
top30 = df[cond].sort_values('PBR').groupby('group').head(30)
print(top30.head())

import numpy as np

how = {
    '수익률' : np.mean
}
yoy = top30.groupby('group').agg(how)
yoy.columns = ['2010']
# print(yoy)

def low_per_pbr(year):
    # 2010년도의 1월1일은 휴장일이기 때문에 휴장일이 아닌 날짜로 수정
    df1 = stock.get_market_cap_by_ticker(f"{year}0107")
    df1 = df1[["종가", "시가총액"]]
    df1.columns = ["시가", "시가총액"]
    df1 = df1.sort_values("시가총액")
    df1["group"] = pd.cut(df1.reset_index().index, bins = 3, labels = ['소형주', '중형주', '대형주'])

    print(df1.head())

    df2 = stock.get_market_fundamental_by_ticker(f"{year}0107")
    df2 = df2[["PER", "PBR"]]

    print(df2.head())

    # 각 df1, df2 에 출력해보았을때 시가, 시가총액, per, pbr 컬럼이 전부 0으로 표기됨
    # 이는 해당 날짜가 휴장일 이기때문에 출력이 안되는것으로 보임 
    # 따라서 휴장일이 아닌 날짜로 수정
    df3 = stock.get_market_ohlcv_by_ticker(f"{year}1230", alternative=True)

    print(df3.head())

    t0 = pd.merge(left = df1, right = df2, left_index = True, right_index = True)
    df = pd.merge(left = t0 , right = df3, left_index = True, right_index = True)

    print(df.head())

    df = df.query('PER ! = 0').copy()
    # merge 함수의 기능 떄문에 공통된 '시가' 라는 컬럼이 합쳐지면서 이름이 수정됨
    # 이름을 확인 후 수정
    df.rename(columns={'시가_x':'시가'}, inplace=True)

    df['수익률'] = df['종가'] / df['시가']
    cond = (df['PER'] >= 2.5) & (df['PER'] <= 10)
    top30 = df[cond].sort_values('PBR').groupby('group').head(30)

    how = {
        '수익률' : np.mean
    }                     
    yoy = top30.groupby('group').agg(how)
    yoy.columns = [year] 
    return yoy

import time 

dfs = [ ]
for date in range(2010, 2021):
    df = low_per_pbr(f"{date}")
    dfs.append(df)
    time.sleep(1)

df = pd.concat(dfs, axis = 1)
# print(df)

# print(df.cumprod(axis=1))

# df.cumprod(axis=1).transpose().plot.line()