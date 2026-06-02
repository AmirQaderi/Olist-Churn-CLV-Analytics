import os
import pandas as pd


# 1. Define file path
file_path = r"C:\Users\Amir\Documents\GitHub\Olist-Churn-CLV-Analytics\data\raw\olist_order_items_dataset.csv"

print("--- Loading Order Items Dataset ---")
items = pd.read_csv(file_path)
print(f"Dataset loaded successfully. Initial shape: {items.shape}\n")


# 2. Initial Data Inspection
print("--- df.info() Output ---")
print(items.info())
print("\n" + "=" * 50 + "\n")


# 3. Handle Negative Price and Freight Values
print("--- Checking and Filtering Price & Freight Values ---")
negative_price = (items["price"] < 0).sum()
negative_freight = (items["freight_value"] < 0).sum()

print(f"Number of rows with negative price: {negative_price}")
print(f"Number of rows with negative freight_value: {negative_freight}")

# Filter out negative pricing/shipping components
if negative_price > 0:
    items = items[items["price"] >= 0]
    
if negative_freight > 0:
    items = items[items["freight_value"] >= 0]

print(f"Dataset shape after filtering economic variables: {items.shape}")
print("\n" + "=" * 50 + "\n")


# 4. Convert Date Column to Datetime
print("--- Converting shipping_limit_date to Datetime Objects ---")
items["shipping_limit_date"] = pd.to_datetime(
    items["shipping_limit_date"],
    errors="coerce"
)
print("Date conversion completed.")
print("\n" + "=" * 50 + "\n")


# 5. Handle Duplicate Records
print("--- Checking for Duplicate Rows ---")
duplicate_count = items.duplicated().sum()
print(f"Total duplicate rows found: {duplicate_count}")

if duplicate_count > 0:
    items = items.drop_duplicates()
    print("Duplicate rows dropped successfully.")
else:
    print("No duplicate rows detected.")
print("\n" + "=" * 50 + "\n")


# 6. Final Inspection
print("--- Cleaned Order Items Sample (First 5 Rows) ---")
print(items.head())