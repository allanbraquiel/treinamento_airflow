from airflow.models import Variable

def get_postgres_conn_string():
    return Variable.get("COVID_POSTGRES_CONN")