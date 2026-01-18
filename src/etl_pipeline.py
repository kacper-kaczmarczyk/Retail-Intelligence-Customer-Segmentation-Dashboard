import pandas as pd
import numpy as np
import os

def clean_retail_data(input_file='online_retail_II.xlsx', output_file='processed_retail_data.csv'):
    """
    ETL Script to clean the raw Online Retail II dataset from Kaggle/UCI.
    Ref: https://archive.ics.uci.edu/ml/datasets/Online+Retail+II
    
    Steps:
    1. Loads raw Excel/CSV.
    2. Removes records with missing Customer ID (crucial for RFM).
    3. Handles cancellations (Quantity < 0).
    4. Filters out non-product codes (Manual, Postage).
    5. Exports clean data for Power BI/Excel consumption.
    """
    
    print("🚀 Starting ETL Pipeline...")
    
    # Check if file exists
    if not os.path.exists(input_file):
        print(f"❌ Error: File '{input_file}' not found. Please download it from Kaggle/UCI.")
        return

    # 1. Load Data
    print(f"📥 Loading data from {input_file} (this might take a moment)...")
    df = pd.read_csv(input_file, encoding='ISO-8859-1')

    initial_shape = df.shape
    print(f"Raw data shape: {initial_shape}")

    # 2. Data Cleaning
    print("🧹 Cleaning data...")

    # Drop rows with missing Customer ID (we cannot calculate CLV/RFM without ID)
    df.dropna(subset=['Customer ID'], inplace=True)
    
    # Rename columns to standard snake_case or CamelCase for consistency
    df.rename(columns={
        'Invoice': 'InvoiceNo', 
        'Price': 'UnitPrice', 
        'Customer ID': 'CustomerID'
    }, inplace=True)

    # Convert CustomerID to integer then string
    df['CustomerID'] = df['CustomerID'].astype(int).astype(str)

    # 3. Handling Cancellations
    # In this dataset, cancellations usually have 'C' in InvoiceNo and negative Quantity.
    
    # Remove records with negative quantity that represent actual returns/errors
    # (keeping only positive sales for the main revenue dashboard)
    df_sales = df[df['Quantity'] > 0].copy()

    # 4. Feature Engineering
    df_sales['TotalSales'] = df_sales['Quantity'] * df_sales['UnitPrice']
    df_sales['InvoiceDate'] = pd.to_datetime(df_sales['InvoiceDate'])

    # 5. Filter out non-product logic (Optional but recommended)
    # Removing 'POST' (Postage), 'M' (Manual), 'BANK CHARGES'
    exclude_codes = ['POST', 'M', 'D', 'BANK CHARGES']
    df_sales = df_sales[~df_sales['StockCode'].isin(exclude_codes)]

    final_shape = df_sales.shape
    print(f"   Cleaned data shape: {final_shape}")
    print(f"   Rows removed: {initial_shape[0] - final_shape[0]}")

    # 6. Export
    print(f"💾 Saving processed data to {output_file}...")
    df_sales.to_csv(output_file, index=False)
    print("✅ ETL Complete! You can now import this CSV into Excel/Power BI.")

if __name__ == "__main__":
    # Updated to point to the correct location of the dataset
    input_path = os.path.join('data', 'raw', 'online_retail_II.csv')
    output_path = os.path.join('data', 'processed', 'processed_retail_data.csv')
    
    clean_retail_data(input_file=input_path, output_file=output_path)