import pandas as pd

def load_data(file_path):
    """
    Load CSV data into a DataFrame.
    
    Args:
        file_path (str): Path to the CSV file.
        
    Returns:
        pd.DataFrame: Loaded DataFrame
    """
    df = pd.read_csv(file_path)
    return df

def clean_data(df):
    """
    Cleans the stock price DataFrame:
    - Converts 'Date' to datetime
    - Drops rows with missing essential data
    - Converts numeric columns to float
    - Sorts by date
    - Drops rows with remaining NaNs
    - Resets index
    
    Args:
        df (pd.DataFrame): Raw stock price data.
        
    Returns:
        pd.DataFrame: Cleaned DataFrame
    """
    # Convert Date column
    df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
    
    # Drop rows with missing critical fields
    df.dropna(subset=['Date', 'Open', 'High', 'Low', 'Close', 'Volume'], inplace=True)
    
    # Convert numeric columns to float
    numeric_cols = ['Open', 'High', 'Low', 'Close', 'Volume']
    df[numeric_cols] = df[numeric_cols].apply(pd.to_numeric, errors='coerce')
    
    # Drop any remaining rows with NaNs
    df.dropna(inplace=True)
    
    # Sort and reset index
    df = df.sort_values('Date').reset_index(drop=True)
    
    return df

def count_invalid_dates(df):
    """
    Counts number of invalid (NaT) values in the 'Date' column.
    
    Args:
        df (pd.DataFrame): DataFrame to check.
        
    Returns:
        int: Number of invalid dates.
    """
    return df['Date'].isna().sum()
