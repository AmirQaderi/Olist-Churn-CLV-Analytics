# Olist-Churn-CLV-Analytics
End-to-end e-commerce customer analytics project using the Olist Brazilian E-Commerce dataset. Built a churn prediction and Customer Lifetime Value (CLV) analysis pipeline with Python, SQL, PostgreSQL, scikit-learn, and Power BI. Includes RFM segmentation, feature engineering, machine learning models, KPI dashboards, and business-focused customer retention insights.
## License
This project is licensed under the MIT License.

```
Olist-Churn-CLV-Analytics
├─ dashboard
│  ├─ Olist_Churn_CLV.pbix
│  └─ screenshots
│     ├─ 1. executive_overview.png
│     ├─ 2. churn_analysis.png
│     ├─ 3. rfm_analysis.png
│     └─ 4. clv_analysis.png
├─ data
│  ├─ analytics
│  │  ├─ churn_dataset.csv
│  │  ├─ churn_predictions.csv
│  │  ├─ clv_dataset.csv
│  │  ├─ customer_analytics.csv
│  │  └─ rfm_table.csv
│  ├─ cleaned
│  │  ├─ customers_clean.csv
│  │  ├─ orders_clean.csv
│  │  ├─ order_items_clean.csv
│  │  ├─ payments_clean.csv
│  │  ├─ products_clean.csv
│  │  └─ reviews_clean.csv
│  ├─ olist_customers_dataset.csv
│  ├─ olist_geolocation_dataset.csv
│  ├─ olist_orders_dataset.csv
│  ├─ olist_order_items_dataset.csv
│  ├─ olist_order_payments_dataset.csv
│  ├─ olist_order_reviews_dataset.csv
│  ├─ olist_products_dataset.csv
│  ├─ olist_sellers_dataset.csv
│  ├─ powerbi
│  │  └─ powerbi_dataset.csv
│  ├─ product_category_name_translation.csv
│  └─ raw
│     ├─ olist_customers_dataset.csv
│     ├─ olist_geolocation_dataset.csv
│     ├─ olist_orders_dataset.csv
│     ├─ olist_order_items_dataset.csv
│     ├─ olist_order_payments_dataset.csv
│     ├─ olist_order_reviews_dataset.csv
│     ├─ olist_products_dataset.csv
│     ├─ olist_sellers_dataset.csv
│     └─ product_category_name_translation.csv
├─ LICENSE
├─ README.md
├─ sql
│  └─ database_load.py
└─ src
   ├─ 01_data_cleaning
   │  ├─ 01_data_cleaning.py
   │  ├─ clean_categories.py
   │  ├─ clean_customers.py
   │  ├─ clean_geolocation.py
   │  ├─ clean_orders.py
   │  ├─ clean_order_items.py
   │  ├─ clean_payments.py
   │  ├─ clean_products.py
   │  ├─ clean_reviews.py
   │  └─ clean_sellers.py
   ├─ 02_feature_engineering.py
   ├─ 03_rfm_segmentation.py
   ├─ 04_churn_dataset_creation.py
   ├─ 05_churn_model.py
   ├─ 06_clv_analysis.py
   └─ 07_powerbi_export.py

```
```
Olist-Churn-CLV-Analytics
├─ dashboard
│  ├─ Olist_Churn_CLV.pbix
│  └─ screenshots
│     ├─ 1. executive_overview.png
│     ├─ 2. churn_analysis.png
│     ├─ 3. rfm_analysis.png
│     └─ 4. clv_analysis.png
├─ data
├─ LICENSE
├─ README.md
├─ sql
│  └─ database_load.py
└─ src
   ├─ 01_data_cleaning
   │  ├─ 01_data_cleaning.py
   │  ├─ clean_categories.py
   │  ├─ clean_customers.py
   │  ├─ clean_geolocation.py
   │  ├─ clean_orders.py
   │  ├─ clean_order_items.py
   │  ├─ clean_payments.py
   │  ├─ clean_products.py
   │  ├─ clean_reviews.py
   │  └─ clean_sellers.py
   ├─ 02_feature_engineering.py
   ├─ 03_rfm_segmentation.py
   ├─ 04_churn_dataset_creation.py
   ├─ 05_churn_model.py
   ├─ 06_clv_analysis.py
   └─ 07_powerbi_export.py

```