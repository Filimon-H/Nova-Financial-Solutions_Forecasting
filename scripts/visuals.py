# scripts/visuals.py

import matplotlib.pyplot as plt

def plot_indicators(df, ticker_name=""):
    """
    Plots:
    - Close price + SMA
    - RSI with thresholds
    - MACD, Signal Line, and Histogram
    """
    fig, axs = plt.subplots(3, 1, figsize=(14, 10), sharex=True)

    # 1. Close Price + SMA
    axs[0].plot(df['Date'], df['Close'], label='Close Price', color='blue')
    axs[0].plot(df['Date'], df['SMA_20'], label='SMA 20', color='orange')
    axs[0].set_title(f'{ticker_name} - Close Price and 20-Day SMA')
    axs[0].legend()
    axs[0].grid(True)

    # 2. RSI
    axs[1].plot(df['Date'], df['RSI_14'], label='RSI 14', color='purple')
    axs[1].axhline(70, color='red', linestyle='--', label='Overbought (70)')
    axs[1].axhline(30, color='green', linestyle='--', label='Oversold (30)')
    axs[1].set_title('Relative Strength Index (RSI)')
    axs[1].legend()
    axs[1].grid(True)

    # 3. MACD
    axs[2].plot(df['Date'], df['MACD'], label='MACD', color='black')
    axs[2].plot(df['Date'], df['MACD_Signal'], label='Signal Line', color='red')
    axs[2].bar(df['Date'], df['MACD_Hist'], label='MACD Histogram', color='gray', alpha=0.5)
    axs[2].set_title('MACD')
    axs[2].legend()
    axs[2].grid(True)

    plt.tight_layout()
    plt.show()
