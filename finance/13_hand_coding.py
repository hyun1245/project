from pykrx import stock
import FinanceDataReader as fdr

df = fdr.DataReader(symbol = 'KS11', start = '2019-11')
start = df.loc["2019-11"]
end = df.loc["2020-09"]

# print(df.loc["2020-11"].head())
# print(start)

start_date = start.index[0]
end_date = end.index[-1]
# print(start_date, end_date)

df1 = stock.get_market_ohlcv_by_ticker("20191101")
df2 = stock.get_market_ohlcv_by_ticker("20200929")
kospi = df1.join(df2, lsuffix = "_l", rsuffix = "_r")
# print(kospi)

kospi['모멘텀'] = 100 * (kospi['종가_r'] - kospi['종가_l']) / kospi['종가_l']
kospi = kospi[['종가_l', '종가_r', '모멘텀']]
kospi = kospi.sort_values(by='모멘텀', ascending=False)[:20]
# print(kospi)

kospi_momentum20 = kospi.sort_values(by='모멘텀', ascending=False)[:20]
kospi_momentum20.rename(columns = {"종가_l" : "매수가", "종가_r" : "매도가"}, inplace = True)
# print(kospi_momentum20)

df3 = stock.get_market_ohlcv_by_ticker("20201102")
df4 = stock.get_market_ohlcv_by_ticker("20210430")
pct_df = df3.join(df4, lsuffix = "_l", rsuffix = "_r")
# print(pct_df)

pct_df = pct_df[['종가_l', '종가_r']]
kospi_momentum20 = kospi_momentum20.join(pct_df)
# print(kospi_momentum20)


kospi_momentum20['수익률'] = (kospi_momentum20['종가 _r'] / 
                           kospi_momentum20['종가_l'])
# print(kospi_momentum20)

수익률평균 = kospi_momentum20['수익률'].fillna(0).mean()
# print(수익률평균)

mom20_cagr = 수익률평균 ** (1/0.5) - 1 # 6개월 수익률
# print(mom20_cagr * 100)

df_ref = fdr.DataReader(
    symbol = 'KS11',
    start = "2020-11-02", # 첫번째 거래일
    end = "2021-04-30"
)
# print(df_ref)

CAGR = ((df_ref['Close'].iloc[-1] / df_ref['Close'].iloc[0]) ** (1/0.5)) - 1
# print(CAGR * 100)

df1 = stock.get_market_ohlcv_by_ticker("20191101", market = "ALL")
df2 = stock.get_market_ohlcv_by_ticker("20200929", market = "ALL")
all = df1.join(df2, lusffix = "_l", rsuffix = "_r")
# print(all)

# 기본 필터링
# 우선주 제외
all2 = all.filter(regex = "0$", axis = 0).copy() # 0으로 끝나는 종목코드
# print(all2)

cap = stock.get_market_cap_by_ticker(date = "20200929", market = "ALL")
cap = cap[['시가총액']]
# print(cap)

all3 = all2.join(other = cap)
# print(all3)

# 대형주 필터링
big = all3.sort_values(by = '시가총액', ascending = False)[:200] # 오름차순 (상위 200개)
# print(big)

# print(big.sort_values(by = '모멘텀', ascending = False))

big_pct20 = big.sort_values(by = '모멘텀', ascending = False)[:20]
# print(big_pct20)

df3 = stock.get_market_ohlcv_by_ticker("20201102", market = "ALL")
df4 = stock.get_market_ohlcv_by_ticker("20211025", market = "ALL")

pct_df = df3.join(df4, lsuffix = "_l", rsuffix = "_r")
pct_df['수익률'] = pct_df['종가_r'] / pct_df['종가_l']
pct_df = pct_df[['종가_l', '종가_r', '수익률']]
# print(pct_df)

big_mom_result = big_pct20.join(pct_df)
# print(big_mom_result)

평균수익률 = big_mom_result['수익률'].mean()
big_mom_cagr = (평균수익률 ** 1/1) -1 
# print(big_mom_cagr * 100)

import pandas as pd
import datetime
from dateutil.relativedelta import relativedelta

year = 2010
month = 11
period = 6

inv_start = f"{year}-{month}-01"
inv_start = datetime.datetime.strptime(inv_start, "%Y-%m-%d")
inv_end = inv_start + relatuvedelta(months = period - 1) 

mon_start = inv_start - relativedelta(months = 12)
mon_end = inv_start - relativedelta(months = 2)
# print(mon_start.strftime("%Y-$m"), mon_end.strftime("%Y-%m"), "=>",
#       inv_start.strftime("%Y-%m"), inv_end.strftime("%Y-%m"))

df = fdr.DataReader(symbol = 'KS11')
# print(df)

def get_business_day(df, year, month, index=0):
    str_month = f"{year}-{month}"
    return df.loc[str_month].index[index]

df = fdr.DataReader(symbol = 'KS11')
get_business_day(df, 2010, 1, 0)

def momentum(df, year = 2010, month = 11, period = 12):
    # 투자 시작일, 종료일
    str_day = f"{year}-{month}-01"
    statr = datetime.datetime.strptime(str_day, "%Y-%m-%d")
    end = start + relativedelta(months = period -1)
    inv_start = get_business_day(df, start.year, start.month, 0) # 첫번째 거래일의 종가
    inv_end = get_business_day(df,enf.year, end.month, -1)
    inv_start = inv_start.strftime("%Y-%m-%d")
    inv_end = inv_end.strftime("%Y-%m-%d")
    # print(inv_start, inv_end)

    # 모멘턴 계산 시작일, 종료일
    end = start - relativedelta(months = 2) # 역추세 1개월 제외
    start = start - relativedelta(months = period)
    mon_start = get_business_day(df, start.year, start.month, 0) # 첫번쨰 거래일의종가
    mon_end = get_business_day(df, end.year, end.month, -1)
    mon_start = mon_start.strftime("%Y-%m-%d")
    mon_end = mon_end.strftime("%Y-%m-%d")
    print(mon_start, mon_end, " | ", inv_start, inv_end)

    # momentum 계산
    df1 = stock.get_market_ohlcv_by_ticker(mon_start)
    df2 = stock.get_market_ohlcv_by_ticker(mon_end)
    mon_df = df1.join(df2, lsuffix = "l", rsuffix = "r")
    mon_df['등락률'] = (mon_df['종가r'] - mon_df['종가l'])/mon_df['종가l']*100

    # 우선주 제외
    mon_df2 = mon_df.filter(regex = "0$", axis = 0)
    mon20 = mon_df.sort_values(by = "등락률", ascending = False)[:20]
    mon20 = mon20[['등락률']]
    # print(mon20)

    # 투자 기간 수익률 
    df3 = stock.get_market_ohlcv_by_ticker(inv_start)
    df4 = stock.get_market_ohlcv_by_ticker(inv_end)
    inv_df = df3.join(df4, lsufixx = "l", rsuffix = "r")
    inv_df['수익률'] = inv_df['종가r'] / inv_df['종가l'] # 수익률 = 매도가 / 매수가
    inv_df = inv_df[['수익률']]

    # join
    result_df = mon20.join(inv_df)
    result = result_df['수익률'].fillna(0).mean()
    return year, result

import time

data = []
for year in range(2010, 2021):
    ret = momentum(df, year , month = 11, period = 6)
    data.append(ret)
    time.sleep(1)

import pandas as pd
ref_df = pd.DataFrame(data = data, columns = ['year', 'yield'])
ref_df.set_index('year', inplace = True)
# print(ref_df)

cum_yield = ret_df['yield'].cumprod()
# print(cum_yield)

CAGR = cum_yield.iloc[-1] ** (1/11) -1
# print(CAGR * 100)

buy_price = df.loc['2010-11'].iloc[0, 0]
sell_price = df.loc['2021-04'].iloc[-1, 0]
kospi_yield = sell_price / buy_price
kospi_cagr = kospi_yield ** (1/11) - 1
# print(kospi_cagr * 100)