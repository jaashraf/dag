import os
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime, timedelta
from helper.Task1Helper import convertJsonToObjectList
from helper.Task1Helper import putDataIntoCSV
from helper.Task1Helper import getVehicleListAsJson
import json

default_args = {
    "owner": "airflow",
    "depends_on_past" : False,
    "start_date" : datetime(2019,11, 8),
    "provide_context": True,
    "email": ["testproject@gmail.com"],
    "email_on_failure": True,
    "email_on_retry": True,
    "retries" : 1,
    "retry_delay" : timedelta(minutes=2)
    }

dag = DAG("Vehicle_processing", default_args = default_args, catchup=False, schedule_interval=timedelta(hours=1))


def pushIntoXComms(**kwargs):
    data = getVehicleListAsJson()
    kwargs['ti'].xcom_push(key='vehicle data', value = data)


def processByFuelData(arg1, **kwargs):
    ti = kwargs['ti']
    data = ti.xcom_pull(key='vehicle_data', task_ids='get_vehicle_from_api')
    print(arg1, data)
    putDataIntoCSV(data, arg1)


# def processFuelType(fuelType):
#     print(" Putting Vehicle data to csv file of type: " + fuelType)
#     putDataIntoCSV(fuelType)


getVehicleListFromAPITask = PythonOperator(
    task_id = 'get_vehicle_from_api',
    python_callable = pushIntoXComms,
    dag = dag
)

# processGasolineTask = PythonOperator(
#     task_id = 'process_gasoline',
#     python_callable = processFuelType,
#     op_args = ['Gasoline'],
#     dag = dag
# )
#
# processDieselTask = PythonOperator(
#     task_id = 'process_Diesel',
#     python_callable = processFuelType,
#     op_args = ['Diesel'],
#     dag = dag
# )
#
# processElectricTask = PythonOperator(
#     task_id = 'process_Electric',
#     python_callable = processFuelType,
#     op_args = ['Electric'],
#     dag = dag
# )
#
# processHybridTask = PythonOperator(
#     task_id = 'process_Hybrid',
#     python_callable = processFuelType,
#     op_args = ['Hybrid'],
#     dag = dag
# )
