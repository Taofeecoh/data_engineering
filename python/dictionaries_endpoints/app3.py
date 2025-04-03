import requests
import pandas as pd
import boto3
import awswrangler as wr
import os
from dotenv import load_dotenv, dotenv_values
import secret

"""
TASK3
Connect to this API endpoint https://randomuser.me/api/?results=500
Extract all male and female profiles into a different list
At the end you should have 2 lists , one for male and the other for female.

Extract all dob date into a list.
You will see the dob key with a value containing 2 keys date and age. We are only interested in the date.

Extract that date into a list
Extract concatenated first name and last name into a list

This means you will find a way to extract the first name, last name and concatenate them together to make a full name, make sure you send the full name into a list.
"""


url = "https://randomuser.me/api/?results=500"
response = requests.get(url)
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

male_pro = pd.DataFrame(data= male_profile)
male_pro = male_pro[["gender", "email", "phone", "cell", "picture", "nat"]]

female_pro = pd.DataFrame(data= female_profile)
female_pro = female_pro[["gender", "email", "phone", "cell", "picture", "nat"]]

personal_info_df = pd.DataFrame({"full_name" : names_list, "date_of_birth" : date_list})

# Write to S3
my_path = "s3://taofeecoh-bucket"

wr.s3.to_parquet(
    df = male_pro,
    path = f"{my_path}/app3/male-profile",
    boto3_session = secret.session,
     mode= "append",
    dataset= True
)

wr.s3.to_parquet(
    df = female_pro,
    path = f"{my_path}/app3/female-profile",
    boto3_session = secret.session,
    mode = "append",
    dataset= True
)

wr.s3.to_parquet(
    df = personal_info_df,
    path = f"{my_path}/app3/personal_info",
    boto3_session = secret.session,
    mode = 'append',
    dataset= True
)