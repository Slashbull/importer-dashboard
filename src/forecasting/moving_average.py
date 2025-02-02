import pandas as pd

def moving_average(df, window=30):
    """
    Calculates moving average for a given dataframe.
    By default, it uses a 30-day moving average for forecasting trends.
    """
    df['Moving Average'] = df['Quantity (tons)'].rolling(window=window).mean()
    
    return df
