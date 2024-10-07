import base64
from typing import Optional
from fastapi import FastAPI, Header
from fastapi.middleware.cors import CORSMiddleware
import json

from starlette.requests import Request
from starlette_exporter import PrometheusMiddleware, handle_metrics
from models import BaseSQL, engine
import routers
from routers.auth import auth_router
from routers.users import user_router

app = FastAPI(
    title="Auth app",
    description="My description",
    version="0.0.1",
)
origins = [
    "http://localhost:4200",
    "http://localhost:3000",
    "http://localhost:3001",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(routers.PostRouter)
app.include_router(routers.HealthRouter)
app.include_router(user_router)
app.include_router(auth_router)

app.add_middleware(PrometheusMiddleware)

app.add_route("/metrics", handle_metrics)


@app.on_event("startup")
async def startup_event():
    BaseSQL.metadata.create_all(bind=engine)


@app.get("/api/headers")
def read_hello(
    request: Request,
    x_userinfo: Optional[str] = Header(None, convert_underscores=True),
):
    print(request["headers"])
    return {"Headers": json.loads(base64.b64decode(x_userinfo))}


@app.get("/")
def read_root():
    return {"Hello": "World"}
