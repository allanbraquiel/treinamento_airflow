# Conexão PostgreSQL
POSTGRES_USER = "postgres"
POSTGRES_PASSWORD = "postgres"
POSTGRES_HOST = "172.17.0.1"  # Nome do serviço no Docker Compose
POSTGRES_PORT = "5433"
POSTGRES_DB = "covid_db"

POSTGRES_CONN_STRING = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}"