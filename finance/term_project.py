import matplotlib.pyplot as plt
import platform
from matplotlib.ticker import MaxNLocator

if platform.system() == 'Darwin':
    plt.rc('font', family = 'AppleGothic')
else:
    plt.rc('font', family = 'Malgun Gothic')

import pandas as pd
Bitcoin = pd.read_csv("data/Bitcoin Data(20240101~20241231).csv", index_col = "Date")
Bitcoin.index = pd.to_datetime(Bitcoin.index)
print(Bitcoin)

Bitcoin.rename(columns={'Price': 'Close'}, inplace=True)
print(Bitcoin.head())

columns_to_convert = ['Open', 'High', 'Low', 'Close']

Bitcoin[columns_to_convert] = Bitcoin[columns_to_convert].apply(
    lambda x: x.astype(str).str.replace(',', '', regex=False).astype(float))
print(Bitcoin.head())

import matplotlib.pyplot as plt
fig = plt.figure(figsize = (14,6))
ax = fig.add_subplot(1,1,1)
ax.plot(Bitcoin['High'])

ax.set_xlabel("날짜")
ax.set_ylabel("가격(USD)")
ax.set_title("비트코인 고가 추이(2024년)")

ax.yaxis.set_major_locator(MaxNLocator(10))

plt.grid(True, axis = 'y')
# plt.show()

import mplfinance as mpf
mpf.plot(Bitcoin, type = 'candle')

mc = mpf.make_marketcolors(
    up = "r",
    down = "b",
    edge = "inherit",
    wick = "inherit",
)
s = mpf.make_mpf_style(
    base_mpf_style="starsandstripes", 
    marketcolors=mc, 
    gridaxis='both',   # horizontal, vertical, both
    y_on_right=True    # False는 y축을 왼쪽에 표시
)
mpf.plot(Bitcoin, type = 'candle', style = s, title = "비트코인(2024년)", ylabel = "가격(USD)", volume = True)