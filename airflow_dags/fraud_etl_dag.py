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
