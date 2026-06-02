import os
import pandas as pd
from sqlalchemy import create_engine, text

# 1. Configuration & Paths
cleaned_data_path = r"C:\Users\Amir\Documents\GitHub\Olist-Churn-CLV-Analytics\data\cleaned"

DB_USER = "postgres"
DB_PASS = "893758"  # Replace with the password you set during installation
DB_HOST = "localhost"
DB_PORT = "5432"
DB_NAME = "olist_analytics"

print("--- Step 1: Checking/Creating Target Database ---")
# Connect to the default 'postgres' database first to execute management commands
maintenance_engine = create_engine(f"postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/postgres")

# Open connection with autocommit turned on (required for CREATE DATABASE statements)
with maintenance_engine.connect().execution_options(isolation_level="AUTOCOMMIT") as conn:
    # Check if our target database already exists
    result = conn.execute(text(f"SELECT 1 FROM pg_database WHERE datname='{DB_NAME}'"))
    db_exists = result.scalar()
    
    if not db_exists:
        print(f"Database '{DB_NAME}' not found. Creating it now...")
        conn.execute(text(f"CREATE DATABASE {DB_NAME}"))
        print(f"Database '{DB_NAME}' created successfully.")
    else:
        print(f"Database '{DB_NAME}' already exists. Proceeding to data load.")

# Dispose of the temporary maintenance engine connection
maintenance_engine.dispose()
print("="*50)


# 2. Establish Connection to the Target Analytics Database
print("--- Step 2: Connecting to Target Database Engine ---")
engine = create_engine(f"postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}")
print(f"Connected to '{DB_NAME}' server successfully.\n" + "="*50)

# Dictionary mapping clean CSV files to target Postgres tables
tables_to_load = {
    "customers_clean.csv": "clean_customers",
    "orders_clean.csv": "clean_orders",
    "payments_clean.csv": "clean_payments",
    "order_items_clean.csv": "clean_order_items",
    "reviews_clean.csv": "clean_reviews"
}


# 3. Stream and Load Clean Dataframes (ETL: Load Phase)
print("--- Step 3: Launching Table Ingestion Pipeline ---")

for file_name, table_name in tables_to_load.items():
    file_url = os.path.join(cleaned_data_path, file_name)
    
    if os.path.exists(file_url):
        print(f"Reading {file_name} from local storage...")
        df = pd.read_csv(file_url)
        
        print(f"Streaming {df.shape[0]} rows into database table '{table_name}'...")
        # to_sql drops the old table schema and rebuilds it automatically
        df.to_sql(name=table_name, con=engine, if_exists="replace", index=False)
        print(f"Table '{table_name}' successfully loaded.")
    else:
        print(f"Warning: Cleaned file {file_name} not found in path. Skipping.")
        
    print("-" * 40)

print("\n--- Success! All data pipelines have settled cleanly in PostgreSQL ---")