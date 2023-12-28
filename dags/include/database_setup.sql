-- Reference / Configuration
drop table if exists cfg_instance;
create table cfg_instance(
	division_name       varchar(16),
	project_name        varchar(64),
	environment_name    varchar(16),
	connection_name     varchar(128)
);
insert into cfg_instance
values
('HH', 'Project1', 'Development', 'CM_DEV_HH_Project1'),
('HH', 'Project2', 'SIT', 'CM_SIT_HH_Project2')
;


-- Stage
drop table if exists stg_dag_run_metric;
create table stg_dag_run_metric(
    environment_name    varchar(16),
    division_name       varchar(16),
    project_name        varchar(64),
    dag_id              varchar(250),
    run_cnt             int
);

