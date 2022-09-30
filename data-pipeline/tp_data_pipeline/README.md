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

Edit `tp_data_pipeline/dags/airflow_intro.py` for the following questions.

When the Python file is saved, the Airflow UI might take some seconds to refresh and see the new version of the file. To check that it is up-to-date, click on `Code` in the DAG page.

1. In the writer function, write the string "1 1 2 3 5 8 13 21" to a file named `/files/numbers.txt`
2. In the reader function, read and print the content of the file `/files/numbers.txt`
3. Create a `calculator` task which:
- receives the content of the reader function
- calculates the sum of the content numbers
- prints the result
- writes the result to a file named `/files/result.txt`

See [XComs docs](https://airflow.apache.org/docs/apache-airflow/stable/concepts/xcoms.html) about communication between tasks.

See this [XComs example](https://github.com/apache/airflow/blob/main/airflow/example_dags/tutorial_dag.py#L69-L85).

## Interact with a Postgres database (advanced)

Use an existing Postgres database, from a previous TP for example. Use the `PostgresOperator` to interact with it from a DAG:
- read data from a table
- write data to a table

See [operator docs](https://airflow.apache.org/docs/apache-airflow-providers-postgres/stable/operators/postgres_operator_howto_guide.html).