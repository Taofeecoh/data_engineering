import requests
import pandas as pd
import boto3
import awswrangler as wr
import os
from dotenv import load_dotenv, dotenv_values


url = "http://api.football-data.org/v4/competitions/"

response = requests.get(url)
if response.status_code == 200:
    competition_data = response.json()
    competition_names = [comp["name"] for comp in competition_data["competitions"]]
    df = pd.DataFrame({"Competition_names": competition_names})
else:
    print("Invalid status code!")

# Write to S3
load_dotenv()
session = boto3.Session(
    aws_access_key_id=os.getenv('ID'),
    aws_secret_access_key=os.getenv('KEY')
)

my_path = "s3://taofeecoh-bucket"
wr.s3.to_parquet(
    df= df,
    path= f"{my_path}/app2/competition-names",
    boto3_session=session,
    mode= "append",
    dataset= True,
    index=False
    )
