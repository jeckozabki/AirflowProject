# Airflow

## Prerequisites

### Virtual environment
Setup a virtual environment 
```shell
python -m venv venv
source ./venv/bin/activate
```

### Docker setup
Follow the guide at [this link](https://airflow.apache.org/docs/apache-airflow/stable/howto/docker-compose/index.html) for setup and run in Docker Compose 

Steps in short 

```shell
mkdir -p ./dags ./logs ./plugins ./config
echo -e "AIRFLOW_UID=$(id -u)" > .env

docker compose up airflow-init
```

### Start / Stop / Terminate 
Start -- detached  
```shell
docker compose up -d
```
Start with additional databases -- detached  
```shell
docker compose $(find docker-compose* | sed -e 's/^/-f /') up -d
```

Start with flower 
```shell
docker compose --profile flower up
```

Stat Flower afterwards -- detached
```shell
docker compose up flower -d 
```

Stop and cleanup 
```shell
docker compose down --volumes --rmi all
```


## Others
Upgrade venv environment 
```shell
PROJECT_DIR=$(pwd)
python -m venv --upgrade $PROJECT_DIR
```