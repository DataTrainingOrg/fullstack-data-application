FROM python:3.8

WORKDIR /app

COPY . .

RUN apt update && apt install -y ca-certificates
RUN pip install -r requirements.txt

ENV FLASK_APP=server
EXPOSE 5000

ENTRYPOINT ["python"]
CMD ["-m" , "flask", "run", "--host=0.0.0.0"]
