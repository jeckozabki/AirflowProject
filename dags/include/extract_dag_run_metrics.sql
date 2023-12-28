SELECT
    '{{ params.environment }}'  AS environment_name,
    '{{ params.division }}'     AS division_name,
    '{{ params.project }}'      AS project_name,
    dag_id,
    count(1)                    AS run_cnt
FROM log
WHERE CAST(dttm as date) = '{{ ds }}'
  AND event = 'running'
  AND dag_id IS NOT NULL
GROUP BY dag_id;
