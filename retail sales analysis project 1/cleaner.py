import pandas as pd

def clean_retail_data(raw_records, column_names):
    """
    Automates text standardization and multi-variable data grouping.
    """
    df = pd.DataFrame(raw_records, columns=column_names)
    
    # 1. Standardize messy spacing and uppercase text
    df['Region'] = df['Region'].str.strip().str.title()
    
    # 2. Group the data by Region to calculate total revenue
    summary = df.groupby('Region')['Revenue'].sum().reset_index()
    
    return summary
