import requests
import pandas as pd
import boto3
import awswrangler as wr
import os
from dotenv import load_dotenv, dotenv_values
import secret



"""
TASK2
Connect to this API endpoint http://api.football-data.org/v4/competitions/ 
Extract all the competition names into a separate list.
"""


url = "http://api.football-data.org/v4/competitions/"

response = requests.get(url)
competition_data = response.json()
competition_names = [comp["name"] for comp in competition_data["competitions"]]
df = pd.DataFrame({"Competition_names": competition_names})

# Write to S3
my_path = "s3://taofeecoh-bucket"

wr.s3.to_parquet(
    df= df,
    path= f"{my_path}/app2/competition-names",
    boto3_session= secret.session,
    mode= "append",
    dataset= True
    )