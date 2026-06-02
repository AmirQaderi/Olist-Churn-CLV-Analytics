import os
import pandas as pd


# 1. Define file path
file_path = r"C:\Users\Amir\Documents\GitHub\Olist-Churn-CLV-Analytics\data\raw\olist_order_reviews_dataset.csv"

print("--- Loading Reviews Dataset ---")
reviews = pd.read_csv(file_path)
print(f"Dataset loaded successfully. Initial shape: {reviews.shape}\n")


# 2. Initial Data Inspection
print("--- df.info() Output ---")
print(reviews.info())
print("\n" + "=" * 50 + "\n")


# 3. Convert Date Columns to Datetime Objects
print("--- Converting Date Columns to Datetime Objects ---")
reviews["review_creation_date"] = pd.to_datetime(
    reviews["review_creation_date"], 
    errors="coerce"
)
reviews["review_answer_timestamp"] = pd.to_datetime(
    reviews["review_answer_timestamp"], 
    errors="coerce"
)
print("Date conversion completed.")
print("\n" + "=" * 50 + "\n")


# 4. Handle Out-of-Bounds Review Scores
print("--- Validating Review Scores (1-5) ---")
invalid_scores = (~reviews["review_score"].between(1, 5)).sum()
print(f"Number of rows with scores outside the 1-5 range: {invalid_scores}")

if invalid_scores > 0:
    reviews = reviews[reviews["review_score"].between(1, 5)]
    print(f"Dataset shape after validating scores: {reviews.shape}")
else:
    print("All review scores are within the acceptable 1-5 range.")
print("\n" + "=" * 50 + "\n")


# 5. Handle Missing Text Data (Imputation)
print("--- Imputing Missing Titles and Messages ---")
missing_title_count = reviews["review_comment_title"].isnull().sum()
missing_message_count = reviews["review_comment_message"].isnull().sum()

print(f"Missing values before - Title: {missing_title_count}, Message: {missing_message_count}")

# Replace NaN values with generic placeholders
reviews["review_comment_title"] = reviews["review_comment_title"].fillna("No Title")
reviews["review_comment_message"] = reviews["review_comment_message"].fillna("No Comment")

print(f"Missing values after - Title: {reviews['review_comment_title'].isnull().sum()}, Message: {reviews['review_comment_message'].isnull().sum()}")
print("\n" + "=" * 50 + "\n")


# 6. Handle Duplicate Records
print("--- Checking for Duplicate Rows ---")
duplicate_count = reviews.duplicated().sum()
print(f"Total duplicate rows found: {duplicate_count}")

if duplicate_count > 0:
    reviews = reviews.drop_duplicates()
    print("Duplicate rows dropped successfully.")
else:
    print("No duplicate rows detected.")
print("\n" + "=" * 50 + "\n")


# 7. Final Inspection
print("--- Cleaned Reviews Sample (First 5 Rows) ---")
print(reviews.head())