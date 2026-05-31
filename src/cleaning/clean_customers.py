import os
import pandas as pd


# 1. Define file path
file_path = r"C:\Users\Amir\Documents\GitHub\Olist-Churn-CLV-Analytics\data\raw\olist_customers_dataset.csv"

print("--- Loading Dataset ---")
customers = pd.read_csv(file_path)
print(f"Dataset loaded successfully. Initial shape: {customers.shape}\n")


# 2. Initial Data Inspection
print("--- df.info() Output ---")
print(customers.info())
print("\n" + "=" * 50 + "\n")

print("--- Missing Values per Column ---")
print(customers.isnull().sum())
print("\n" + "=" * 50 + "\n")

print("--- Statistical Summary df.describe() ---")
print(customers.describe(include="all"))
print("\n" + "=" * 50 + "\n")



# 3. Handle Duplicate Records
print("--- Checking for Duplicate Rows ---")
duplicate_count = customers.duplicated().sum()
print(f"Total duplicate rows found: {duplicate_count}")

if duplicate_count > 0:
    customers = customers.drop_duplicates()
    print("Duplicate rows dropped successfully.")
else:
    print("No duplicate rows detected.")
print("\n" + "=" * 50 + "\n")


# 4. Text Standardization (City and State)
print("--- Standardizing Text Data ---")

# Strip whitespaces and convert city names to lowercase
customers["customer_city"] = (
    customers["customer_city"].str.strip().str.lower()
)

# Convert state abbreviations to uppercase
customers["customer_state"] = customers["customer_state"].str.upper()

print("Text standardization completed successfully.")
print("\n" + "=" * 50 + "\n")


# 5. Display Cleaned Sample
print("--- Cleaned Data Sample (First 5 Rows) ---")
print(customers.head())