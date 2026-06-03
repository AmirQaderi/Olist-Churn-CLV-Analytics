import os
import pandas as pd

# Define dynamic workspace paths
base_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
input_file = os.path.join(base_path, "data", "analytics", "customer_analytics.csv")
output_file = os.path.join(base_path, "data", "analytics", "churn_dataset.csv")

# Load base analytics table
print("--- Step 4.1 & 4.2: Loading Customer Analytics Data ---")
df = pd.read_csv(input_file)

# Step 4.4: Create Target Variable (Churn defined as Recency > 90 days)
print("--- Step 4.4: Engineering Target Churn Variable ---")
df["churn"] = (df["recency_days"] > 90).astype(int)

# Step 4.5: Class Distribution Analysis
print("--- Step 4.5: Class Distribution Percentages ---")
counts = df["churn"].value_counts()
percentages = df["churn"].value_counts(normalize=True) * 100
for cls, pct in percentages.items():
    print(f"Class {cls}: {counts[cls]} profiles ({pct:.2f}%)")

# Step 4.6: Dropping Unnecessary ID and Leakage Identification Columns
print("--- Step 4.6: Cleaning Matrix for Machine Learning Ingestion ---")
# Critically dropping recency_days here to avoid perfect data leakage
drop_cols = ["customer_unique_id", "last_purchase", "recency_days"]
df_model = df.drop(columns=drop_cols)

# Step 4.7: Export Clean ML Ready Dataset
print("--- Step 4.7: Exporting Final Churn Dataset ---")
df_model.to_csv(output_file, index=False)

print(f"\n Churn dataset successfully created! Matrix shape: {df_model.shape}")
print(f"Output saved to: {output_file}")