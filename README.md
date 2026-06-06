# Olist E-Commerce Churn Prediction & Customer Lifetime Value Analytics

An end-to-end Data Analytics project that combines customer segmentation, churn prediction, and customer lifetime value (CLV) analysis using the Olist Brazilian E-Commerce dataset.

The project demonstrates the complete analytics workflow:

- Data Cleaning & Transformation
- PostgreSQL Data Loading
- Feature Engineering
- RFM Customer Segmentation
- Customer Churn Prediction
- CLV Analysis
- Interactive Power BI Dashboards

## Project Overview

Customer retention is one of the most important challenges in e-commerce. Identifying customers who are likely to stop purchasing and understanding their long-term value can significantly improve marketing effectiveness and revenue growth.

This project builds a complete analytics solution that transforms raw transactional data into actionable business insights. Using Python, PostgreSQL, Machine Learning, and Power BI, the solution helps identify:

- Customers with high churn risk
- High-value customer segments
- Revenue at risk
- Customer lifetime value distribution
- Retention priorities

## Business Problem

E-commerce companies often struggle to answer key questions:

- Which customers are most likely to churn?
- Which customers generate the highest long-term value?
- How should retention efforts be prioritized?
- Where is potential revenue at risk?

This project addresses these challenges through predictive analytics and customer segmentation techniques that support data-driven retention strategies.

## Tech Stack

### Programming Language
- Python 3.x

### Data Processing & Analytics
- Pandas
- NumPy

### Database & Data Warehousing
- PostgreSQL
- SQLAlchemy
- psycopg2

### Data Engineering
- ETL Pipeline Development
- Data Cleaning & Transformation
- Feature Engineering

### Machine Learning
- Scikit-Learn
- Logistic Regression
- Customer Churn Prediction

### Customer Analytics
- RFM Segmentation
- Customer Lifetime Value (CLV) Analysis

### Business Intelligence & Visualization
- Power BI
- DAX
- Interactive Dashboards

### Configuration & Environment Management
- Python-Dotenv

### File Handling
- OpenPyXL

### Version Control
- Git
- GitHub

## Project Structure

```text
dashboard/   → Power BI dashboard screenshots
data/        → Raw, cleaned, and analytical datasets
sql/         → PostgreSQL data loading scripts
src/         → Data processing and machine learning pipeline
README.md    → Project documentation
```

## Key Features

### Data Cleaning
Cleaned and standardized multiple relational tables from the Olist marketplace dataset.

### Customer Analytics Dataset
Built a unified customer-level analytical dataset by combining transactional, payment, and behavioral information.

### RFM Segmentation
Segmented customers using Recency, Frequency, and Monetary metrics to identify behavioral groups.

### Churn Prediction
Developed a machine learning model to estimate customer churn probability.

### Customer Lifetime Value Analysis
Calculated customer value metrics and identified high-value customer segments.

### Power BI Dashboard
Designed interactive dashboards for churn analysis, customer segmentation, and CLV monitoring.

## Dashboard Preview

### Executive Overview

![Executive Overview](dashboard/screenshots/1.%20executive_overview.png)

### Churn Analysis

![Churn Analysis](dashboard/screenshots/2.%20churn_analysis.png)

### RFM Segmentation

![RFM Analysis](dashboard/screenshots/3.%20rfm_analysis.png)

### CLV Analysis

![CLV Analysis](dashboard/screenshots/4.%20clv_analysis.png)

## Results

The project provides:

- Customer-level churn probability scores
- RFM-based customer segmentation
- Customer lifetime value analysis
- Revenue-at-risk visibility
- Interactive Power BI reporting for business stakeholders

These insights can support retention campaigns, customer prioritization, and marketing decision-making.

## Resume Highlights

- Built an end-to-end customer analytics solution using Python, PostgreSQL, and Power BI.
- Developed an RFM-based customer segmentation framework for behavioral analysis.
- Created a machine learning pipeline for customer churn prediction.
- Designed interactive Power BI dashboards for churn, CLV, and retention analytics.
- Automated data cleaning and database loading workflows using Python and SQLAlchemy.

## License

This project is distributed under the MIT License. See the LICENSE file for more information.