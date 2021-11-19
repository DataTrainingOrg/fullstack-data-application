from flask import current_app,jsonify,request
from app import create_app,db
from models import Articles,articles_schema
from flask import render_template,request,redirect,flash
from . import server
from .models import RatingForm
from datetime import datetime
import urllib
import json


# Create an application instance
app = create_app()

# Define a route to fetch the avaialable articles

@app.route("/verif", methods=["GET"], strict_slashes=False)
def listPatient():

    patients = Patients.query.all()
    results = patients_schema.dump(patients)

    return jsonify(results)


@app.route("/signup", methods=["POST"], strict_slashes=False)
def add_patient():

    familyName = request.json['familyName']
    firstName = request.json['firstName']
    maidenName = request.json['maidenName']
    birthdayDate = request.json['birthdayDate']
    address = request.json['address']
    secuNumber = request.json['secuNumber']

    hospitalName = request.json['hospitalName']
    longTermCareHospitalisation = request.json['longTermCareHospitalisation']


    email = request.json['email']
    password = request.json['password']



    patient = Patients(

        familyName=familyName,
        firstName=firstName,
        maidenName = maidenName,
        birthdayDate=birthdayDate,
        address = address,
        secuNumber = secuNumber,

        hospitalName = hospitalName,
        longTermCareHospitalisation = longTermCareHospitalisation,

        email=email,
        password=password,
        )

    db.session.add(patient)
    db.session.commit()

    return patient_schema.jsonify(patient)