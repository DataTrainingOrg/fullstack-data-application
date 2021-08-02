FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7

ADD requirements.txt .

RUN pip install -r requirements.txt

COPY ./app /app/app
COPY ./scripts/wait-for-it.sh /app/

RUN chmod +x /app/wait-for-it.sh