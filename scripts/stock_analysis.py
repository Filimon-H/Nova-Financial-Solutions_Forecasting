# stock_analysis.py

import pandas as pd
import matplotlib.pyplot as plt
import talib

def load_and_prepare_data(file_path):
    df = pd.read_csv(file_path)
    df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
    df = df.dropna(subset=['Date'])
    df = df.sort_values('Date')
    return df

def apply_indicators(df):
    df['SMA_20'] = talib.SMA(df['Close'], timeperiod=20)
    df['RSI_14'] = talib.RSI(df['Close'], timeperiod=14)
    macd, macd_signal, macd_hist = talib.MACD(df['Close'])
    df['MACD'] = macd
    df['MACD_Signal'] = macd_signal
    df['MACD_Hist'] = macd_hist
    return df

def detect_signals(df):
    df['Buy_Signal'] = (df['RSI_14'] < 30) | ((df['MACD'] > df['MACD_Signal']) & (df['MACD'].shift(1) <= df['MACD_Signal'].shift(1)))
    df['Sell_Signal'] = (df['RSI_14'] > 70) | ((df['MACD'] < df['MACD_Signal']) & (df['MACD'].shift(1) >= df['MACD_Signal'].shift(1)))
    return df

def plot_all(df, title="Stock Analysis"):
    fig, axs = plt.subplots(3, 1, figsize=(14, 12), sharex=True)

    # Price + SMA + signals
    axs[0].plot(df['Date'], df['Close'], label='Close Price', color='blue')
    axs[0].plot(df['Date'], df['SMA_20'], label='SMA 20', color='orange')
    axs[0].scatter(df[df['Buy_Signal']]['Date'], df[df['Buy_Signal']]['Close'], marker='^', color='green', label='Buy Signal')
    axs[0].scatter(df[df['Sell_Signal']]['Date'], df[df['Sell_Signal']]['Close'], marker='v', color='red', label='Sell Signal')
    axs[0].set_title('Close Price and SMA with Signals')
    axs[0].legend()
    axs[0].grid(True)

    # RSI
    axs[1].plot(df['Date'], df['RSI_14'], label='RSI 14', color='purple')
    axs[1].axhline(70, color='red', linestyle='--')
    axs[1].axhline(30, color='green', linestyle='--')
    axs[1].set_title('RSI Indicator')
    axs[1].legend()
    axs[1].grid(True)

    # MACD
    axs[2].plot(df['Date'], df['MACD'], label='MACD', color='black')
    axs[2].plot(df['Date'], df['MACD_Signal'], label='Signal Line', color='red')
    axs[2].bar(df['Date'], df['MACD_Hist'], label='MACD Hist', color='gray')
    axs[2].set_title('MACD Indicator')
    axs[2].legend()
    axs[2].grid(True)

    plt.tight_layout()
    plt.suptitle(title, fontsize=16)
    plt.subplots_adjust(top=0.95)
    plt.show()
