import requests
import awswrangler as wr
import pandas as pd
import boto3
from datetime import datetime
from dotenv import load_dotenv
from airflow.models import Variable
import os


def send_request():
    """
    Function to send a request to the API and return the response.
    :param end_point: The endpoint of the API.
    :param parameters: The parameters to be sent with the request.
    :return: The json response from the API.
    """

    endpoint = "https://randomuser.me/api"
    count = "/?results=20"
    gender = "&gender=female"
    r = requests.get(endpoint + count + gender)
    if r.status_code==200:
        r = r.json()
        return r
    else:
        print(f"Error: {r.status_code} - {r.text}")
        return None


def extract_json_inlist():
    """
    Function to extract relevant items from the json response.
    :param response: The json response from the API.
    :return: A list of relevant keys extracted from the json response.
    """
    response = send_request()
    mini_result = []
    for result in response['results']:
        new_result = [result['name'], result['dob'], result['email']]
        mini_result.append(new_result)
    return mini_result


def parse_date(date_str):
    """
    Function to parse the date string from the API response.
    :param date_str: The date string from the API response.
    :return: The date string in the format "dd-mm-yyyy".
    """
    
    date = date_str.split('T')[0]
    date = datetime.strptime(date, "%Y-%m-%d")
    date = date.strftime("%d-%m-%Y")
    return date


def list_to_df():
    """
    Function to convert the list of dictionaries to a pandas DataFrame.
    :param result_in_list: The list of dictionaries to be converted.
    :return: A pandas DataFrame containing the data.
    """
    result_in_list = extract_json_inlist()
    data = []
    for row in result_in_list:
        value = [{'first_name': row[0]['first'],
                'last_name': row[0]['last'],
                'date_of_birth': parse_date(row[1]['date']),
                'age': row[1]['age'],
                'email': row[2]}]
        data.extend(value)
    df = pd.DataFrame(data)
    return df


def boto_session():
    """
    Function to create a boto3 session using the AWS credentials from environment variables.
    :return: A boto3 session object.
    """

    session = boto3.Session(
        aws_access_key_id=Variable.get('AWS_KEY_ID'),
        aws_secret_access_key=Variable.get('AWS_SECRET_KEY')
        #aws_access_key_id=os.getenv('ID'),
        #aws_secret_access_key=os.getenv('KEY')
    )
    return session


def write_s3():
    """
    Function to write the DataFrame to S3 in CSV format.
    :param data_df: The DataFrame to be written to S3.
    :return: None
    """
    data_df = list_to_df()
    mypath = 's3://taofeecoh-bucket/airflow/randomuserAPI-v3'
    wr.s3.to_csv(
        df=data_df,
        path=mypath,
        boto3_session=boto_session(),
        dataset=True
    )


def pipeline():
    send_request()
    extract_json_inlist()
    list_to_df()
    write_s3()
    return "done"


def return_csv(data:list):
    df = pd.DataFrame(data)
    df_csv = df.to_csv('./data_csv', header=True, index=False)
    return df_csv
