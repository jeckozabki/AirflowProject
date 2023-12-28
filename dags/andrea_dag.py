from datetime import datetime

import yaml
from airflow.decorators import dag
from airflow.operators.empty import EmptyOperator
from airflow.operators.generic_transfer import GenericTransfer


def get_sources():
    with open('/opt/airflow/dags/include/sources.yaml', 'r') as source_yaml:
        return yaml.safe_load(source_yaml)


@dag(
    dag_id='andrea_dag',
    start_date=datetime(2023, 12, 1),
    catchup=True,
    schedule="@daily",
    template_searchpath='/opt/airflow/dags/include'
)
def andrea_taskflow():
    begin_task = EmptyOperator(task_id='begin_task')
    end_task = EmptyOperator(task_id='end_task')

    sources = get_sources()
    extract_and_load = [GenericTransfer.partial(task_id='extract_and_load_' + env.lower(),
                                                preoperator='delete_for_run.sql',
                                                sql='extract_dag_run_metrics.sql',
                                                destination_table='stg_dag_run_metric',
                                                destination_conn_id='cost_monitor_db',
                                                ).expand_kwargs(
        [
            {'source_conn_id': s['connection'],
             'params': {'environment': s['environment'],
                        'division': s['division'],
                        'project': s['project'],
                        'ref_date': '{{ ds }}'
                        }
             } for s in sources if s['environment'].upper() == env.upper()
        ]
    ) for env in ('Dev', 'Sit', 'UAT', 'Prod')]

    begin_task >> extract_and_load >> end_task


andrea_taskflow()
