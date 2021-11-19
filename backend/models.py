import datetime as _dt

import sqlalchemy as _sqlalchemy
import sqlalchemy.orm as _sqlorm
import passlib.hash as _passlibhash

import database as _database


class Patient(_database.Base):
    __tablename__ = "patient"
    id = _sqlalchemy.Column(_sqlalchemy.Integer, primary_key=True, index=True)
    email = _sqlalchemy.Column(_sqlalchemy.String, unique=True, index=True)
    password = _sqlalchemy.Column(_sqlalchemy.String)

    patientform = _sqlorm.relationship("PatientForm", back_populates="patients")

    def verify_password(self, password: str):
        return _passlibhash.bcrypt.verify(password, self.password)


class PatientForm(_database.Base):
    __tablename__ = "patientform"
    id = _sqlalchemy.Column(_sqlalchemy.Integer, primary_key=True, index=True)
    patient_id = _sqlalchemy.Column(_sqlalchemy.Integer, _sqlalchemy.ForeignKey("patient.id"))

    first_name = _sqlalchemy.Column(_sqlalchemy.String, index=True, nullable=False)
    last_name = _sqlalchemy.Column(_sqlalchemy.String, index=True, nullable=False)
    maiden_name = _sqlalchemy.Column(_sqlalchemy.String)
    #birthdayDate = _sqlalchemy.Column(_sqlalchemy.Date, index=True, nullable=False)
    birthdayDay = _sqlalchemy.Column(_sqlalchemy.Integer, index=True, nullable=False)
    birthdayMonth = _sqlalchemy.Column(_sqlalchemy.Integer, index=True, nullable=False)
    birthdayYear = _sqlalchemy.Column(_sqlalchemy.Integer, index=True, nullable=False)

    email = _sqlalchemy.Column(_sqlalchemy.String, index=True, nullable=False)

    numberAddress = _sqlalchemy.Column(_sqlalchemy.Integer, index=True, nullable=False)
    nameAddress = _sqlalchemy.Column(_sqlalchemy.String, index=True, nullable=False)
    postalCode = _sqlalchemy.Column(_sqlalchemy.Integer, index=True, nullable=False)
    cityAddress = _sqlalchemy.Column(_sqlalchemy.String, index=True, nullable=False)
    countryAddress = _sqlalchemy.Column(_sqlalchemy.String, index=True, nullable=False)

    secuNumber = _sqlalchemy.Column(_sqlalchemy.Integer, nullable=False)

    hospitalName = _sqlalchemy.Column(_sqlalchemy.String, nullable=False)
    causeHosp = _sqlalchemy.Column(_sqlalchemy.String, nullable=False)
    dateHosp = _sqlalchemy.Column(_sqlalchemy.DateTime, nullable=False, default=_dt.datetime.utcnow)
    
    patients = _sqlorm.relationship("Patient", back_populates="patientform")
