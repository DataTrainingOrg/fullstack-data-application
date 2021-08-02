from fastapi import FastAPI, Header, Request
from typing import Optional
import base64
import json

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/api")
def read_hello():
    return {"Hello": "Api"}


@app.get("/api/headers")
def read_hello(request: Request, x_userinfo: Optional[str] = Header(None, convert_underscores=True), ):
    print(request["headers"])
    return {"Headers": json.loads(base64.b64decode(x_userinfo))}
