from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

import models
from schemas.users import User
from services.users import create_user, get_all_users

user_router = APIRouter(prefix="/users")


@user_router.post("/", tags=["users"])
async def post_user(user: User, db: Session = Depends(models.get_db)):
    return create_user(user=user, db=db)


@user_router.get("/", tags=["users"])
async def retrieve_all_users(db: Session = Depends(models.get_db)) -> List[User]:
    return get_all_users(db=db)
