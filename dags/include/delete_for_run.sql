DELETE FROM stg_dag_run_metric
WHERE environment_name = '{{ params.environment }}'
  AND division_name = '{{ params.division }}'
  AND project_name = '{{ params.project }}'
;