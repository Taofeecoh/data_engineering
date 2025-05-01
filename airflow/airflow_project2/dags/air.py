from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.models import Variable

import utils as ut
import app

endpoint = "https://randomuser.me/api"
count = "/?results=20"
gender = "&gender=female"


dag = DAG(
    dag_id='random_user_dag',
    description='a DAG instance for random users API tasks'
)

task_one = PythonOperator(
    task_id = 'send_request',
    python_callable=app.first_request
)

task_two = PythonOperator(
    task_id = 'extract_json',
    python_callable=app.first_json_list
)

task_three = PythonOperator(
    task_id = 'list_to_df',
    python_callable=app.first_df
)

task_four = PythonOperator(
    task_id = 'write_s3',
    python_callable=app.s3_write
    )


