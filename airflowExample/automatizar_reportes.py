from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
import pandas as pd
import requests

# Configuración del DAG
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2024, 3, 20),
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG(
    'automatizar_reportes',
    default_args=default_args,
    schedule_interval='@daily',  # Ejecuta diariamente
    catchup=False
)

# Función para extraer datos de Google Sheets
def extract_data():
    url = "URL_DE_GOOGLE_SHEETS_EN_CSV_O_JSON"
    data = pd.read_csv(url)  # O usa requests.get(url).json()
    data.to_csv('/tmp/raw_data.csv', index=False)

# Función para procesar datos
def process_data():
    df = pd.read_csv('/tmp/raw_data.csv')
    df['nueva_columna'] = df['columna_existente'] * 2  # Ejemplo de transformación
    df.to_csv('/tmp/processed_data.csv', index=False)

# Función para generar reporte
def generate_report():
    df = pd.read_csv('/tmp/processed_data.csv')
    df.to_excel('/tmp/reporte.xlsx', index=False)

# Definición de tareas
task_extract = PythonOperator(
    task_id='extract_data',
    python_callable=extract_data,
    dag=dag,
)

task_process = PythonOperator(
    task_id='process_data',
    python_callable=process_data,
    dag=dag,
)

task_report = PythonOperator(
    task_id='generate_report',
    python_callable=generate_report,
    dag=dag,
)

# Definir el flujo de ejecución
task_extract >> task_process >> task_report
