import pandas as pd

def validate_data(df):
    """
    Validates the incoming data for required columns, data types, and missing values.
    """
    required_columns = ['Consignee', 'Exporter', 'Product', 'Quantity', 'Date']
    
    # Check for missing columns
    missing_columns = [col for col in required_columns if col not in df.columns]
    if missing_columns:
        raise ValueError(f"Missing required columns: {', '.join(missing_columns)}")
    
    # Check for missing data
    missing_data = df.isnull().sum()
    if missing_data.any():
        raise ValueError(f"Missing data detected: {missing_data[missing_data > 0]}")
    
    return df
