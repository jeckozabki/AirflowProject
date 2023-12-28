from datetime import datetime

from airflow.decorators import dag
from airflow.operators.empty import EmptyOperator
from airflow.providers.postgres.operators.postgres import PostgresOperator
from airflow.utils.helpers import chain

setup_sql = '''
    drop table if exists stg_dag_run_metric;
    create table stg_dag_run_metric(
        division_name       varchar(16),
        project_name        varchar(64),
        dag_id              varchar(250),
        run_cnt             int
    );
   
'''


@dag(
    dag_id='andrea_setup_database',
    schedule=None,
    start_date=datetime(2023, 12, 1),
    catchup=False,
    template_searchpath='/opt/airflow/dags/include',
)
def taskflow():
    begin_task = EmptyOperator(task_id='begin_task')
    end_task = EmptyOperator(task_id='end_task')

    database_setup = PostgresOperator(task_id='database_setup',
                                      postgres_conn_id='cost_monitor_db',
                                      sql='database_setup.sql')

    chain(
        begin_task,
        database_setup,
        end_task)


taskflow()
