#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 18 07:55:58 2026

@author: suraj
"""

import os

# Root project folder
root = "customer-360-data-platform"

folders = [
    "",
    "configs",
    "data/raw/customers",
    "data/raw/orders",
    "data/raw/payments",
    "data/raw/clickstream",
    "data/raw/support_tickets",
    "data/staging/customers",
    "data/staging/orders",
    "data/staging/payments",
    "data/staging/clickstream",
    "data/staging/support_tickets",
    "data/processed/parquet",
    "data/processed/csv",
    "data/curated/dim_tables",
    "data/curated/fact_tables",
    "notebooks",
    "src",
    "src/ingestion",
    "src/transformation",
    "src/pyspark_jobs",
    "src/database",
    "src/analytics",
    "src/utils",
    "sql/ddl",
    "sql/dml",
    "sql/analytics",
    "airflow/dags",
    "airflow/plugins",
    "airflow/logs",
    "dashboards/powerbi",
    "dashboards/tableau",
    "dashboards/screenshots",
    "tests",
    "docs",
    "scripts"
]

files = [
    "README.md",
    "requirements.txt",
    ".gitignore",
    "docker-compose.yml",
    ".env.example",

    "configs/config.yaml",
    "configs/db_config.yaml",
    "configs/airflow_config.yaml",

    "notebooks/01_data_exploration.ipynb",
    "notebooks/02_pandas_cleaning.ipynb",
    "notebooks/03_customer_analysis.ipynb",
    "notebooks/04_feature_engineering.ipynb",

    "src/__init__.py",

    "src/ingestion/load_customers.py",
    "src/ingestion/load_orders.py",
    "src/ingestion/load_payments.py",
    "src/ingestion/load_clickstream.py",
    "src/ingestion/load_support.py",

    "src/transformation/pandas_cleaning.py",
    "src/transformation/customer_360_builder.py",
    "src/transformation/deduplication.py",
    "src/transformation/feature_generation.py",
    "src/transformation/data_quality_checks.py",

    "src/pyspark_jobs/spark_orders_etl.py",
    "src/pyspark_jobs/spark_clickstream_etl.py",
    "src/pyspark_jobs/spark_customer_merge.py",
    "src/pyspark_jobs/spark_fact_load.py",

    "src/database/postgres_connection.py",
    "src/database/load_to_postgres.py",
    "src/database/upsert_logic.py",
    "src/database/schema_manager.py",

    "src/analytics/churn_logic.py",
    "src/analytics/clv_calculation.py",
    "src/analytics/segmentation.py",
    "src/analytics/kpi_metrics.py",

    "src/utils/logger.py",
    "src/utils/helpers.py",
    "src/utils/validators.py",
    "src/utils/constants.py",

    "sql/ddl/create_staging_tables.sql",
    "sql/ddl/create_dim_tables.sql",
    "sql/ddl/create_fact_tables.sql",

    "sql/dml/load_dim_customer.sql",
    "sql/dml/load_fact_orders.sql",
    "sql/dml/customer_snapshot.sql",

    "sql/analytics/top_customers.sql",
    "sql/analytics/churn_customers.sql",
    "sql/analytics/monthly_revenue.sql",
    "sql/analytics/support_risk_users.sql",

    "airflow/dags/customer_360_pipeline.py",
    "airflow/dags/daily_orders_pipeline.py",
    "airflow/dags/clickstream_pipeline.py",

    "tests/test_ingestion.py",
    "tests/test_transformations.py",
    "tests/test_sql_logic.py",
    "tests/test_data_quality.py",

    "docs/architecture.md",
    "docs/api_reference.md",

    "scripts/run_local_pipeline.sh",
    "scripts/start_airflow.sh",
    "scripts/init_db.sh",
    "scripts/generate_fake_data.py"
]

# Create folders
for folder in folders:
    path = os.path.join(root, folder)
    os.makedirs(path, exist_ok=True)

# Create files
for file in files:
    file_path = os.path.join(root, file)
    with open(file_path, "w") as f:
        pass

print(f"Project structure created successfully: {root}")