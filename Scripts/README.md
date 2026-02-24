# 📘 Dimension Tables Creation – README

This folder contains two Python scripts used to generate **dimension tables** from source datasets using Pandas and NumPy. These scripts are helpful for data warehousing, ETL pipelines, and analytical model preparation.

---

# 📂 Project Overview

The following scripts are included:

1. **Dim_Date_Creation.py**
   Creates a Date/Time dimension table by extracting multiple datetime attributes.

2. **Dim_Location_Creation.py**
   Creates a Location dimension table based on selected columns.

---

# ⚙️ Requirements

Make sure the following Python libraries are installed:

```
pandas
numpy
```

Install them using:

```
pip install pandas numpy
```

---

# 🕒 Dim_Date_Creation.py

## Description

This script generates a **Date Dimension table** from a source dataframe. It performs several datetime transformations using Pandas and NumPy.

The function extracts:

* Day
* Hour
* Month
* Year
* Weekday Name
* Weekend Indicator

It also creates a surrogate key for the dimension table.

---

## Function

```
date_dataframe(df, column_name, description)
```

### Parameters

* **df** : Source Pandas DataFrame
* **column_name** : Name of the datetime column
* **description** : Prefix used to create the surrogate key column

### Returns

A new DataFrame containing:

* `{description}_id`
* `date_time`
* `day`
* `hour`
* `month`
* `year`
* `weekday`
* `is_weekend`

---

## Example Usage

```python
import pandas as pd
from Dim_Date_Creation import date_dataframe

result = date_dataframe(df, "created_at", "date")
print(result.head())
```

---

## Notes

* The datetime column must already be in **datetime format**.
* Weekend values are generated using NumPy conditional logic.
* Weekday values are converted from numeric format to names.

---

# 📍 Dim_Location_Creation.py

## Description

This script generates a **Location Dimension table** by selecting two location-related columns and assigning a surrogate key.

---

## Function

```
location_dataframe(df, column_one, column_two, description)
```

### Parameters

* **df** : Source Pandas DataFrame
* **column_one** : First location column
* **column_two** : Second location column
* **description** : Prefix used for the surrogate key

### Returns

A new DataFrame containing:

* `{description}_key`
* Selected location columns

---

## Example Usage

```python
import pandas as pd
from Dim_Location_Creation import location_dataframe

location_dim = location_dataframe(df, "city", "country", "location")
print(location_dim.head())
```

---

# ✅ Best Practices

* Ensure datetime columns are parsed using:

```
df['column'] = pd.to_datetime(df['column'])
```

* Validate null values before generating dimension tables.
* Use clear naming conventions for the `description` parameter.

---

# 👨‍💻 Author

**Somnath Mondal, S. M., somnath1360mondal-INDIA**

---

## 👨‍💻 Author Notes

These scripts are designed to be reusable in ETL pipelines and dimensional modeling workflows. You can extend them to include more attributes such as quarter, timezone, region hierarchy, etc.
