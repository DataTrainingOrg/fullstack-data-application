# TP

## Goals

- Introduction to Airflow DAGs

## Before starting

1. Remove previous containers that expose port 8080. They will conflict with the Airflow webserver container.
2. Run `docker-compose up -d --build`
3. Open `localhost:8080` in your browser
4. Login with username `airflow` and password `airflow`


DAGs need to be created in the folder `tp_data_pipeline/dags`.

Find some example DAGs [here](https://github.com/apache/airflow/tree/main/airflow/example_dags).

## Run a DAG

1. In the UI, click on the DAG `airflow_intro`
2. Click on the play button and select `Trigger DAG`
3. By default, the page is on the Grid/Tree view. Click on `Graph` to see the graph view.
4. Enable `Auto-refresh` if it is not already on
5. Click on a task, then click on `Log`, scroll down and find the printed string
6. Click on a task, then click on `Clear` to rerun the task

## Create a DAG

1. In `tp_data_pipeline/dags`