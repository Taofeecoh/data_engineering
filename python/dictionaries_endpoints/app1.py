
"""
TASK1
Connect to this API endpoint https://jobicy.com/api/v2/remote-jobs?count=20&geo=usa&industry=marketing&tag=seo 
Extract all senior roles and manager roles into a different list.
At the end you should have 2 lists , one for senior roles and the other for manager roles.
"""

from app1_response import response
import pandas as pd
import boto3
import awswrangler as wr
import os
from dotenv import load_dotenv, dotenv_values
import secret       

jobs = response["jobs"]

senior_roles = []
manager_roles = []
for job in jobs:
    if (job["jobTitle"]) and ("Senior" in job["jobTitle"]):
        senior_roles.append(job["jobTitle"])
    elif (job["jobTitle"]) and ("Manager" in job["jobTitle"]): # ("Senior" not in job["jobTitle"]) and ("Manager" in job["jobTitle"]) :
        manager_roles.append(job["jobTitle"])

# Join job title lists
titles = senior_roles + manager_roles

#Create position identifier
position = []
for i in titles:
    if "Senior" in i:
       position.append("Senior")
    else:
        position.append("Manager")

# load data into df
df = df = pd.DataFrame({"Position": position, "Job_title": titles})

# Write to S3
my_path = "s3://taofeecoh-bucket"
wr.s3.to_parquet(
    df= df,
    path= f"{my_path}/app1",
    boto3_session= secret.session,
    mode= "append",
    dataset= True
    )