import pandas as pd

def competitor_performance(df):
    """
    Analyzes competitor performance based on sales volume.
    """
    competitor_performance_df = df.groupby('Consignee')['Quantity (tons)'].sum().reset_index()
    competitor_performance_df = competitor_performance_df.sort_values(by='Quantity (tons)', ascending=False)
    
    return competitor_performance_df
