from dotenv import load_dotenv
import utils as ut

load_dotenv()

endpoint = "https://randomuser.me/api"
count = "/?results=20"
gender = "&gender=female"

first_request =ut.send_request(endpoint,(count+gender))
first_json_list = ut.extract_json_inlist(first_request)
first_df = ut.list_to_df(first_json_list)
s3_write = ut.write_s3(first_df)


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
