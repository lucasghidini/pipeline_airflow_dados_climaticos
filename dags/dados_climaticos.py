from airflow.models import DAG
from airflow.utils.dates import days_ago
import pendulum
from airflow.operators.bash import BashOperator
from airflow.operators.empty import EmptyOperator
from airflow.operators.python import PythonOperator
from os.path import join
import pandas as pd


with DAG(
    'dados_climatico',
    start_date = pendulum.datetime(2025,8, 11, tz="UTC"),
    schedule_interval= '0 0 * * 1',
)as dag:
    tarefa_1 = BashOperator(
        task_id = 'criar_pasta',
        bash_command= 'mkdir -p "/home/lucas/Documents/airflowalura/semana={{data_interval_end.strftime("%Y-%m-%d")}}"'
    )

    def extrair_dados(data_interval_end):
        city = 'Boston'
        key = '95DBGKD52MR8EF86KV9TQSNHS'

        data_inicio = pendulum.parse(data_interval_end)
        data_final = data_inicio.add(days=7)

        data_inicio_str = data_inicio.strftime("%Y-%m-%d")
        data_final_str = data_final.strftime("%Y-%m-%d")

        URL = join('https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/',
                    f'{city}/{data_inicio_str}/{data_final_str}?unitGroup=metric&include=days&key={key}&contentType=csv')

        dados = pd.read_csv(URL)

        file_path = f'/home/lucas/Documents/airflowalura/semana={data_interval_end}/'
        

        dados.to_csv(file_path + 'dados_brutos.csv')
        dados[['datetime', 'tempmin', 'temp', 'tempmax']].to_csv(file_path + 'temperaturas.csv')
        dados[['datetime', 'description', 'icon']].to_csv(file_path + 'condicoes.csv')

    tarefa_2 = PythonOperator(
        task_id ='extrair_dados',
        python_callable= extrair_dados,
        op_kwargs={'data_interval_end': '{{data_interval_end.strftime("%Y-%m-%d")}}'}
    )

    tarefa_1 >> tarefa_2