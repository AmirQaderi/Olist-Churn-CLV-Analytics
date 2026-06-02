import os
import pandas as pd


# 1. Define file path
file_path = r"C:\Users\Amir\Documents\GitHub\Olist-Churn-CLV-Analytics\data\raw\olist_products_dataset.csv"

print("--- Loading Products Dataset ---")
products = pd.read_csv(file_path)
print(f"Dataset loaded successfully. Initial shape: {products.shape}\n")


# 2. Initial Data Inspection
print("--- df.info() Output ---")
print(products.info())
print("\n" + "=" * 50 + "\n")


# 3. Handle Invalid (Zero/Negative) and Missing Physical Metrics
dimension_cols = [
    "product_weight_g",
    "product_length_cm",
    "product_height_cm",
    "product_width_cm"
]

print("--- Filtering and Imputing Physical Dimensions ---")
for col in dimension_cols:
    # Count anomalies before cleaning
    invalid_count = (products[col] <= 0).sum()
    missing_count = products[col].isnull().sum()
    print(f"Column '{col}' -> Invalid (<=0): {invalid_count} | Missing (NaN): {missing_count}")
    
    # Filter out rows where the metric is explicitly 0 or negative
    products = products[(products[col] > 0) | (products[col].isnull())]
    
    # Impute remaining missing values using the column's median
    col_median = products[col].median()
    products[col] = products[col].fillna(col_median)

print("\nFiltering and median imputation completed.")
print("\n" + "=" * 50 + "\n")


# 4. Handle Duplicate Products based on product_id
print("--- Dropping Duplicate Products ---")
initial_rows = products.shape[0]
products = products.drop_duplicates(subset=["product_id"])
final_rows = products.shape[0]

print(f"Rows before dropping duplicates: {initial_rows}")
print(f"Rows after dropping duplicates: {final_rows}")
print(f"Removed {initial_rows - final_rows} duplicate product rows.")
print("\n" + "=" * 50 + "\n")


# 5. Final Verification of Imputed Columns
print("--- Missing Values Verification ---")
print(products[dimension_cols].isnull().sum())
print("\n" + "=" * 50 + "\n")

print("--- Cleaned Products Sample (First 5 Rows) ---")
print(products.head())