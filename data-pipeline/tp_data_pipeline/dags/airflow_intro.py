from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python import PythonOperator

with DAG(
    "airflow_intro",
    default_args={
        "retries": 2,
        "retry_delay": timedelta(minutes=5),
    },
    schedule=None,
    start_date=datetime(2022, 9, 1),
    catchup=False,
) as dag:

    def writer(**kwargs):
        print("hello")

    def reader(**kwargs):
        print("world")

    writer_task = PythonOperator(task_id="writer", python_callable=writer)

    reader_task = PythonOperator(task_id="reader", python_callable=reader)

    writer_task >> reader_task
