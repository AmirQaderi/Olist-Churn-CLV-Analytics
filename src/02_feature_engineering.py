import os
import pandas as pd

# Define dynamic relative paths to avoid directory location mismatch
base_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
clean_data_path = os.path.join(base_path, "data", "cleaned")
output_path = os.path.join(base_path, "data", "analytics")

# Ensure target directory exists
os.makedirs(output_path, exist_ok=True)

# Step 1.1: Load Cleaned Files
print("--- Step 1.1: Loading Cleaned Datasets ---")
customers = pd.read_csv(os.path.join(clean_data_path, "customers_clean.csv"))
orders = pd.read_csv(os.path.join(clean_data_path, "orders_clean.csv"))
payments = pd.read_csv(os.path.join(clean_data_path, "payments_clean.csv"))
items = pd.read_csv(os.path.join(clean_data_path, "order_items_clean.csv"))
reviews = pd.read_csv(os.path.join(clean_data_path, "reviews_clean.csv"))
products = pd.read_csv(os.path.join(clean_data_path, "products_clean.csv"))

# Step 1.2: Convert Timestamps
print("--- Step 1.2: Converting Timestamps into Datetime Objects ---")
date_cols = [
    "order_purchase_timestamp",
    "order_delivered_customer_date",
    "order_estimated_delivery_date"
]
for col in date_cols:
    orders[col] = pd.to_datetime(orders[col])

# Step 1.3: Create Delivery Features
print("--- Step 1.3: Engineering Logistic Delivery Features ---")
orders["delivery_days"] = (
    orders["order_delivered_customer_date"] - orders["order_purchase_timestamp"]
).dt.days

orders["delivery_delay"] = (
    orders["order_delivered_customer_date"] - orders["order_estimated_delivery_date"]
).dt.days

orders["late_delivery"] = (orders["delivery_delay"] > 0).astype(int)

# Step 1.4: Calculate Actual Values per Order
print("--- Step 1.4: Aggregating Pure Financial Values per Order ---")
order_values = (
    items.groupby("order_id")
    .agg(
        total_price=("price", "sum"),
        total_freight=("freight_value", "sum")
    )
    .reset_index()
)

# Step 1.5: Calculate Average Review Score
print("--- Step 1.5: Aggregating Review Scores per Order ---")
reviews_summary = (
    reviews.groupby("order_id")
    .agg(
        avg_review_score=("review_score", "mean")
    )
    .reset_index()
)

# Step 1.6: Build Enriched Orders Table
print("--- Step 1.6: Enriched Orders Table Merge Sequence ---")
orders_enriched = (
    orders
    .merge(order_values, on="order_id", how="left")
    .merge(payments, on="order_id", how="left")
    .merge(reviews_summary, on="order_id", how="left")
)

# Step 1.7: Connect Customer Dimensions
print("--- Step 1.7: Joining Customer Information to Enriched Table ---")
orders_enriched = (
    orders_enriched
    .merge(customers, on="customer_id", how="left")
)

# Step 1.8: Construct Customer Analytics Table
print("--- Step 1.8: Creating Core Customer Profiles GroupBy Summary ---")
snapshot_date = orders_enriched["order_purchase_timestamp"].max()

customer_analytics = (
    orders_enriched
    .groupby("customer_unique_id")
    .agg(
        total_orders=("order_id", "nunique"),
        total_spent=("payment_value", "sum"),
        avg_order_value=("payment_value", "mean"),
        avg_review_score=("avg_review_score", "mean"),
        avg_delivery_days=("delivery_days", "mean"),
        late_delivery_rate=("late_delivery", "mean"),
        last_purchase=("order_purchase_timestamp", "max")
    )
    .reset_index()
)

# Step 1.9: Calculate Recency
print("--- Step 1.9: Engineering Recency Metric Days ---")
customer_analytics["recency_days"] = (
    snapshot_date - customer_analytics["last_purchase"]
).dt.days

# Fill potential missing values resulting from structural outer joins for model stability
customer_analytics["avg_review_score"] = customer_analytics["avg_review_score"].fillna(customer_analytics["avg_review_score"].mean())
customer_analytics["avg_delivery_days"] = customer_analytics["avg_delivery_days"].fillna(customer_analytics["avg_delivery_days"].median())
customer_analytics["late_delivery_rate"] = customer_analytics["late_delivery_rate"].fillna(0)

# Step 1.10: Export Final Analytics Dataset
print("--- Step 1.10: Exporting Output File ---")
output_file = os.path.join(output_path, "customer_analytics.csv")
customer_analytics.to_csv(output_file, index=False)

print(f"\n Pipeline Executed Successfully! Matrix saved to:\n{output_file}")
print(f"Final customer dataset dimensions for Machine Learning modeling: {customer_analytics.shape}")