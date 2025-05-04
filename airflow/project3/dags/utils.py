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

def pipeline():
    send_request()
    extract_json_inlist()
    return "done extracting to list"