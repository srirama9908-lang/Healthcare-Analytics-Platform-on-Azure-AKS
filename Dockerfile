FROM apache/airflow:2.9.3-python3.11

USER root

RUN apt-get update && apt-get install -y git \
    && apt-get clean

USER airflow

# ✅ ONLY install dbt (do NOT use requirements.txt)
RUN pip install --no-cache-dir dbt-core dbt-snowflake

USER root

# Copy dbt project
COPY --chown=airflow:0 inpatient_dbt /opt/dbt

USER airflow