# Data Engineering Learning

This repository documents my hands-on journey toward becoming a **Junior Data Engineer**.

The goal is to learn data engineering concepts through practical exercises, mini data pipelines, and the **DeepLearning.AI Data Engineering Professional Certificate** on Coursera.

## Roadmap

1. Python & Pandas
2. SQL
3. PostgreSQL
4. ETL & Data Pipelines
5. Docker
6. Apache Airflow & dbt
7. Cloud Data Engineering

## Current Progress

### 01 - Python & Pandas

Topics covered so far:

* Data Engineering fundamentals
* ETL: Extract, Transform, Load
* Reading CSV files with Pandas
* Handling missing values
* Data type conversion
* Filtering DataFrames
* Creating new columns
* Using `.apply()` with custom transformation functions
* Exporting data to CSV
* Converting CSV data to JSON
* Reading JSON data with Pandas
* Basic data quality concepts

### Mini Pipeline

```text
customers.csv
      |
      v
   Extract
      |
      v
    Pandas
      |
      v
  Transform
  - Fill missing values
  - Convert data types
  - Filter customers
  - Create customer_level
      |
      v
     Load
      |
      +----> high_value_customers.csv
      |
      +----> high_value_customers.json
      |
      +----> customer_with_level.json
```

## Repository Structure

```text
data-engineering-learning/
|
|-- 01-python-pandas/
|   |-- main.py
|   |-- customers.csv
|   |-- high_value_customers.csv
|   |-- high_value_customers.json
|   `-- customer_with_level.json
|
`-- README.md
```

More folders will be added as I progress through SQL, PostgreSQL, ETL, Docker, Airflow/dbt, and cloud technologies.

## Learning Method

For each topic:

1. Learn the core concept.
2. Build a small practical example.
3. Study the related Coursera material.
4. Create additional exercises and examples.
5. Build mini projects.
6. Document progress on GitHub.

## Technologies

Currently:

* Python
* Pandas
* CSV
* JSON
* Git
* GitHub

Planned:

* SQL
* PostgreSQL
* Docker
* Apache Airflow
* dbt
* Cloud platforms

## Goal

Build a strong practical foundation and a public portfolio suitable for **Junior Data Engineer / Entry-Level Data Engineer** roles.
