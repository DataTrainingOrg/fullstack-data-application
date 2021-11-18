from flask import current_app,jsonify,request
from app import create_app,db
from models import Articles,articles_schema

from flask import render_template,request,redirect,flash
from . import server
from .models import RatingForm
import pymongo
from datetime import datetime
import urllib
import json

# Create an application instance
app = create_app()

# Define a route to fetch the avaialable articles

@app.route("/articles", methods=["GET"], strict_slashes=False)
def articles():

	articles = Articles.query.all()
	results = articles_schema.dump(articles)

	return jsonify(results)



if __name__ == "__main__":
	app.run(debug=True)