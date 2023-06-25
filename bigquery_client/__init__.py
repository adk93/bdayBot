from google.cloud import bigquery
from dotenv import load_dotenv
import os
import ast


load_dotenv()


def get_data(query: str) -> [dict]:
    service_account_json = ast.literal_eval(os.getenv("bigquery_service_account_json"))
    client = bigquery.Client.from_service_account_info(service_account_json)

    job = client.query(query)
    return job.result()


