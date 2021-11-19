from typing import List
import fastapi as _fastapi
import fastapi.security as _fastapisecurity
import uvicorn

import sqlalchemy.orm as _sqlorm

import services as _services, schemas as _schemas

app = _fastapi.FastAPI()


@app.post("/hospForm/patient")
async def create_patient(
    patient: _schemas.PatientCreate, db: _sqlorm.Session = _fastapi.Depends(_services.get_db)
):
    db_patient = await _services.get_patient_by_email(patient.email, db)
    if db_patient:
        raise _fastapi.HTTPException(status_code=400, detail="Cette email est déjà utilisée")

    patient = await _services.create_patient(patient, db)

    return await _services.create_token(patient)


@app.post("/hospForm/connection")
async def generate_token(
    form_data: _fastapisecurity.OAuth2PasswordRequestForm = _fastapi.Depends(),
    db: _sqlorm.Session = _fastapi.Depends(_services.get_db),
):
    patient = await _services.authenticate_patient(form_data.username, form_data.password, db)

    if not patient:
        raise _fastapi.HTTPException(status_code=401)

    return await _services.create_token(patient)


@app.get("/hospForm/patient/moi", response_model=_schemas.Patient)
async def get_patient(patient: _schemas.Patient = _fastapi.Depends(_services.get_current_patient)):
    return patient


@app.post("/hospForm/form", response_model=_schemas.PatientForm)
async def create_patient_form(
    patientform: _schemas.PatientFormCreate,
    patient: _schemas.Patient = _fastapi.Depends(_services.get_current_patient),
    db: _sqlorm.Session = _fastapi.Depends(_services.get_db),
):
    return await _services.create_patient_form(patientform=patientform, patient=patient, db=db)


@app.get("/hospForm/form", response_model=List[_schemas.PatientForm])
async def get_patient_forms(
    patient: _schemas.Patient = _fastapi.Depends(_services.get_current_patient),
    db: _sqlorm.Session = _fastapi.Depends(_services.get_db),
):
    return await _services.get_patient_forms(patient=patient, db=db)


@app.get("/hospForm/form/{patientform_id}", status_code=200)
async def get_patient_form(
    patientform_id: int,
    patient: _schemas.Patient = _fastapi.Depends(_services.get_current_patient),
    db: _sqlorm.Session = _fastapi.Depends(_services.get_db),
):
    return await _services.get_patient_form(patientform_id, patient, db)


@app.delete("/hospForm/form/{patientform_id}", status_code=204)
async def delete_patient_form(
    patientform_id: int,
    patient: _schemas.Patient = _fastapi.Depends(_services.get_current_patient),
    db: _sqlorm.Session = _fastapi.Depends(_services.get_db),
):
    await _services.delete_patient_form(patientform_id, patient, db)
    return {"Message :", "Formulaire supprmé avec succès"}


@app.put("/hospForm/form/{patientform_id}", status_code=200)
async def update_patient_form(
    patientform_id: int,
    patient_form: _schemas.PatientFormCreate,
    patient: _schemas.Patient = _fastapi.Depends(_services.get_current_patient),
    db: _sqlorm.Session = _fastapi.Depends(_services.get_db),
):
    await _services.update_patient_form(patientform_id, patient_form, patient, db)
    return {"Message :", "Formulaire mis à jour avec succès"}


@app.get("/hospForm")
async def root():
    return {"message": "Awesome Leads Manager"}

if __name__ == "__main__":
    uvicorn.run("main:app")