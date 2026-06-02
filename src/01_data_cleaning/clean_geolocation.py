import os
import pandas as pd


# 1. Define file path
file_path = r"C:\Users\Amir\Documents\GitHub\Olist-Churn-CLV-Analytics\data\raw\olist_geolocation_dataset.csv"

print("--- Loading Geolocation Dataset (Large File) ---")
geo = pd.read_csv(file_path)
print(f"Dataset loaded successfully. Initial shape: {geo.shape}\n")


# 2. Handle Duplicate Records (Crucial for a 1M+ row dataset)
print("--- Checking and Removing Duplicate Rows ---")
initial_rows = geo.shape[0]
geo = geo.drop_duplicates()
final_rows = geo.shape[0]

print(f"Rows before dropping duplicates: {initial_rows}")
print(f"Rows after dropping duplicates: {final_rows}")
print(f"Removed {initial_rows - final_rows} duplicate rows, optimizing memory.")
print("\n" + "=" * 50 + "\n")


# 3. Validate Geographical Coordinates
print("--- Validating Latitude and Longitude Boundaries ---")
# Latitude must be between -90 and 90 degrees
geo = geo[geo["geolocation_lat"].between(-90, 90)]

# Longitude must be between -180 and 180 degrees
geo = geo[geo["geolocation_lng"].between(-180, 180)]

print(f"Dataset shape after validating coordinate bounds: {geo.shape}")
print("\n" + "=" * 50 + "\n")


# 4. Text Standardization (City and State)
print("--- Standardizing Geolocation City Names ---")

# Lowercase and strip whitespace from city profiles
geo["geolocation_city"] = (
    geo["geolocation_city"].str.lower().str.strip()
)

# Capitalize state codes to keep format consistent
geo["geolocation_state"] = geo["geolocation_state"].str.upper()

print("Text standardization completed successfully.")
print("\n" + "=" * 50 + "\n")


# 5. Final Inspection
print("--- Cleaned Geolocation Sample (First 5 Rows) ---")
print(geo.head())