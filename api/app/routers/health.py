from fastapi import FastAPI, Header, Request, APIRouter
from typing import Optional
import base64
import json

router = APIRouter()


@router.get("/")
def read_root():
    return {"Hello": "World"}


@router.get("/api")
def read_hello():
    return {"Hello": "Api"}


@router.get("/health")
def read_root():
    return {"message": "Api is running fine!"}


@router.get("/api/headers")
def read_hello(
    request: Request, x_userinfo: Optional[str] = Header(None, convert_underscores=True)
):
    print(request["headers"])
    return {"Headers": json.loads(base64.b64decode(x_userinfo))}
