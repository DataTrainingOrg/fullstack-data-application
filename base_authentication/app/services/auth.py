import os
from typing import Dict, Union, List

import jwt
from fastapi import Depends, HTTPException, Header
from sqlalchemy.orm import Session

import models
from schemas.users import User

JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY", "should-be-an-environment-variable")
JWT_SECRET_ALGORITHM = os.getenv("JWT_SECRET_ALGORITHM", "HS256")


def _encode_jwt(user: User) -> str:
    return jwt.encode(
        {
            "user_id": str(user.id),
            "role": user.role, # admin, customer, staff, manager...
        },
        JWT_SECRET_KEY,
        algorithm=JWT_SECRET_ALGORITHM,
    )


async def verify_authorization_header(
    authorization: str = Header(...),
) -> Dict[str, Union[int, Dict[str, Union[List[str], int, str]]]]:
    if not authorization or not authorization.startswith("Bearer "):
        raise HTTPException(status_code=401, detail="No authorization header")
    try:
        auth = jwt.decode(
            authorization[7:],
            JWT_SECRET_KEY,
            algorithms=[JWT_SECRET_ALGORITHM],
        )
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Token expired")
    except jwt.InvalidTokenError as err:
        raise HTTPException(status_code=401, detail=f"Invalid token: '{err}'")

    return auth


async def get_user_id(authorization: str = Header(...)) -> str:
    auth = await verify_authorization_header(authorization)
    try:
        user_id = str(auth["user_id"])
    except KeyError:
        raise HTTPException(status_code=401, detail="Invalid token")
    return user_id


def generate_access_token(
    db: Session,
    user_login: User,
):
    user = (
        db.query(models.User)
        .filter(
            models.User.username == user_login.username,
            models.User.password == user_login.password,
        )
        .first()
    )

    if not user:
        raise HTTPException(status_code=404, detail="Incorrect username or password")

    return _encode_jwt(user)
