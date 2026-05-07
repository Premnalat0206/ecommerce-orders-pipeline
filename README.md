# E-Commerce Orders Pipeline

## Overview

This project is a production-style PySpark ETL pipeline built for processing e-commerce order data.

The pipeline performs:
- data ingestion
- data transformation
- data validation
- bad records separation
- clean records generation
- logging and error handling

---

## Tech Stack

- Python
- PySpark
- Git
- GitHub

---

## Project Structure

e-commerce_orders_pipeline/
│
├── data/
├── logs/
├── src/
│   ├── ingestion.py
│   ├── transformation.py
│   ├── validation.py
│   ├── utils.py
│   └── main.py

---

## Pipeline Flow

1. Read raw CSV data
2. Standardize categories
3. Remove duplicate records
4. Convert timestamps
5. Validate records
6. Separate bad records
7. Generate clean dataset

---

## Validation Rules

- customer_id should not be null
- amount should be greater than 0
- order_time should contain valid timestamps

---

## Features

- Modular architecture
- Reusable utility functions
- Logging support
- Exception handling
- Bad records tracking
- PySpark transformations

---

## How to Run

```bash
python src/main.py
```
