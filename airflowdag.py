from datetime import timedelta, datetime
from airflow import DAG
from airflow.operators.python import PythonOperator
import json
import requests

seven_days = datetime.combine(
	datetime.today() - timedelta(7), datetime.min.time())

args = {
	'owner': 'Dylan',
	'start_date': seven_days,
}

dag = DAG(
	dag_id = 'vaccination_count_operator',
	default_args = args,
	schedule_interval = None)

def print_context(ds, **kwargs):
	print(kwargs)
	return 'Whatever you return gets printed in the logs'

def get_data():
	url = "https://opendata.arcgis.com/datasets/da83fdaab14e42f0b3fe198a15c5bad5_0.geojson"
	obj = requests.get(url).content
	return obj

run_this = PythonOperator(
	task_id = 'print_context',
	provide_context = True,
	python_callable = print_context,
	dag = dag)

for i in range(10):

	task = PythonOperator(
	        task_id = "get_data_url",
        	provide_context = True,
        	python_callable = print_context,
        	dag = dag)

	task.set_upstream(run_this)
