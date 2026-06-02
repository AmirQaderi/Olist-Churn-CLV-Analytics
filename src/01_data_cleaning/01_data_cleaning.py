import os
import pandas as pd

# Define paths
raw_path = r"C:\Users\Amir\Documents\GitHub\Olist-Churn-CLV-Analytics\data\raw"
cleaned_path = r"C:\Users\Amir\Documents\GitHub\Olist-Churn-CLV-Analytics\data\cleaned"

# Ensure directory exists
os.makedirs(cleaned_path, exist_ok=True)

print("--- Starting Data Cleaning Pipeline ---")

# =====================================================================
# 1. CUSTOMERS
# =====================================================================
print("Processing Customers...")
customers = pd.read_csv(os.path.join(raw_path, "olist_customers_dataset.csv"))
customers = customers.drop_duplicates()
customers["customer_city"] = customers["customer_city"].str.strip().str.lower()
customers["customer_state"] = customers["customer_state"].str.upper()
customers.to_csv(os.path.join(cleaned_path, "customers_clean.csv"), index=False)

# =====================================================================
# 2. ORDERS
# =====================================================================
print("Processing Orders...")
orders = pd.read_csv(os.path.join(raw_path, "olist_orders_dataset.csv"))
date_cols = [
    "order_purchase_timestamp",
    "order_approved_at",
    "order_delivered_carrier_date",
    "order_delivered_customer_date",
    "order_estimated_delivery_date"
]
for col in date_cols:
    orders[col] = pd.to_datetime(orders[col], errors="coerce")

orders = orders[orders["order_status"].isin(["delivered"])]
orders = orders.drop_duplicates()
orders.to_csv(os.path.join(cleaned_path, "orders_clean.csv"), index=False)

# =====================================================================
# 3. PAYMENTS
# =====================================================================
print("Processing Payments...")
payments = pd.read_csv(os.path.join(raw_path, "olist_order_payments_dataset.csv"))
payments = payments[payments["payment_value"] > 0]
payments["payment_type"] = payments["payment_type"].str.lower()
payments = payments.drop_duplicates()
payments.to_csv(os.path.join(cleaned_path, "payments_clean.csv"), index=False)

# =====================================================================
# 4. ORDER ITEMS
# =====================================================================
print("Processing Order Items...")
items = pd.read_csv(os.path.join(raw_path, "olist_order_items_dataset.csv"))
items = items[items["price"] >= 0]
items = items[items["freight_value"] >= 0]
items["shipping_limit_date"] = pd.to_datetime(items["shipping_limit_date"], errors="coerce")
items = items.drop_duplicates()
items.to_csv(os.path.join(cleaned_path, "order_items_clean.csv"), index=False)

# =====================================================================
# 5. REVIEWS
# =====================================================================
print("Processing Reviews...")
reviews = pd.read_csv(os.path.join(raw_path, "olist_order_reviews_dataset.csv"))
reviews["review_creation_date"] = pd.to_datetime(reviews["review_creation_date"], errors="coerce")
reviews["review_answer_timestamp"] = pd.to_datetime(reviews["review_answer_timestamp"], errors="coerce")
reviews = reviews[reviews["review_score"].between(1, 5)]
reviews["review_comment_title"] = reviews["review_comment_title"].fillna("No Title")
reviews["review_comment_message"] = reviews["review_comment_message"].fillna("No Comment")
reviews = reviews.drop_duplicates()
reviews.to_csv(os.path.join(cleaned_path, "reviews_clean.csv"), index=False)

print("\n--- Data Cleaning Pipeline Finished Successfully! ---")
print(f"Cleaned files are saved in: {cleaned_path}")

# =====================================================================
# 6. PRODUCTS
# =====================================================================
print("Processing Products...")
products = pd.read_csv(os.path.join(raw_path, "olist_products_dataset.csv"))
products = products.drop_duplicates(subset=["product_id"])
# Fill missing category names with a placeholder to prevent missing rows in future joins
products["product_category_name"] = products["product_category_name"].fillna("unknown")
products.to_csv(os.path.join(cleaned_path, "products_clean.csv"), index=False)
print("products_clean.csv exported successfully.")