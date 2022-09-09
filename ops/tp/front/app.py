from flask import Flask, render_template
import requests

app = Flask(__name__)

# @app.context_processor
# def utility_processor():
#     def request_api(url=API_URL):
#         response = requests.get(f"http://{url}").text
#         return response
#     return dict(request_api=request_api)

@app.route('/')
def hello():
    return render_template('./index.html')