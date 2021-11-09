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


@app.route("/signin", methods=["GET"], strict_slashes=False)
def signin():
	if request.method == 'POST':
		connection = pymongo.MongoClient("mongodb://mongodb:27017/mongodb")
		db_m = connection["mongodb"]
		collection = db_m['User']
		form_username = str(request.form.get('username'))
		form_password = str(request.form.get('password'))

		try:
			mongo_pwd = collection.find({'username': form_username})[0]['password']
		except:
			mongo_pwd=''

		try:
			if mongo_pwd == form_password:
				server.config["LOGGED"] = True
				server.config["USERNAME"] = form_username
				return redirect('/')
			else:
				flash('Wrong password')
				return redirect('/signin')
			
		except:
			
			return redirect('/signupko')

	return render_template('signin.html')


if __name__ == "__main__":
	app.run(debug=True)