import os
import pandas as pd


# 1. Define file path
file_path = r"C:\Users\Amir\Documents\GitHub\Olist-Churn-CLV-Analytics\data\raw\product_category_name_translation.csv"

print("--- Loading Category Translation Dataset ---")
categories = pd.read_csv(file_path)
print(f"Dataset loaded successfully. Initial shape: {categories.shape}\n")


# 2. Initial Data Inspection
print("--- df.info() Output ---")
print(categories.info())
print("\n" + "=" * 50 + "\n")


# 3. Handle Duplicate Records
print("--- Checking for Duplicate Rows ---")
duplicate_count = categories.duplicated().sum()
print(f"Total duplicate rows found: {duplicate_count}")

if duplicate_count > 0:
    categories = categories.drop_duplicates()
    print("Duplicate rows dropped successfully.")
else:
    print("No duplicate rows detected.")
print("\n" + "=" * 50 + "\n")


# 4. Handle Missing Values (Nulls)
print("--- Checking and Removing Missing Translations ---")
null_count = categories.isnull().sum().sum()
print(f"Total missing value entries: {null_count}")

if null_count > 0:
    categories = categories.dropna()
    print(f"Dataset shape after dropping missing values: {categories.shape}")
else:
    print("No missing values detected in the translation map.")
print("\n" + "=" * 50 + "\n")


# 5. Final Inspection
print("--- Cleaned Categories Sample (First 5 Rows) ---")
print(categories.head())