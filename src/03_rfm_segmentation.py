import os
import pandas as pd

# Define dynamic relative paths to guarantee workspace consistency
base_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
input_file = os.path.join(base_path, "data", "analytics", "customer_analytics.csv")
output_file = os.path.join(base_path, "data", "analytics", "rfm_table.csv")

# 1. Load Customer Analytics Matrix
print("--- Step 3.1: Loading Customer Analytics Data ---")
if not os.path.exists(input_file):
    raise FileNotFoundError(f"Required base file not found at: {input_file}")

df = pd.read_csv(input_file)
print(f"Loaded dataset with shape: {df.shape}")

# 2. Engineer Recency (R) Score
print("--- Step 3.2: Computing Recency (R) Scores ---")
df["R"] = pd.qcut(
    df["recency_days"],
    q=5,
    labels=[5, 4, 3, 2, 1]
)

# 3. Engineer Frequency (F) Score using explicit Business Logic Mapping
print("--- Step 3.3: Computing Frequency (F) Scores via Manual Mapping ---")
def map_frequency_score(orders):
    if orders == 1:
        return 1
    elif orders == 2:
        return 2
    elif orders == 3:
        return 3
    elif orders == 4:
        return 4
    else:
        return 5

df["F"] = df["total_orders"].apply(map_frequency_score)

# 4. Engineer Monetary (M) Score
print("--- Step 3.4: Computing Monetary (M) Scores ---")
df["M"] = pd.qcut(
    df["total_spent"],
    q=5,
    labels=[1, 2, 3, 4, 5]
)

# 5. Construct Final Combined RFM String Score
print("--- Step 3.5: Generating Combined RFM_SCORE ---")
df["RFM_SCORE"] = (
    df["R"].astype(str) +
    df["F"].astype(str) +
    df["M"].astype(str)
)

# 6. Export Segmented Output Table
print("--- Step 3.6: Exporting Final RFM Table ---")
df.to_csv(output_file, index=False)

print(f"\n RFM Segmentation Complete! Output saved to:\n{output_file}")
print("\nSample of generated scores:")
print(df[["customer_unique_id", "recency_days", "total_orders", "total_spent", "R", "F", "M", "RFM_SCORE"]].head())