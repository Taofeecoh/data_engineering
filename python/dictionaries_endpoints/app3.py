import os

import awswrangler as wr
import boto3
import pandas as pd
import requests
from dotenv import load_dotenv

url = "https://randomuser.me/api/?results=500"
response = requests.get(url)
if response.status_code == 200:
    user_data = response.json()
    male_profile = []
    female_profile = []
    date_list = []
    names_list = []

    for user in user_data["results"]:
        if user["gender"] == "male":
            male_profile.append(user)
        elif user["gender"] == "female":
            female_profile.append(user)

        if user["dob"]:
            date_list.append(user["dob"]["date"])

        if user["name"]:
            full_name = f"{user["name"]["first"]} {user["name"]["last"]}"
            names_list.append(full_name)

        # Converting to dataframes
        male_pro_df = pd.DataFrame(data=male_profile)
        male_pro_df = male_pro_df[["gender", "email",
                                   "phone", "cell", "picture", "nat"]]

        female_pro_df = pd.DataFrame(data=female_profile)
        female_pro_df = female_pro_df[["gender", "email",
                                       "phone", "cell", "picture", "nat"]]

        personal_info_df = pd.DataFrame({"full_name": names_list,
                                         "date_of_birth": date_list})
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
    df=male_pro_df,
    path=f"{my_path}/app3/male-profile",
    boto3_session=session,
    mode="append",
    dataset=True,
    index=False
)

wr.s3.to_parquet(
    df=female_pro_df,
    path=f"{my_path}/app3/female-profile",
    boto3_session=session,
    mode="append",
    dataset=True,
    index=False
)

wr.s3.to_parquet(
    df=personal_info_df,
    path=f"{my_path}/app3/personal_info",
    boto3_session=session,
    mode='append',
    dataset=True,
    index=False
)
