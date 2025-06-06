from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.providers.apache.spark.operators.spark_submit import SparkSubmitOperator
import sys
import os

# Ajouter le dossier parent au path pour les imports Python
sys.path.append(os.path.abspath(os.path.dirname(os.path.dirname(__file__))))

from download_tmdb_movies import download_and_extract_tmdb_dataset
from download_netflix import download_and_extract_netflix_dataset

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

with DAG(
    'pipeline_dag',
    default_args=default_args,
    description='Pipeline complet : ingestion+formatting+combinaison',
    schedule=None,
    start_date=datetime(2023, 1, 1),
    catchup=False,
    tags=['bigdata', 'pipeline'],
) as dag:

    task_ingest_tmdb = PythonOperator(
        task_id='ingest_tmdb',
        python_callable=download_and_extract_tmdb_dataset,
    )

    task_ingest_netflix = PythonOperator(
        task_id='ingest_netflix',
        python_callable=download_and_extract_netflix_dataset,
    )

    task_format_tmdb = SparkSubmitOperator(
        task_id='format_tmdb',
        application=os.path.abspath("spark_jobs/format_tmdb.py"),
        conn_id='spark_default',  
        verbose=True,
        executor_memory='1g',
        driver_memory='1g',
        num_executors=1,
        executor_cores=1,
    )

    task_format_netflix = SparkSubmitOperator(
        task_id='format_netflix',
        application=os.path.abspath("spark_jobs/format_netflix.py"),
        conn_id='spark_default',
        verbose=True,
        executor_memory='1g',
        driver_memory='1g',
        num_executors=1,
        executor_cores=1,
    )

    task_combine = SparkSubmitOperator(
        task_id='combine_datasets',
        application=os.path.abspath("spark_jobs/combine_datasets.py"),
        conn_id='spark_default',
        verbose=True,
        executor_memory='1g',
        driver_memory='1g',
        num_executors=1,
        executor_cores=1,
    )

    # Dépendances
    task_ingest_tmdb >> task_format_tmdb
    task_ingest_netflix >> task_format_netflix
    [task_format_tmdb, task_format_netflix] >> task_combine
