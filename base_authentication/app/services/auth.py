import os

import jwt
from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session

import models
from schemas.users import User

JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY", "should-be-an-environment-variable")
JWT_SECRET_ALGORITHM = os.getenv("JWT_SECRET_ALGORITHM", "HS256")


def _encode_jwt(user: User) -> str:
    return jwt.encode(
        {
            "user_id": str(user.id),
        },
        JWT_SECRET_KEY,
        algorithm=JWT_SECRET_ALGORITHM,
    )


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
