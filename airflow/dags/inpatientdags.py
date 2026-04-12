from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

DBT_PROJECT_PATH = "/opt/dbt/inpatient_dbt"
DBT_VENV_PATH = "/opt/dbt/inpatient_dbt/.venv/bin/activate"

default_args = {
    "owner": "data_engineer",
    "depends_on_past": False,
    "retries": 1,
}

with DAG(
    dag_id="dbt_inpatient_pipeline",
    default_args=default_args,
    description="Run dbt models for inpatient project",
    schedule_interval="@daily",  # change if needed
    start_date=datetime(2024, 1, 1),
    catchup=False,
    tags=["dbt", "inpatient"],
) as dag:

    dbt_silver = BashOperator(
        task_id="dbt_silver",
        bash_command=f"""
        cd {DBT_PROJECT_PATH} &&
        dbt run --select silver
        """
    )

    dbt_gold = BashOperator(
        task_id="dbt_gold",
        bash_command=f"""
        cd {DBT_PROJECT_PATH} &&
        dbt run --select gold
        """
    )

    dbt_test = BashOperator(
        task_id="dbt_test",
        bash_command=f"""
        cd {DBT_PROJECT_PATH} &&
        dbt test
        """
    )

    dbt_silver >> dbt_gold >> dbt_test