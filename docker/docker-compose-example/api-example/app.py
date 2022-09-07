from flask import Flask, jsonify
from flask_cors import CORS
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os 

app = Flask(__name__)
CORS(app)

@app.route('/', methods=['GET'])
def hello_world():
    response = jsonify({'data': 'Hello, Docker!'})
    return response

@app.route('/db', methods=['GET'])
def hello_db():
    POSTGRES_USER = os.environ.get("POSTGRES_USER")
    POSTGRES_PASSWORD = os.environ.get("POSTGRES_PASSWORD")
    POSTGRES_DB = os.environ.get("POSTGRES_DB")

    SQLALCHEMY_DATABASE_URL = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@db/{POSTGRES_DB}"

    engine = create_engine(
        SQLALCHEMY_DATABASE_URL
    )
    SessionLocal = sessionmaker(autocommit=False, autoflush=True, bind=engine)

    BaseSQL = declarative_base()
    query = engine.execute('SELECT datname FROM pg_database;')
    available_tables = query.fetchall()
    available_tables = [tup[0] for tup in available_tables]
    response = jsonify({'data': available_tables})
    return response
