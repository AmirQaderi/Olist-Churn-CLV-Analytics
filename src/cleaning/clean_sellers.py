import os
import pandas as pd


# 1. Define file path
file_path = r"C:\Users\Amir\Documents\GitHub\Olist-Churn-CLV-Analytics\data\raw\olist_sellers_dataset.csv"

print("--- Loading Sellers Dataset ---")
sellers = pd.read_csv(file_path)
print(f"Dataset loaded successfully. Initial shape: {sellers.shape}\n")


# 2. Initial Data Inspection
print("--- df.info() Output ---")
print(sellers.info())
print("\n" + "=" * 50 + "\n")


# 3. Handle Duplicate Records
print("--- Checking for Duplicate Rows ---")
duplicate_count = sellers.duplicated().sum()
print(f"Total duplicate rows found: {duplicate_count}")

if duplicate_count > 0:
    sellers = sellers.drop_duplicates()
    print("Duplicate rows dropped successfully.")
else:
    print("No duplicate rows detected.")
print("\n" + "=" * 50 + "\n")


# 4. Text Standardization (City and State)
print("--- Standardizing Seller City Names ---")

# Lowercase and strip whitespace from city profiles
sellers["seller_city"] = (
    sellers["seller_city"].str.lower().str.strip()
)

# Capitalize state codes just in case to maintain consistency
sellers["seller_state"] = sellers["seller_state"].str.upper()

print("Text standardization completed successfully.")
print("\n" + "=" * 50 + "\n")


# 5. Final Inspection
print("--- Cleaned Sellers Sample (First 5 Rows) ---")
print(sellers.head())