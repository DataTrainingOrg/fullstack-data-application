import fastapi as _fastapi
import fastapi.security as _security
import jwt as _jwt
import sqlalchemy.orm as _sqlorm
import passlib.hash as _passlibhash

import database as _database, models as _models, schemas as _schemas

oauth2schema = _security.OAuth2PasswordBearer(tokenUrl="/hospForm/connection")

SECRET_PASSWORD = "password"


def create_database():
    return _database.Base.metadata.create_all(bind=_database.engine)


def get_db():
    db = _database.SessionLocal()
    try:
        yield db
    finally:
        db.close()


async def get_patient_by_email(email: str, db: _sqlorm.Session):
    return db.query(_models.Patient).filter(_models.Patient.email == email).first()


async def create_patient(user: _schemas.PatientCreate, db: _sqlorm.Session):
    patient_obj = _models.Patient(
        email=user.email, password=_passlibhash.bcrypt.hash(user.password)
    )
    db.add(patient_obj)
    db.commit()
    db.refresh(patient_obj)
    return patient_obj


async def authenticate_patient(email: str, password: str, db: _sqlorm.Session):
    patient = await get_patient_by_email(db=db, email=email)

    if not patient:
        return False

    if not patient.verify_password(password):
        return False

    return patient


async def create_token(patient: _models.Patient):
    patient_obj = _schemas.Patient.from_orm(patient)

    token = _jwt.encode(patient_obj.dict(), SECRET_PASSWORD)

    return dict(access_token=token, token_type="bearer")


async def get_current_patient(
    db: _sqlorm.Session = _fastapi.Depends(get_db),
    token: str = _fastapi.Depends(oauth2schema),
):
    try:
        payload = _jwt.decode(token, SECRET_PASSWORD, algorithms=["HS256"])
        patient = db.query(_models.Patient).get(payload["id"])
    except:
        raise _fastapi.HTTPException(
            status_code=401, detail="Votre adresse email ou mot de passe est invalide."
        )

    return _schemas.Patient.from_orm(patient)


async def create_patient_form(patient: _schemas.Patient, db: _sqlorm.Session, patientform: _schemas.PatientFormCreate):
    patientform = _models.PatientForm(**patientform.dict(), patient_id=patient.id)
    db.add(patientform)
    db.commit()
    db.refresh(patientform)
    return _schemas.PatientForm.from_orm(patientform)


async def get_patient_forms(patient: _schemas.Patient, db: _sqlorm.Session):
    patient_forms = db.query(_models.PatientForm).filter_by(patient_id=patient.id)

    return list(map(_schemas.PatientForm.from_orm, patient_forms))


async def select_patient_form(patientform_id: int, patient: _schemas.Patient, db: _sqlorm.Session):
    patient_forms = (
        db.query(_models.PatientForm)
        .filter_by(patient_id=patient.id)
        .filter(_models.PatientForm.id == patientform_id)
        .first()
    )

    if patient_forms is None:
        raise _fastapi.HTTPException(status_code=404, detail="Formulaires inexistants")

    return patient_forms


async def get_patient_form(patientform_id: int, patient: _schemas.Patient, db: _sqlorm.Session):
    patient_forms = await select_patient_form(patientform_id=patientform_id, patient=patient, db=db)

    return _schemas.Patient.from_orm(patient_forms)


async def delete_patient_form(patientform_id: int, patient: _schemas.Patient, db: _sqlorm.Session):
    patient_form = await select_patient_form(patientform_id, patient, db)

    db.delete(patient_form)
    db.commit()


async def update_patient_form(patientform_id: int, patientform_create: _schemas.PatientFormCreate, patient: _schemas.Patient, db: _sqlorm.Session):
    patient_form_db = await select_patient_form(patientform_id, patient, db)

    patient_form_db.first_name = patientform_create.first_name
    patient_form_db.last_name = patientform_create.last_name
    patient_form_db.maiden_name = patientform_create.maiden_name

    #patient_form_db.birthday_date = patientform_create.birthdayDate
    patient_form_db.birthday_day = patientform_create.birthdayDay
    patient_form_db.birthday_month = patientform_create.birthdayMonth
    patient_form_db.birthday_year = patientform_create.birthdayYear

    patient_form_db.number_address = patientform_create.numberAddress
    patient_form_db.name_address = patientform_create.nameAddress
    patient_form_db.code_postal = patientform_create.postalCode
    patient_form_db.city_address = patientform_create.cityAddress
    patient_form_db.country_address = patientform_create.countryAddress

    patient_form_db.secu_number = patientform_create.secuNumber

    patient_form_db.name_hospital = patientform_create.hospitalName
    patient_form_db.cause_hosp = patientform_create.causeHosp

    
    db.commit()
    db.refresh(patient_form_db)

    return _schemas.PatientForm.from_orm(patient_form_db)