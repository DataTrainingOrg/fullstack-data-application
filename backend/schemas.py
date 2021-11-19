import datetime as _datetime
import pydantic as _pydantic


class _PatientBase(_pydantic.BaseModel):
    email: str


class PatientCreate(_PatientBase):
    password: str

    class Config:
        orm_mode = True


class Patient(_PatientBase):
    id: int

    class Config:
        orm_mode = True


class _PatientFormBase(_pydantic.BaseModel):
    first_name: str
    last_name: str
    maiden_name: str
    #birthdayDate: _datetime.date
    birthdayDay: int
    birthdayMonth: int
    birthdayYear: int

    email: str

    numberAddress: int
    nameAddress: str
    postalCode: int
    cityAddress: str
    countryAddress: str

    secuNumber: int

    hospitalName: str
    causeHosp: str


class PatientFormCreate(_PatientFormBase):
    pass


class PatientForm(_PatientFormBase):
    id: int
    patient_id: int
    dateHosp: _datetime.datetime

    class Config:
        orm_mode = True
