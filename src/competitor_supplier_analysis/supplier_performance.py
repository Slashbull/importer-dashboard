import pandas as pd

def supplier_performance(df):
    """
    Analyzes supplier performance based on delivery times, consistency, and anomalies.
    """
    supplier_performance_df = df.groupby('Exporter')['Quantity (tons)'].sum().reset_index()
    supplier_performance_df = supplier_performance_df.sort_values(by='Quantity (tons)', ascending=False)
    
    return supplier_performance_df
