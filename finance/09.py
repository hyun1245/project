from pykrx import stock

tickers = stock.get_market_ticker_list("20190225")
print(tickers)

tickers = stock.get_market_ticker_list(market="KOSDAQ")
print(tickers)

t0 = stock.get_market_ticker_list("19950502")
t1 = stock.get_market_ticker_list("20210930")
print(len(t0), len(t1))

intersection = set(t0) & set(t1)
print(len(intersection))

complement = set(t1) - set(t0)
print(len(complement))

tickers = stock.get_index_ticker_list("20190225")
print(tickers)

for t in tickers:
    name = stock.get_index_ticker_name(t)
    print(t, name)

from pykrx import stock
from datetime import datetime, timedelta

# 어제 날짜를 YYYYMMDD 형식의 문자열로 가져오기
yesterday = (datetime.today() - timedelta(days=1)).strftime("%Y%m%d")

print("어제 날짜:", yesterday)  # 예: 20250105

df = stock.get_market_ohlcv("20190501",yesterday, "005930")
print(df.head())
print(df.tail())

import time 

tickers = stock.get_market_ticker_list()
for t in tickers:
    df = stock.get_market_ohlcv("20210101", "20210131", t)
    df.to_excel(f"{t}.xlsx")
    time.sleep(1)
    

df = stock.get_market_fundamental("20210108")
print(df.head())

print(df.sort_values("PER"))

print(df.query("PER != 0").sort_values("PER"))

