# scripts/data_cleaning.py

import pandas as pd

def load_data(file_path):
    """Load CSV data into a DataFrame."""
    df = pd.read_csv(file_path)
    return df

def clean_data(df):
    """
    Cleans the DataFrame:
    - Converts 'Date' column to datetime
    - Drops rows with invalid or missing data
    - Sorts by date
    - Resets index
    """
    df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
    df.dropna(subset=['Date', 'Open', 'High', 'Low', 'Close', 'Volume'], inplace=True)
    df = df.sort_values('Date').reset_index(drop=True)
    return df

def count_invalid_dates(df):
    """Returns number of NaT values in the 'Date' column."""
    return df['Date'].isna().sum()
