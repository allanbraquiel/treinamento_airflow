from airflow import DAG 
from airflow.decorators import dag, task
from datetime import datetime, timedelta

@dag(
    dag_id='task_flow_dag',
    start_date=datetime(2025, 4, 1),
    catchup=False
)

def init():
    @task()
    def extract():
        print("Extracting data...")
        return{"data": "extract"}

    @task()
    def transform(data):
        return{"data": data["data"].upper()}

    transform(extract())

dag = init()
