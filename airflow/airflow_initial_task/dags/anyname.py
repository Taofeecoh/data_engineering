from airflow import DAG
from airflow.operators.python import PythonOperator

from utils import add_num, sub_num



dag = DAG(
    dag_id='initial_dag',
    description='A DAG instance'
    )

task_one = PythonOperator(
    task_id='add_task',
    python_callable=add_num,
    dag=dag
)

task_two=PythonOperator(
    task_id="sub_task",
    python_callable=sub_num,
    dag=dag
)

task_one >> task_two