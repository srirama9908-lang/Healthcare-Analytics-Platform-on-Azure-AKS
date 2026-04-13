from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

def test():
    print("Airflow is working!")

with DAG(
    dag_id="test_dag_simple",
    start_date=datetime(2024, 1, 1),
    schedule=None,
    catchup=False,
) as dag:

    task1 = PythonOperator(
        task_id="test_task",
        python_callable=test
    )