# my_dag.py
from airflow.decorators import dag, task
from datetime import datetime
from airflow.providers.apache.spark.operators.spark_submit import SparkSubmitOperator

@dag(
    dag_id="my_dag",
    start_date=datetime(2024, 1, 1),
    schedule_interval=None,
    catchup=False,
)
def my_dag():
    submit_job = SparkSubmitOperator(
        task_id="submit_job",
        conn_id="my_spark_conn",
        application="include/scripts/read.py",
        verbose=True,
    )

    @task.pyspark(conn_id="my_spark_conn")
    def read_data(spark, sc):
        df = spark.createDataFrame(
            [
                (1, "John Doe", 21),
                (2, "Jane Doe", 22),
                (3, "Joe Bloggs", 23),
            ],
            ["id", "name", "age"],
        )
        df.show()
        return df.toPandas().to_json()

    submit_job >> read_data()

my_dag()
