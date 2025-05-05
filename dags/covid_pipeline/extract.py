import requests
import pandas as pd
from airflow.models import Variable

def extract_covid_data():
    url = "https://brasil.io/api/dataset/covid19/caso/data/"
    headers = {
        "Authorization": f"Token {Variable.get('BRASIL_IO_TOKEN')}"
    }
    params = {
        "is_last": "True",
        "place_type": "state"
    }
    response = requests.get(url, headers=headers, params=params)
    response.raise_for_status()
    results = response.json()["results"]
    return pd.DataFrame(results)