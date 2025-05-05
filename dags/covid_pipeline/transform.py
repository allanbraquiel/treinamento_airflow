import pandas as pd


def transform_by_state(df: pd.DataFrame) -> dict:
    grouped = df[["state", "confirmed", "deaths", "date"]]
    states = df["state"].unique()

    state_data = {state: grouped[grouped["state"] == state] for state in states}
    return state_data