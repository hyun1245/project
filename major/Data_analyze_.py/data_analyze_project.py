import yfinance as yf

# 'NVDA' 티커에 대한 객체 생성
ticker = "NVDA"
stock_data = yf.download(ticker, start="2020-01-01", end="2025-11-04")

# 다운로드된 데이터 확인 (상위 5개)
print(stock_data.head())

# Ticker 객체로 상세 정보 접근
stock_info = yf.Ticker("NVDA").info

# 총 발행 주식 수 확인
shares_outstanding = stock_info.get('sharesOutstanding')

if shares_outstanding:
    # 일별 종가에 총 발행 주식 수를 곱하여 시가총액 계산
    stock_data['MarketCap'] = stock_data['Close'] * shares_outstanding
    print(stock_data.head())
else:
    print("총 발행 주식 수 정보를 가져올 수 없습니다.")


# CSV 파일로 저장
stock_data.to_csv("NVDA_stock_data.csv")

# 필요한 라이브러리 임포트
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import yfinance as yf

# ==============================================================================
# 1. 데이터 로딩 및 전처리
# ==============================================================================

# 분석 대상 종목 및 기간 설정
tickers = ['TSLA', 'NVDA']
start_date = '2024-11-04'
end_date = '2025-11-04'

# --- 로컬 환경용 실제 데이터 다운로드 코드 ---
# # yfinance를 사용하여 데이터 다운로드
# data = {}
# for ticker in tickers:
#     data[ticker] = yf.download(ticker, start=start_date, end=end_date)

# --- 현재 환경용 가상 데이터 생성 코드 ---
np.random.seed(123)
dates = pd.date_range(start=start_date, end=end_date, freq='B')
n = len(dates)
data = {
    'TSLA': pd.DataFrame({'Close': np.cumprod(1 + np.random.normal(0, 0.02, n)) * 600}, index=dates),
    'NVDA': pd.DataFrame({'Close': np.cumprod(1 + np.random.normal(0, 0.025, n)) * 300}, index=dates)
}
# -----------------------------------------


# ==============================================================================
# 2. 지표 계산 및 3. 매매 신호 생성 함수
# ==============================================================================

def generate_signals(df, window):
    # 2. 지표 계산: 이동평균선(SMA) 계산
    df[f'SMA_{window}'] = df['Close'].rolling(window=window).mean()

    # 3. 매매 신호 생성
    df['Signal'] = 0
    # 종가가 이평선을 상향 돌파 시 매수 신호(1)
    df.loc[(df['Close'] > df[f'SMA_{window}']) & (df['Close'].shift(1) <= df[f'SMA_{window}'].shift(1)), 'Signal'] = 1
    # 종가가 이평선을 하향 돌파 시 매도 신호(-1)
    df.loc[(df['Close'] < df[f'SMA_{window}']) & (df['Close'].shift(1) >= df[f'SMA_{window}'].shift(1)), 'Signal'] = -1
    return df

# ==============================================================================
# 4. 백테스팅 시뮬레이션 함수
# ==============================================================================

def backtest_strategy(df, window, initial_capital=1_000_000):
    """매매 신호에 따라 백테스팅을 수행하고 성과를 반환합니다."""
    
    data_with_signals = generate_signals(df.copy(), window)
    
    capital = initial_capital
    position = 0  # 보유 주식 수
    portfolio_values = []

    for i in range(len(data_with_signals)):
        row = data_with_signals.iloc[i]
        
        # 매수 신호 발생 및 현금 보유 시
        if row['Signal'] == 1 and capital > 0:
            position = capital // row['Close']  # 현재가로 살 수 있는 최대 주식 수
            capital -= position * row['Close']
        
        # 매도 신호 발생 및 주식 보유 시
        elif row['Signal'] == -1 and position > 0:
            capital += position * row['Close']
            position = 0

        # 현재 포트폴리오 가치 계산 (현금 + 보유 주식 평가액)
        portfolio_value = capital + position * row['Close']
        portfolio_values.append(portfolio_value)

    data_with_signals['Portfolio_Value'] = portfolio_values
    
    return data_with_signals

# ==============================================================================
# 5. 성과 분석 및 시각화
# ==============================================================================

def analyze_performance(df, ticker, window):
    """백테스트 결과를 분석하고 시각화합니다."""
    
    # 누적 수익률 계산
    final_value = df['Portfolio_Value'].iloc[-1]
    initial_value = df['Portfolio_Value'].iloc[0]
    cumulative_return = (final_value / initial_value - 1) * 100

    # 최대 낙폭 (Maximum Drawdown, MDD) 계산
    running_max = df['Portfolio_Value'].cummax()
    drawdown = (running_max - df['Portfolio_Value']) / running_max
    max_drawdown = drawdown.max() * 100

    print(f"--- {ticker} ({window}일 SMA 전략) 분석 결과 ---")
    print(f"최종 포트폴리오 가치: {final_value:,.0f} 원")
    print(f"누적 수익률: {cumulative_return:.2f}%")
    print(f"최대 낙폭 (MDD): {max_drawdown:.2f}%")
    print("-" * 40)

    # 시각화
    plt.style.use('seaborn-v0_8-whitegrid')
    fig, ax1 = plt.subplots(figsize=(15, 7))

    # 1축: 주가 및 이동평균선
    ax1.plot(df.index, df['Close'], label='Close Price', color='skyblue')
    ax1.plot(df.index, df[f'SMA_{window}'], label=f'{window}-Day SMA', color='orange', linestyle='--')
    ax1.set_xlabel('Date')
    ax1.set_ylabel('Stock Price ($)')
    
    # 매수/매도 신호 표시
    buy_signals = df[df['Signal'] == 1]
    ax1.scatter(buy_signals.index, buy_signals['Close'], marker='^', color='green', s=100, label='Buy Signal', zorder=5)
    sell_signals = df[df['Signal'] == -1]
    ax1.scatter(sell_signals.index, sell_signals['Close'], marker='v', color='red', s=100, label='Sell Signal', zorder=5)
    
    # 2축: 포트폴리오 가치
    ax2 = ax1.twinx()
    ax2.plot(df.index, df['Portfolio_Value'], label='Portfolio Value', color='purple', alpha=0.7)
    ax2.set_ylabel('Portfolio Value (KRW)')

    fig.suptitle(f'{ticker} - {window}-Day SMA Strategy', fontsize=16)
    fig.legend(loc='upper left', bbox_to_anchor=(0.1, 0.9))
    plt.show()

# --- 실행 ---
# 20일 이동평균선 전략을 예시로 실행
selected_window = 5
for ticker in tickers:
    backtested_data = backtest_strategy(data[ticker], window=selected_window)
    analyze_performance(backtested_data, ticker, window=selected_window)


