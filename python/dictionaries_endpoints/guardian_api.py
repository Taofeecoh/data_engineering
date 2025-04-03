import os

import awswrangler as wr
import boto3
import pandas as pd
import requests
from dotenv import load_dotenv

import secret

url = "https://content.guardianapis.com/search?q=%22Nigeria%22&api-key=test"

r = requests.get(url)
if r.status_code == 200:
    response = r.json()
    data = response["response"]
    data = data["results"]
    df = pd.DataFrame(data=data)
    # df.to_csv('guardian_Nigeria.csv',
    # encoding='utf-8', index=False, header=True)
else:
    print("Invalid status code!")

# Write to s3 bucket
load_dotenv()
session = boto3.Session(
    aws_access_key_id=os.getenv('ID'),
    aws_secret_access_key=os.getenv('KEY')
)

my_path = "s3://taofeecoh-bucket"
wr.s3.to_parquet(
    df=df,
    path=f"{my_path}/app4/nigerian-guardian",
    boto3_session=secret.session,
    mode="append",
    dataset=True,
    index=False
    )


############################################
def guardian_api(link):
    r = requests.get(link)
    if r.status_code == 200:
        response = r.json()
        data = response["response"]
        # print(data.keys())
        data = data["results"]
        df = pd.DataFrame(data=data)
        df.to_csv('guardianNigeria.csv', encoding='utf-8',
                  index=False, header=True)   # if saving on local machine
        # return(df) if writing to a cloud storage
    else:
        print("Invalid status code")
