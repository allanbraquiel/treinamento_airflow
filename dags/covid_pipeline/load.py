from sqlalchemy import create_engine

def load_to_postgres(state_data: dict, conn_string: str):
    engine = create_engine(conn_string)

    for state, df in state_data.items():
        table_name = f"covid_{state.lower()}"
        df.to_sql(table_name, engine, if_exists="replace", index=False)