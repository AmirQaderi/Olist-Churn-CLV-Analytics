import os
import pandas as pd

# Define dynamic relative paths for workspace consistency
base_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
analytics_path = os.path.join(base_path, "data", "analytics")
output_path = os.path.join(base_path, "data", "powerbi")

# Ensure target powerbi directory exists
os.makedirs(output_path, exist_ok=True)

# Step 7.1: Load Analytics Artifacts
print("--- Step 7.1: Loading Analytics Tables ---")
rfm = pd.read_csv(os.path.join(analytics_path, "rfm_table.csv"))
clv = pd.read_csv(os.path.join(analytics_path, "clv_dataset.csv"))

# Step 7.2: Verify Shared Identifier Key
print("--- Step 7.2: Verifying Primary Key Columns ---")
print(f"RFM Columns Has ID: {'customer_unique_id' in rfm.columns}")
print(f"CLV Columns Has ID: {'customer_unique_id' in clv.columns}")

# Step 7.3 & 7.4: Direct Merge (Bring RFM scores into the master CLV dataset)
print("--- Step 7.3 & 7.4: Merging RFM Scores into Master CLV Dataset ---")
rfm_subset = rfm[["customer_unique_id", "R", "F", "M", "RFM_SCORE"]]

# Merge rfm scores directly. clv already contains churn_probability natively!
powerbi_data = clv.merge(rfm_subset, on="customer_unique_id", how="left")

# Step 7.5: Engineer Risk Level Categorical KPI
print("--- Step 7.5: Engineering Risk Level Segmentation ---")
def assign_risk_level(prob):
    if prob >= 0.8:
        return "High Risk"
    elif prob >= 0.5:
        return "Medium Risk"
    else:
        return "Low Risk"

powerbi_data["risk_level"] = powerbi_data["churn_probability"].apply(assign_risk_level)

# Step 7.6: Engineer Financial 'Revenue At Risk' Metric
print("--- Step 7.6: Calculating Revenue At Risk Feature ---")
powerbi_data["revenue_at_risk"] = powerbi_data["clv"] * powerbi_data["churn_probability"]

# Step 7.7: Engineer VIP Customer Flag Indicator
print("--- Step 7.7: Mapping VIP Identification Flags ---")
powerbi_data["vip_flag"] = (powerbi_data["clv_segment"] == "High Value").astype(int)

# Step 7.8: Engineer Retention Priority Focus Flag
print("--- Step 7.8: Creating Strategic Retention Priority Flag ---")
powerbi_data["retention_priority"] = (
    (powerbi_data["clv_segment"] == "High Value") & 
    (powerbi_data["churn_probability"] > 0.7)
).astype(int)

# Step 7.9: Final Quality Assurance Imputation Check
print("--- Step 7.9: Checking and Imputing Missing Values ---")
for col in powerbi_data.columns:
    if powerbi_data[col].dtype == "object":
        powerbi_data[col] = powerbi_data[col].fillna("Unknown")
    else:
        powerbi_data[col] = powerbi_data[col].fillna(0)

# Step 7.10: Export Power BI Master Dataset
print("--- Step 7.10: Exporting Master Power BI Dataset ---")
output_file = os.path.join(output_path, "powerbi_dataset.csv")
powerbi_data.to_csv(output_file, index=False)

print(f"\n Power BI Data Export Pipeline Executed Successfully!")
print(f"Final Dashboard Dataset Location:\n{output_file}")
print(f"Dataset Matrix Dimensions: {powerbi_data.shape}")