from typing import Optional, List
from uuid import uuid4

import jwt
from fastapi import HTTPException
from jwt import InvalidTokenError
from sqlalchemy.orm import Session
from starlette.status import HTTP_401_UNAUTHORIZED

import models
from models import get_db
from schemas.users import User
from services.auth import JWT_SECRET_KEY, JWT_SECRET_ALGORITHM


def create_user(db: Session, user: User) -> models.User:
    record = db.query(models.User).filter(models.User.username == user.username).first()
    if record:
        raise HTTPException(status_code=409, detail="Username already taken")

    db_user = models.User(
        id=str(uuid4()), username=user.username, password=user.password
    )
    db.add(db_user)
    db.commit()

    return db_user


def get_all_users(db: Session) -> List[models.User]:
    return db.query(models.User).filter().all()


def get_user_by_id(db: Session, user_id: int) -> Optional[models.User]:
    return db.query(models.User).filter(models.User.id == user_id).first()


def get_current_user_id(token: str):
    try:
        payload = jwt.decode(token, JWT_SECRET_KEY, algorithms=[JWT_SECRET_ALGORITHM])
        user_id: str = payload.get("user_id")
        if user_id is None:
            raise HTTPException(
                status_code=HTTP_401_UNAUTHORIZED,
                detail="Could not validate credentials",
            )
        return user_id
    except InvalidTokenError:
        raise HTTPException(
            status_code=HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentials",
        )
