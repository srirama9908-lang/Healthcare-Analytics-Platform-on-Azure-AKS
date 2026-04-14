from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

DBT_PROJECT_PATH = "/opt/dbt"

default_args = {
    "owner": "data_engineer",
    "depends_on_past": False,
    "retries": 1,
}

with DAG(
    dag_id="dbt_inpatient_pipeline",
    default_args=default_args,
    description="Run dbt silver → gold → test",
    schedule="@daily",
    start_date=datetime(2024, 1, 1),
    catchup=False,
) as dag:

    dbt_silver = BashOperator(
        task_id="run_silver_models",
        bash_command=f"""
        cd {DBT_PROJECT_PATH} &&
        dbt run --select silver
        """,
    )

    dbt_gold = BashOperator(
        task_id="run_gold_models",
        bash_command=f"""
        cd {DBT_PROJECT_PATH} &&
        dbt run --select gold
        """,
    )

    dbt_test = BashOperator(
        task_id="run_tests",
        bash_command=f"""
        cd {DBT_PROJECT_PATH} &&
        dbt test
        """,
    )

    dbt_silver >> dbt_gold >> dbt_test