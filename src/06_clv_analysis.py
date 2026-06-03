import os
import pandas as pd

# Define dynamic relative paths for workspace consistency
base_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
analytics_path = os.path.join(base_path, "data", "analytics")

input_file = os.path.join(analytics_path, "customer_analytics.csv")
churn_file = os.path.join(analytics_path, "churn_predictions.csv")
output_file = os.path.join(analytics_path, "clv_dataset.csv")

# Step 6.1 & 6.2: Load Data & Inspect Columns
print("--- Step 6.1: Loading Customer Analytics Data ---")
if not os.path.exists(input_file):
    raise FileNotFoundError(f"Missing required base file: {input_file}")
df = pd.read_csv(input_file)

# Step 6.3: Create Purchase Frequency Metric
print("--- Step 6.3: Engineering Purchase Frequency ---")
df["purchase_frequency"] = df["total_orders"]

# Step 6.4 & 6.5: Calculate Customer Lifespan & Clip Lower Bound
print("--- Step 6.4 & 6.5: Computing Customer Lifespan ---")
df["customer_lifespan"] = 365 - df["recency_days"]
df["customer_lifespan"] = df["customer_lifespan"].clip(lower=1)

# Step 6.6: Compute Customer Lifetime Value (CLV Formulation)
print("--- Step 6.6: Calculating CLV Scores ---")
df["clv"] = (
    df["avg_order_value"] * df["purchase_frequency"] * (df["customer_lifespan"] / 365)
)

# Step 6.7: Quantile-based CLV Segmentation for Power BI
print("--- Step 6.7: Applying Quantile-based CLV Segmentation ---")
high_cutoff = df["clv"].quantile(0.75)
medium_cutoff = df["clv"].quantile(0.50)

def assign_clv_segment(clv_value):
    if clv_value >= high_cutoff:
        return "High Value"
    elif clv_value >= medium_cutoff:
        return "Medium Value"
    else:
        return "Low Value"

df["clv_segment"] = df["clv"].apply(assign_clv_segment)

# Step 6.8: Merge CLV Matrix with ML Churn Predictions
print("--- Step 6.8: Merging CLV Matrix with Churn Probability Scores ---")
if not os.path.exists(churn_file):
    raise FileNotFoundError(f"Missing required prediction file: {churn_file}. Please run 05_churn_model.py first.")

churn_df = pd.read_csv(churn_file)

# Merge only the specific target identifiers and probabilities
final_df = df.merge(
    churn_df[["customer_unique_id", "churn_probability"]],
    on="customer_unique_id",
    how="left"
)
# Safe fill for any unmatched profiles
final_df["churn_probability"] = final_df["churn_probability"].fillna(0)

# Step 6.9: Build Business Action Segments (High CLV + High Risk)
print("--- Step 6.9: Mapping Business Action Segments ---")
def assign_action_segment(row):
    if row["clv_segment"] == "High Value" and row["churn_probability"] > 0.7:
        return "Retention Priority"
    elif row["clv_segment"] == "High Value":
        return "VIP Customer"
    else:
        return "Normal Customer"

final_df["action_segment"] = final_df.apply(assign_action_segment, axis=1)

# Step 6.10: Export Final CLV Analytics Table
print("--- Step 6.10: Exporting Final Combined CLV Dataset ---")
final_df.to_csv(output_file, index=False)

print(f"\n CLV Ingestion & Segmentation Pipeline Complete!")
print(f"Final analytical dataset dimensions: {final_df.shape}")
print(f"Matrix successfully exported to: {output_file}")

print("\nAction Segment Breakdown Counts:")
print(final_df["action_segment"].value_counts())