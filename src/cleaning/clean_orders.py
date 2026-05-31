import os
import pandas as pd


# 1. Define file path
file_path = r"C:\Users\Amir\Documents\GitHub\Olist-Churn-CLV-Analytics\data\raw\olist_orders_dataset.csv"

print("--- Loading Orders Dataset ---")
orders = pd.read_csv(file_path)
print(f"Dataset loaded successfully. Initial shape: {orders.shape}\n")


# 2. Initial Data Inspection
print("--- df.info() Output ---")
print(orders.info())
print("\n" + "=" * 50 + "\n")

print("--- Missing Values per Column (Before Cleaning) ---")
print(orders.isnull().sum())
print("\n" + "=" * 50 + "\n")


# 3. Convert Date Columns to Datetime
print("--- Converting Date Columns to Datetime Objects ---")
date_cols = [
    "order_purchase_timestamp",
    "order_approved_at",
    "order_delivered_carrier_date",
    "order_delivered_customer_date",
    "order_estimated_delivery_date"
]

for col in date_cols:
    orders[col] = pd.to_datetime(
        orders[col],
        errors="coerce"
    )

print("Date conversion completed.")
print("\n" + "=" * 50 + "\n")


# 4. Filter for Valid/Real Orders (Delivered Only)
print("--- Filtering for Real/Delivered Orders ---")
print(f"Value counts of order_status before filtering:\n{orders['order_status'].value_counts()}")

orders = orders[orders["order_status"].isin(["delivered"])]

print(f"\nShape after filtering for 'delivered' status: {orders.shape}")
print("\n" + "=" * 50 + "\n")


# 5. Handle Duplicate Records
print("--- Checking for Duplicate Rows ---")
duplicate_count = orders.duplicated().sum()
print(f"Total duplicate rows found: {duplicate_count}")

if duplicate_count > 0:
    orders = orders.drop_duplicates()
    print("Duplicate rows dropped successfully.")
else:
    print("No duplicate rows detected.")
print("\n" + "=" * 50 + "\n")


# 6. Final Inspection
print("--- Missing Values per Column (After Filtering) ---")
print(orders.isnull().sum())
print("\n" + "=" * 50 + "\n")

print("--- Cleaned Orders Sample (First 5 Rows) ---")
print(orders.head())