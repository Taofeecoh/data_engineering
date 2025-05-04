# from airflow import DAG
# from airflow.operators.python import PythonOperator
# from airflow.models import Variable

# import utils as ut


# dag = DAG(
#     dag_id='random_user_dag',
#     description='a DAG instance for random users API tasks'
# )

# task_one = PythonOperator(
#     task_id = 'random_user_etl_pipeline',
#     python_callable=ut.pipeline,
#     dag=dag
#     )

# task_one