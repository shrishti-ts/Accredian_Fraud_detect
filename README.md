# 🚀 Fraud Detection System

A machine learning project to detect fraudulent financial transactions. This repository demonstrates a complete **data science workflow** including **ETL pipelines, feature engineering, machine learning models, and evaluation**.

---

## 📂 Project Overview

The project simulates a real-world fraud detection system with the following components:

1. **ETL Pipeline (Extract, Transform, Load)**

   * Extract raw transactions from `.csv`.
   * Transform: handle missing values, encode categorical variables, and create new features (e.g., transaction velocity, balance ratios).
   * Load cleaned data into an **SQLite database** (`fraud_cleaned.db`).

2. **Machine Learning Models**

   * Random Forest Classifier
   * MLP Classifier
   * Stacked Ensemble Model (meta Random Forest)

3. **Model Evaluation**

   * Accuracy, Precision, Recall, F1-score, ROC-AUC
   * Precision-Recall curve with threshold tuning
   * SHAP values for feature importance & explainability

4. **Industrial-Grade Enhancements (Future Scope)**

   * **Airflow DAG for automated ETL** ✅ (example provided below)
   * MLOps with MLflow, Docker, CI/CD
   * Dashboards for monitoring (Power BI / Tableau)
   * Data governance: logging, monitoring, retraining

---

## ⚙️ ETL Workflow

Implemented in `etl_pipeline.py` (or inside the notebook):

```python
import pandas as pd
import sqlite3

def run_etl(file_path: str, db_name: str = "fraud_cleaned.db"):
    col_names = [
        "step", "type", "amount", "nameOrig", "oldbalanceOrg", "newbalanceOrig",
        "nameDest", "oldbalanceDest", "newbalanceDest", "isFraud", "isFlaggedFraud"
    ]
    df = pd.read_csv(file_path, names=col_names, skiprows=1)
    df = df.dropna()
    df["type"] = df["type"].astype("category").cat.codes
    df["transaction_velocity"] = df["amount"] / (df["step"] + 1)
    df["amount_to_balance_ratio"] = df["amount"] / (df["oldbalanceOrg"] + 1)
    df = df.drop(["nameOrig", "nameDest"], axis=1, errors="ignore")
    conn = sqlite3.connect(db_name)
    df.to_sql("transactions", conn, if_exists="replace", index=False)
    conn.close()
    return df
```

Run:

```python
df_cleaned = run_etl("Fraud.csv")
```

---

## 🛠️ Airflow DAG Integration

Here’s a **sample Airflow DAG** (`fraud_etl_dag.py`) to schedule the ETL daily:

```python
from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
from etl_pipeline import run_etl

default_args = {
    "owner": "airflow",
    "start_date": datetime(2025, 1, 1),
    "retries": 1,
}

with DAG(
    dag_id="fraud_etl_pipeline",
    default_args=default_args,
    schedule_interval="@daily",  # run daily
    catchup=False,
) as dag:

    etl_task = PythonOperator(
        task_id="run_etl_task",
        python_callable=run_etl,
        op_args=["/path/to/Fraud.csv"],  # adjust path
    )

    etl_task
```

* Place this file in your Airflow DAGs folder.
* Airflow will automatically run the ETL and refresh the SQLite DB daily.

---

## 📊 Results

* **Best Model:** Stacked Ensemble (Random Forest + MLP → meta Random Forest)
* **Performance:**

  * Precision: \~0.92
  * Recall: \~0.89
  * ROC-AUC: \~0.96
* **Key Predictors of Fraud:**

  * Transaction type
  * Transaction velocity
  * Amount-to-balance ratio
  * Old balance differences

---

## 📦 Installation

Clone repo:

```bash
git clone https://github.com/shrishti-ts/fraud_detection_model.git
cd fraud_detection_model
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## 📁 File Structure

```
fraud-detection/
│── accredian_fraud_detect.ipynb   # Main notebook with model training & evaluation
│── etl_pipeline.py                # ETL pipeline script
│── fraud_etl_dag.py               # Airflow DAG (scheduling ETL)
│── Fraud.csv                      # Dataset (add manually, not in repo)
│── fraud_cleaned.db               # SQLite DB (created after ETL)
│── requirements.txt
│── README.md
```

---

## 🔮 Next Steps

* [ ] Add MLflow for experiment tracking
* [ ] Build a Power BI / Tableau dashboard for fraud monitoring
* [ ] Deploy as REST API with Docker + CI/CD

---

## 🙌 Acknowledgments

* Dataset inspired by **financial fraud detection benchmarks**.
* Project created as part of **Accredian Assignment**.

---
