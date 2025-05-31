# scripts/data_cleaning.py

import pandas as pd

def clean_data(df):
    """
    Cleans the DataFrame:
    - Converts 'Date' to datetime
    - Drops rows with missing essential data
    - Converts numeric columns to float
    - Sorts by date
    - Drops rows with remaining NaNs
    - Resets index
    """
    df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
    
    # Drop rows with missing key columns
    df.dropna(subset=['Date', 'Open', 'High', 'Low', 'Close', 'Volume'], inplace=True)
    
    # Convert numeric columns to float (coerce invalid strings to NaN)
    numeric_cols = ['Open', 'High', 'Low', 'Close', 'Volume']
    df[numeric_cols] = df[numeric_cols].apply(pd.to_numeric, errors='coerce')
    
    # Drop rows with any remaining NaNs
    df.dropna(inplace=True)
    
    # Sort by date and reset index
    df = df.sort_values('Date').reset_index(drop=True)
    
    return df
