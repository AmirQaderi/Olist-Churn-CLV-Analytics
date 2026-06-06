import os
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler  # Added for feature scaling
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.metrics import roc_auc_score

# Define dynamic workspace paths
base_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
dataset_file = os.path.join(base_path, "data", "analytics", "churn_dataset.csv")
original_analytics_file = os.path.join(base_path, "data", "analytics", "customer_analytics.csv")
output_prediction_file = os.path.join(base_path, "data", "analytics", "churn_predictions.csv")

# Step 5.1: Load Training Matrix
print("--- Step 5.1: Loading ML Ready Churn Dataset ---")
df = pd.read_csv(dataset_file).fillna(0)

# Step 5.2: Define Features and Target
print("--- Step 5.2: Splitting Features (X) and Target (y) ---")
X = df.drop(columns=["churn"])
y = df["churn"]

# Step 5.3: Train/Test Stratified Split
print("--- Step 5.3: Performing Stratified Train/Test Split ---")
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# --- NEW: Scale Features to prevent model bias and extreme probabilities ---
print("--- Scaling Features for Logistic Regression Stability ---")
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)
X_all_scaled = scaler.transform(X)  # For predicting the whole dataset safely
# --------------------------------------------------------------------------

# Step 5.4: Model Training on Scaled Data
print("--- Step 5.4: Fitting Logistic Regression Model on Scaled Data ---")
model = LogisticRegression(max_iter=1000, random_state=42)
model.fit(X_train_scaled, y_train)

# Step 5.5 & 5.6: Predict & Evaluate Model
print("--- Step 5.5 & 5.6: Evaluating Model Performance ---")
y_pred = model.predict(X_test_scaled)
print("\nClassification Report:")
print(classification_report(y_test, y_pred))

# Step 5.7: Calculate ROC-AUC score based on predicted probabilities
auc_score = roc_auc_score(y_test, model.predict_proba(X_test_scaled)[:, 1])
print(f"ROC-AUC Score: {auc_score:.4f}")

# Step 5.8: Generate Churn Probabilities Matrix safely using Scaled Features
print("--- Step 5.8: Mapping Scaled Churn Probabilities back to Profiles ---")
original_df = pd.read_csv(original_analytics_file)

original_df["churn_probability"] = model.predict_proba(X_all_scaled)[:, 1]
original_df["churn_predicted_label"] = model.predict(X_all_scaled)

# Step 5.9: Export Predictive Scores Matrix
print("--- Step 5.9: Saving Output Predictions File ---")
original_df.to_csv(output_prediction_file, index=False)
print(f" Optimized predictions saved to:\n{output_prediction_file}")