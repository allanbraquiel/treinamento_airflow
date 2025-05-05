from airflow.decorators import dag, task
from datetime import datetime
from covid_pipeline.extract import extract_covid_data
from covid_pipeline.transform import transform_by_state
from covid_pipeline.load import load_to_postgres
from covid_pipeline.utils import get_postgres_conn_string

@dag(schedule="@daily", start_date=datetime(2024, 1, 1), catchup=False, tags=["covid"])
def covid_pipeline():

    @task
    def extract_task():
        return extract_covid_data()

    @task
    def transform(df):
        return transform_by_state(df)

    @task
    def load(state_data):
        conn_str = get_postgres_conn_string()
        load_to_postgres(state_data, conn_str)

    raw_data = extract_task()
    transformed = transform(raw_data)
    load(transformed)

covid_pipeline()
