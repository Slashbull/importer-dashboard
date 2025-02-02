import pandas as pd

def exponential_smoothing(df, alpha=0.1):
    """
    Applies Exponential Smoothing for trend prediction.
    """
    df['Exponential Smoothing'] = df['Quantity (tons)'].ewm(alpha=alpha).mean()
    
    return df
