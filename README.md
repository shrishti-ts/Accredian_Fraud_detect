# 🚨 Fraud Detection using Machine Learning

This repository contains a machine learning project that builds and evaluates models to detect fraudulent transactions. The project is based on the dataset `Fraud.csv` and is implemented in the Jupyter Notebook **`fraud_detection_model.ipynb`**.

---

## 📌 Project Overview

Fraud detection is a critical problem in the financial industry, where fraudulent transactions can cause significant financial losses. In this project, we:

1. **Clean the dataset** – handle missing values, outliers, and multicollinearity.
2. **Perform feature engineering** – create meaningful variables such as transaction velocity and amount-to-balance ratio.
3. **Balance the dataset** – since fraud data is highly imbalanced, we apply **SMOTE** for resampling.
4. **Train multiple models** including:

   * Random Forest (RF)
   * Multi-Layer Perceptron (MLP)
   * Stacking (RF + MLP with RF as meta-model)
5. **Evaluate performance** using accuracy, precision, recall, F1-score, ROC-AUC, and PR curves.
6. **Interpret the model** with **SHAP values** to identify the most important features predicting fraud.

---
⚡ ETL Orchestration (Airflow Simulation):
The repo includes a DAG file (airflow_dags/fraud_etl_dag.py) demonstrating how this project would be orchestrated in production using Apache Airflow.
While Colab cannot run Airflow directly, the DAG can be deployed in any Airflow environment by placing it inside the dags/ folder.

## 🛠️ Tech Stack

* **Python** 3.8+
* **Libraries**:

  * pandas, numpy
  * scikit-learn
  * imbalanced-learn (SMOTE)
  * matplotlib, seaborn
  * shap

---

## 📂 Repository Structure

```
├── accredian_fraud_detect.ipynb   # Main notebook with analysis & models
├── Fraud.csv                      # Dataset (if provided)
├── requirements.txt               # Dependencies
└── README.md                      # Project documentation
```

---

## 🚀 Results

* **Best Model**: Stacked model (Random Forest + MLP with Random Forest as meta-model).

* **Performance Metrics**:

  * Accuracy: \~0.98
  * Precision: High (indicates few false positives)
  * Recall: Improved via threshold tuning (critical for fraud detection)
  * ROC-AUC: \~0.99

* **Key Factors Predicting Fraud** (from SHAP & feature importance):

  * **Transaction Amount**
  * **Transaction Velocity (Amount / Step)**
  * **Amount-to-Balance Ratio**
  * **Transaction Type (encoded)**

These factors make sense since unusual spending behavior or disproportionate amounts relative to balance are common fraud indicators.

---

## ✅ Prevention Recommendations

* Set **dynamic transaction limits** based on user history.
* Monitor **velocity of transactions** (multiple high-value transactions in short time).
* Strengthen **infrastructure logging** to flag anomalies.
* Deploy the ML model in production for real-time fraud alerts.

---

## 📊 Next Steps

* Deploy the model as an API (FastAPI/Flask).
* Automate retraining with new data (MLOps).
* Test with real-world streaming data (Kafka/Spark).

---

## ⚙️ Installation

Clone the repo:

```bash
git clone https://github.com/shrishti-ts/fraud-detection.git
cd fraud-detection
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run Jupyter Notebook:

```bash
jupyter notebook accredian_fraud_detection_model.ipynb
```

---

✨ Built with Python and Machine Learning to detect fraud efficiently.

---

Do you want me to now **rewrite your requirements.txt** from your notebook imports (so it’s 100% correct)?
