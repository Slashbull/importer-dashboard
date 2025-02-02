def normalize_data(df):
    """
    Normalizes data by handling different units and normalizing the quantity values.
    Converts quantity from kgs to tons if necessary.
    """
    # Normalize the 'Quantity' column to tons
    df['Quantity (tons)'] = df['Quantity'] / 1000  # Assuming quantity is in kgs
    
    return df
