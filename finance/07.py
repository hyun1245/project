# import matplotlib.pyplot as plt

# fig = plt.figure()
# subplot = fig.add_subplot(1, 1, 1)
# subplot.plot([1, 2, 3, 4])
# plt.show()

# import matplotlib.pyplot as plt 

# fig = plt.figure()
# subplot1 = fig.add_subplot(1, 2, 1) #1행, 2열의 첫 번째 subplot
# subplot2 = fig.add_subplot(1, 2, 2)
# subplot1.plot([1, 2, 3, 4])
# subplot2.plot([4, 3, 2, 1])
# plt.show()

# import matplotlib.pyplot as plt 

# fig, axes = plt.subplots(2, 2)

# axes[0][0].plot([1, 2, 3, 4])
# axes[0][1].plot([4, 3, 2, 1])
# axes[1][0].plot([1, 2, 2, 1])
# axes[1][1].plot([2, 1, 1, 2])
# plt.show()

# import matplotlib.pyplot as plt

# plt.plot([1, 2, 3, 4])
# plt.show()

# import matplotlib.pyplot as plt 

# plot 함수로  리스트를 전달하면 해당 값을 y축 값으로 사용
# x축 값은 자동으로 0부터 시작하는 정수로 설정
# plt.plot([2, 1, 1, 2])
# plt.show()

# import matplotlib.pyplot as plt 

# 처음 리스트는 x축 값, 두 번째 리스트는 y축 값으로 사용
# plt.plot([1, 2, 3, 4], [2, 1, 1, 2])

# plt.xlabel("x-axis")
# plt.ylabel("y-axis")
# plt.title("title")
# plt.show()

# import matplotlib.pyplot as plt 

# fig, ax = plt.subplots()
# ax.plot([1, 2, 3, 4], [2, 1, 1, 2])

# ax.set_xlabel("x-axis")
# ax.set_ylabel("y-axis")
# ax.set_title("title")

# plt.show()

# import matplotlib.pyplot as plt 

# 여러 개의 선 그리기(하나의 plot에 여러번 겹쳐짐)
# plt.plot([1, 2, 3, 4], [1, 2, 3, 4])
# plt.plot([1, 2, 3, 4], [4, 3, 2, 1])

# plt.show()


# import matplotlib.pyplot as plt 

# # 범례 표시하기
# plt.plot([1, 2, 3, 4], [1, 2, 3, 4], label='ascending')
# plt.plot([1, 2, 3, 4], [4, 3, 2, 1], label='descending')

# plt.legend(loc='best') # loc = 'best'는 자동으로 최적의 위치에 범례를 배치
# plt.show()

import matplotlib.pyplot as plt
import platform

# 한글 폰트 설정
if platform.system() == 'Darwin':
    plt.rc('font', family='AppleGothic') 
else:
    plt.rc('font', family='Malgun Gothic') 

    
# import pandas as pd

# kospi = pd.read_excel("data/kospi.xlsx", index_col="Date")
# print(kospi)

# import matplotlib.pyplot as plt 

# fig = plt.figure(figsize=(14, 6))
# ax = fig.add_subplot(1, 1, 1)
# ax.plot(kospi['Close'])

# ax.set_xlabel("날짜")
# ax.set_ylabel("코스피지수")
# ax.set_title("2019년 이후 코스피지수")
# plt.grid(True, axis='y')
# plt.show()

import pandas as pd

df = pd.read_excel("data/loan.xlsx", index_col=0, header=[0, 1])
# print(df.head())

대출잔액 = df['대출잔액']
대출잔액 = 대출잔액[::-1] # 데이터프레임의 행 순서를 뒤집음
# print(대출잔액.head())

# import matplotlib.pyplot as plt

# fig = plt.figure(figsize=(12, 8))
# plt.plot(대출잔액.index, 대출잔액["전체"], marker='o', label="전체")
# plt.plot(대출잔액.index, 대출잔액["1금융권"], marker='o', label="1금융권")
# plt.plot(대출잔액.index, 대출잔액["2금융권"], marker='o', label="2금융권")

# plt.rc("axes", unicode_minus=False)   # y축 음수처리
# plt.ylabel("(전년동월비,%)")
# plt.legend()
# plt.grid(True, axis='y')
# plt.show()

import matplotlib.pyplot as plt

# plt.bar([1, 3, 5, 7, 9], [2, 3, 2, 2, 8])
# plt.show()

import pandas as pd

kospi = pd.read_excel("data/kospi.xlsx", index_col='Date')
kospi2020 = kospi.loc["2020"]
mean_kospi_2020 = kospi2020.resample('MS').mean()
# print(mean_kospi_2020.head())

import matplotlib.pyplot as plt
        
# fig = plt.figure(figsize=(15, 8))
# ax = fig.add_subplot(1, 1, 1)
# month = [x.strftime("%Y-%m") for x in mean_kospi_2020.index]
# ax.bar(x=month, height=mean_kospi_2020['Volume'], width=0.5, color='skyblue')

# plt.ticklabel_format(axis='y', style='plain')   # 지수로 표현하지 않음
# plt.title("KOSPI 월별 평균 거래량 (2020년)")
# plt.xlabel("월")
# plt.ylabel("평균 거래량")
# plt.show()

import matplotlib.pyplot as plt
        
# fig = plt.figure(figsize=(15, 8))
# ax = fig.add_subplot(1, 1, 1)
# month = [x.strftime("%Y-%m") for x in mean_kospi_2020.index]
# ax.barh(y=month[::-1], width=mean_kospi_2020['Volume'][::-1], height=0.5, color='#F88878')

# plt.ticklabel_format(axis='x', style='plain')  # 지수로 표현하지 않음
# plt.title("KOSPI 월별 평균 거래량 (2020년)")
# plt.ylabel("월")
# plt.xlabel("평균 거래량")
# plt.show() # 수평 막대 그래프

# import matplotlib.pyplot as plt

# data = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]   # 1이 1개, 2가 2개, 3이 3개, 4가 4개
# plt.hist(data)
# plt.show()

import pandas as pd

kospi = pd.read_excel("data/kospi.xlsx", index_col='Date')
# print(kospi.head())

import matplotlib.pyplot as plt 

# 정규분포 그래프를 그릴때 히스토그램을 자주 사용
# n, bins, patches = plt.hist(x=kospi['Change'] * 100, bins=20)
# plt.grid()
# plt.show()

import pandas as pd

sec = pd.read_excel("data/sec.xlsx", index_col="Date")
skhynix = pd.read_excel("data/skhynix.xlsx", index_col="Date")

# import matplotlib.pyplot as plt 


# fig = plt.figure(figsize=(12, 8))
# ax = fig.add_subplot(1, 1, 1)
# ax.plot(sec.index, sec['Close'], label="SEC")
# ax.plot(sec.index, skhynix['Close'], label="SK hynix")
# plt.title("삼성전자, SK하이닉스 2020년 가격 비교")
# plt.legend()
# plt.show()

## 지수화(표준화)

# import matplotlib.pyplot as plt 


# sec_index = (sec['Close'] / sec['Close'][0]) * 100
# skhynix_index = (skhynix['Close'] / skhynix['Close'][0]) * 100

# fig = plt.figure(figsize=(12, 8))
# ax = fig.add_subplot(1, 1, 1)
# ax.plot(sec.index, sec_index, label="SEC")
# ax.plot(sec.index, skhynix_index, label="SK hynix")
# plt.ylabel("가격지수")
# plt.title("삼성전자, SK하이닉스 2020년 가격지수 비교")
# plt.legend()
# plt.show()


import pandas as pd 

df = pd.read_excel("data/sec.xlsx", index_col=0)
df.head()

# import mplfinance as mpf

# 기본 캔들차트
# mpf.plot(data=df.loc["2020-12"], type='candle')

# mc = mpf.make_marketcolors(
#     up="r", 
#     down="b", 
#     edge="inherit",   # 캔들의 몸통색
#     wick="inherit"    # 캔들의 머리/꼬리색
# )

# s = mpf.make_mpf_style(
#     base_mpf_style="starsandstripes", 
#     marketcolors=mc, 
#     gridaxis='both',   # horizontal, vertical, both
#     y_on_right=True    # False는 y축을 왼쪽에 표시
# )

# mpf.plot(data=df.iloc[:60], type='candle', style=s, figratio=(13, 6))

##  거래량 표시 추가
# mc = mpf.make_marketcolors(
#     up="r", 
#     down="b", 
#     edge="inherit",   # 캔들의 몸통색
#     wick="inherit",   # 캔들의 머리/꼬리색
#     volume="inherit"  # 거래량 색상
# )

# s = mpf.make_mpf_style(
#     base_mpf_style="starsandstripes", 
#     marketcolors=mc, 
#     gridaxis='both',   # horizontal, vertical, both
#     y_on_right=True    # False는 y축을 왼쪽에 표시
# )

# mpf.plot(
#     data=df.iloc[:60], 
#     type='candle', 
#     style=s, 
#     figratio=(13, 6),
#     volume=True,      # volume
#     scale_width_adjustment=dict(volume=0.8, candle=1)
# )

# 5,20 이동평균선 추가
# mc = mpf.make_marketcolors(
#     up="r", 
#     down="b", 
#     edge="inherit",   # 캔들의 몸통색
#     wick="inherit",   # 캔들의 머리/꼬리색
#     volume="inherit"  # 거래량 색상
# )

# s = mpf.make_mpf_style(
#     base_mpf_style="starsandstripes", 
#     marketcolors=mc, 
#     gridaxis='both',   # horizontal, vertical, both
#     y_on_right=True    # False는 y축을 왼쪽에 표시
# )

# mpf.plot(
#     data=df.iloc[:60], 
#     type='candle',
#     mav=(5, 20),   # moving average
#     style=s, 
#     figratio=(13, 6),
#     volume=True,      # volume
#     scale_width_adjustment=dict(volume=0.8, candle=1)
# )