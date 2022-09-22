from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route("/")
def hello_world():
    return jsonify({"title": "Hello from api!"})


@app.route("/job", methods=["POST"])
def print_job():
    title = request.json["title"]
    company = request.json["company"]
    salary = request.json["salary"]
    result = {"message": f"{title}s at {company} earn {salary} dollars"}
    return jsonify(result)
