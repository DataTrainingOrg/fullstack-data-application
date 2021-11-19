from . import click
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_marshmallow import Marshmallow
from flask_cors import CORS

db = SQLAlchemy()
migrate = Migrate()
ma = Marshmallow()
cors = CORS()

def create_app():
   app = Flask(name)
  # app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
   #app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False           #True

   #db.init_app(app)
   #migrate.init_app(app, db)
   #ma.init_app(app)
   #cors.init_app(app)

   return app