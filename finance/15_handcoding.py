# from pykrx import stock

# df = stock.get_market_ohlcv_by_date("20000101", "20191231", "005930")
# df = df[['종가']]
# print(df.head())

# df['변화량'] = df['종가'] - df['종가'].shift(1)
# df.loc[df['변화량'] >= 0 , '상승폭'] = df['변화량']
# df.loc[df['변화량'] < 0 , '하락폭'] = -df['변화량']
# df = df.fillna(0)
# print(df.head())

# df['AU'] = df['상승폭'].rolling(14).mead() # 14일 동안의 상승폭 평균
# df['DU'] = df['하락폭'].rolling(14).mean() # 14일 동안의 하락폭 평균
# df['RSI'] = df['AU'] / (df['AU'] + df['DU']) * 100
# print(df.iloc[12:].head())

# df['AU'] = df['상승폭'].ewm(span = 14, adjust = False).mean() # 14일 지수이동평균 계산
# df['DU'] = df['하락폭'].ewm(span = 14, adjust = False).mean()
# df['RSI'] = df['AU'] / (df['AU'] + df['DU']) * 100
# print(df.iloc[12:].head())

# df['AU'] = df['상승폭'].rolling(14).mean()
# df['DU'] = df['하락폭'].rolling(14).mean()
# df['RSI-SMA'] = df['AU'] / (df['AU'] + df['DU']) * 100

# df['AU'] = df['상승폭'].ewm(span = 14, adjust = False).mean()
# df['DU'] = df['하락폭'].ewm(span = 14, adjust = False).mean()
# df['RSI-EMA'] = df['AU'] / (df['AU'] + df['DU']) * 100

# df[['RSI-SMA', 'RSI-EMA']].iloc[20:300].plot(figsize = (8,4))

# # RSI 전량 백테스팅
# from pykrx import stock
# import numpy as np

# df = stock.get_market_ohlcv_by_date("20000101", "20191231", "005930")
# df = df[['종가']]

# df['변화량'] = df['종가'] - df['종가'].shift(1)
# df.loc[df['변화량'] >= 0 , '상승폭'] = df['변화량']
# df.loc[df['변화량'] < 0 , '하락폭'] = -df['변화량']
# df = df.fillna(0)

# df['AU'] = df['상승폭'].rolling(14).mead() # 14일 동안의 상승폭 평균
# df['DU'] = df['하락폭'].rolling(14).mean() # 14일 동안의 하락폭 평균
# df['RSI'] = df['AU'] / (df['AU'] + df['DU']) * 100

# df = df[['종가', 'RSI']]
# print(df.head())

# df['일간수익률'] = df['종가'].pct_change() + 1

# df.loc[df['RSI'] < 30 , '매매신호'] = True
# df.loc[df['RSI'] > 70 , '매매신호'] = False

# # 전날 종가 매수면 당일은 보유
# df.loc[df['매매신호'].shift(1) == True, '보유여부'] = True
# # 전날 종가 매도면 당일은 미보유
# df.loc[df['매매신호'].shift(1) == False, '보유여부'] = False
# # 매수/매도 조건이 아니라면 전일 상태 유지
# df['보유여부'].ffill(inplace = True)
# df['보유여부'].fillna(False, inplace = True)

# # print(df.loc['2000-02-03':].head(10))

# df['보유수익률'] = df.loc[ df['보유여부'] == True, '일간수익률']
# df['보유수익률'].fillna(1, inplace = True)

# df['RSI수익률'] = df['보유수익률'].cumprod()
# df['단순보유수익률'] = df['종가'] / df.iloc[0, 0]
# print(df.tail())

# import matplotlib.pyplot as plt
# import platform
# plt.rcParams['figure.dpi'] = 200

# # 한글 처리
# if platform.system() == 'Darwin' :
#     plt.rc('font', family = 'AppleGothic')
# else:
#     plt.rc('font', family = 'Malgun Gothic')

# df[['RSI수익률', '단순보유수익률']].plot(figsize = (8, 4))

# from pykrx import stock
# import time
# import os

# if not os.path.isdir("data/data1"):
#     os.mkdir("data/data1")

# tickers = stock.get_market_ticker_list("20000101")
# for t in tickers:
#     df = stock.get_market_ohlcv_by_date("20000101", "20191231", t)
#     if df.empty:
#         continue

#     df.to_excel(f"data/data1/{t}.xlsx")
#     time.sleep(0.5) # 서버 과부하 방지 위해 0.5초 대기

# def RSI(df, window = 14, threshold_low  = 30, threshold_high = 70):
#     df = df.query('종가 ! = 0')
#     df = df[['종가']].copy()
#     df['변화량'] = df['종가'] - df['종가'].shift(1)
#     df.loc[df['변화량'] >= 0 , '상승폭'] = df['변화량']
#     df.loc[df['변화량'] < 0 , '하락폭'] = -df['변화량']
#     df = df.fillna(0)
#     df['AU'] = df['상승폭'].rolling(window).mean()
#     df['DU'] = df['하락폭'].rolling(window).mean()
#     df['RSI'] = df['AU'] / (df['AU'] + df['DU']) * 100
#     df = df[['종가', 'RSI']].copy()

#     df['일간수익률'] = df['종가'].pct_change() + 1
#     df.loc[df['RSI'] < threshold_low , '매매신호'] = True
#     df.loc[df['RSI'] > threshold_high , '매매신호'] = False
#     df.loc[df['매매신호'].shift(1) == True, '보유여부'] = True
#     df.loc[df['매매신호'].shift(1) == False, '보유여부'] = False   

#     df['보유여부'].ffill(inplace = True)
#     df['보유여부'].fillna(False, inplace = True)
#     df['보유수익률'] = df.loc[ df['보유여부'] == True, '일간수익률']
#     df['보유수익률'].fillna(1, inplace = True)
#     return df['보유수익률'].cumprod().iloc[-1]

# import pandas as pd

# yeild = []
# file_list = os.listdir("data/data1")
# for file in file_list:
#     df = pd.read_excel(f"data/data1/{file}")
#     val = RSI(df)
#     yeild.append(val)

# s = pd.Series(yeild, index = file_list)
# print(s.describe())    

# print(s.idxmax())

# df = stock.get_market_ohlcv_by_date("20000101", "20191231", "008080")
# df.loc['2013-09':, '종가'].plot(figsize = (8,2))

# print(s.idxmin())
# print(df['종가'].tail())

# df = stock.get_market_ohlcv_by_date("20000101", "20191231", "007630")
# df.loc[:"2001", '종가'].plot(figsize = (8,2))

# idx = []
# yeild = []
# file_list = os.listdir("data/data1")
# for file in file_list:
#     df = pd.read_excel(f"data/data1/{file}")
#     cond = abs(df['종가'].pct_change()) > 0.3
#     if len(df[cond]) ! = 0:
#         continue

#     val = RSI(df)
#     idx.append(file.split(".")[0])
#     yeild.append(val)

# s = pd.Series(yeild, index = idx)
# print(s.descirbe())

# df = stock.get_index_ohlcv_by_date("20000101", "20191231", "1010")
# peinr(df['종가'][-1]/df['종가'][0])