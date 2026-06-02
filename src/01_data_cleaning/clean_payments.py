import os
import pandas as pd


# 1. Define file path
file_path = r"C:\Users\Amir\Documents\GitHub\Olist-Churn-CLV-Analytics\data\raw\olist_order_payments_dataset.csv"

print("--- Loading Payments Dataset ---")
payments = pd.read_csv(file_path)
print(f"Dataset loaded successfully. Initial shape: {payments.shape}\n")


# 2. Initial Data Inspection
print("--- df.info() Output ---")
print(payments.info())
print("\n" + "=" * 50 + "\n")

print("--- Missing Values per Column ---")
print(payments.isnull().sum())
print("\n" + "=" * 50 + "\n")


# 3. Handle Negative and Zero Payment Values
print("--- Checking and Filtering Payment Values ---")
negative_count = (payments["payment_value"] < 0).sum()
zero_count = (payments["payment_value"] == 0).sum()

print(f"Number of rows with negative payment_value: {negative_count}")
print(f"Number of rows with zero payment_value: {zero_count}")

# Filter out both negative and zero values to keep only realistic transactions
if negative_count > 0 or zero_count > 0:
    payments = payments[payments["payment_value"] > 0]
    print(f"Filtered dataset shape (payment_value > 0): {payments.shape}")
else:
    print("No negative or zero values found in payment_value.")
print("\n" + "=" * 50 + "\n")


# 4. Text Standardization (Payment Type)
print("--- Standardizing Payment Type Column ---")
print(f"Unique payment types before: {payments['payment_type'].unique()}")

# Convert to lowercase
payments["payment_type"] = payments["payment_type"].str.lower()

print(f"Unique payment types after: {payments['payment_type'].unique()}")
print("\n" + "=" * 50 + "\n")


# 5. Handle Duplicate Records
print("--- Checking for Duplicate Rows ---")
duplicate_count = payments.duplicated().sum()
print(f"Total duplicate rows found: {duplicate_count}")

if duplicate_count > 0:
    payments = payments.drop_duplicates()
    print("Duplicate rows dropped successfully.")
else:
    print("No duplicate rows detected.")
print("\n" + "=" * 50 + "\n")


# 6. Final Inspection
print("--- Cleaned Payments Sample (First 5 Rows) ---")
print(payments.head())