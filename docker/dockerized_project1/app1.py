import json
import os
import time

import awswrangler as wr
import boto3
import pandas as pd
from dotenv import load_dotenv


# time.sleep(180)

with open("app_response1.json", 'r') as file:
    response = json.load(file)

jobs = response["jobs"]

senior_roles = []
manager_roles = []

for job in jobs:
    if (job["jobTitle"]) and ("Senior" in job["jobTitle"]):
        senior_roles.append(job["jobTitle"])
    elif (job["jobTitle"]) and ("Manager" in job["jobTitle"]):
        manager_roles.append(job["jobTitle"])

titles = senior_roles + manager_roles

position = []

for i in titles:
    if "Senior" in i:
        position.append("Senior")
    else:
        position.append("Manager")

df = pd.DataFrame({"Position": position, "Job_title": titles})

# Write to S3
load_dotenv()
session = boto3.Session(
    aws_access_key_id=os.getenv('ID'),
    aws_secret_access_key=os.getenv('KEY')
)

my_path = "s3://taofeecoh-bucket"
wr.s3.to_parquet(
    df=df,
    path=f"{my_path}/app1-v1",
    boto3_session=session,
    mode="append",
    dataset=True,
    index=False
    )

print("done!")
