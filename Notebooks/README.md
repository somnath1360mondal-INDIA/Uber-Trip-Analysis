# 📊 Uber Data Warehouse – ETL Notebooks README

This folder contains a collection of **Jupyter Notebooks** used to transform raw Uber trip data into a structured **Dimensional Data Model**. The notebooks perform data cleaning, datatype transformations, dimension table creation, and fact table generation using **Pandas** and **DuckDB**.

---

# 🧱 Overview

The workflow follows a typical data engineering pipeline:

1. Raw data ingestion and datatype standardization
2. Dimension table generation
3. Surrogate key mapping
4. Fact table construction
5. Exporting curated datasets into Parquet format

The architecture aligns with a **Star Schema** approach used in analytical data warehouses.

---

# ⚙️ Technologies Used

* Python
* Pandas
* NumPy
* DuckDB
* Parquet File Format

---

# 📂 Notebook Descriptions

## 1️⃣ data_type_transformation.ipynb

### Purpose

Prepares the raw Uber dataset by:

* Loading CSV source data
* Inspecting schema and metadata
* Converting datetime fields
* Standardizing data types for downstream processing

This notebook acts as the **data staging layer** before dimensional modeling begins.

---

## 2️⃣ dim_location.ipynb

### Purpose

Creates pickup and dropoff location dimension tables using reusable Python scripts.

### Key Operations

* Reads staged Parquet dataset
* Generates pickup and dropoff location dimensions
* Assigns surrogate keys

Outputs:

* Dim_PickUp_Location
* Dim_DropOff_Location

---

## 3️⃣ dim_payment_type.ipynb

### Purpose

Builds the Payment Type dimension.

### Transformations

* Extracts unique payment types
* Maps numeric codes to readable labels such as Credit Card, Cash, etc.

Output:

* Dim_Payment

---

## 4️⃣ dim_pick_up_drop_off.ipynb

### Purpose

Creates Date/Time dimensions for pickup and dropoff timestamps using reusable datetime transformation scripts.

### Features

* Generates surrogate keys
* Extracts day, hour, month, year, weekday
* Adds weekend indicator

Outputs:

* Dim_Date_Pick_Up
* Dim_Date_Drop_Off

---

## 5️⃣ dim_rate.ipynb

### Purpose

Builds the Rate Code dimension.

### Transformations

* Extracts unique RatecodeID values
* Renames fields to standardized warehouse naming conventions

Output:

* Dim_Rate

---

## 6️⃣ dim_travel.ipynb

### Purpose

Creates a Travel dimension by linking pickup and dropoff time surrogate keys.

### Key Logic

* Uses DuckDB SQL joins
* Maps datetime fields to dimension IDs
* Produces relational bridge between pickup and dropoff events

Output:

* Dim_Travel

---

## 7️⃣ fact_trips.ipynb

### Purpose

Generates the central **Fact Table** by joining all dimensions with the staged dataset.

### Key Transformations

* Calculates trip duration (time_taken)
* Joins date, location, payment, rate, and travel dimensions
* Builds analytics-ready fact dataset

Output:

* Fact_Trips

---

# 🔄 Data Flow

Raw CSV → Datatype Transformation → Drafts (Parquet) → Dimension Creation → Final (Parquet) → Fact Table

---

# 📁 Data Layers

## Drafts Layer

Contains intermediate transformed datasets used to generate dimensions.

## Final Layer

Stores curated dimension tables and fact tables ready for analytics.

---

# ✅ Best Practices Implemented

* Modular reusable scripts for dimension creation
* Surrogate key design for star schema modeling
* DuckDB for scalable SQL-based joins
* Parquet format for efficient storage

---

# 👨‍💻 Author

**Somnath Mondal, S. M., somnath1360mondal-INDIA**

---

# 🚀 Notes

This ETL workflow is designed for analytical workloads and can be extended into a full production pipeline using orchestration tools such as Airflow or Prefect. Additional enhancements may include incremental loading, partitioning strategies, and data validation layers.
