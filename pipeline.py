import pandas as pd
import sqlite3

# 1. INGEST: Read the raw data
print("Starting data pipeline...")
df = pd.read_csv('data/raw_sales.csv')

# 2. TRANSFORM: Clean the data
print("Cleaning data...")
df = df.dropna()
df['SaleDate'] = pd.to_datetime(df['SaleDate'])
df['Total'] = df['Quantity'] * df['UnitPrice']

# 3. LOAD: Save to a SQL Database
print("Loading data into SQLite database...")
conn = sqlite3.connect('sales.db')
df.to_sql('sales_data', conn, if_exists='replace', index=False)

# 4. VERIFY: Run a SQL query to summarize the data
print("Verifying data...")
query = """
SELECT Region, SUM(Total) as TotalRevenue 
FROM sales_data 
GROUP BY Region 
ORDER BY TotalRevenue DESC
"""
summary = pd.read_sql_query(query, conn)
print("\n--- Sales Summary by Region ---")
print(summary)

conn.close()
print("\nPipeline complete!")
