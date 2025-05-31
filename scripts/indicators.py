# scripts/indicators.py

import talib

def add_technical_indicators(df):
    """
    Adds common TA-Lib technical indicators to the DataFrame:
    - SMA (Simple Moving Average)
    - RSI (Relative Strength Index)
    - MACD (Moving Average Convergence Divergence)
    """
    df['SMA_20'] = talib.SMA(df['Close'], timeperiod=20)
    df['RSI_14'] = talib.RSI(df['Close'], timeperiod=14)

    macd, macd_signal, macd_hist = talib.MACD(
        df['Close'],
        fastperiod=12,
        slowperiod=26,
        signalperiod=9
    )
    df['MACD'] = macd
    df['MACD_Signal'] = macd_signal
    df['MACD_Hist'] = macd_hist

    return df
