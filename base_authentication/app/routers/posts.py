from typing import List

from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import HTTPBearer
from sqlalchemy.orm import Session
from starlette.requests import Request
from starlette.routing import Router

import models
import schemas
from routers.utils import verify_autorization_header
from services import posts as posts_service

router = APIRouter(prefix="/posts")

security = HTTPBearer()


@router.post("/", tags=["posts"])
async def create_post(post: schemas.Post, db: Session = Depends(models.get_db)):
    return posts_service.create_post(post=post, db=db)


@router.get("/users", dependencies=[Depends(security)], tags=["posts_per_user"])
async def get_user_posts(
    request: Request,
    db: Session = Depends(models.get_db),
) -> List[schemas.Post]:
    auth_header = request.headers.get("Authorization")

    token = verify_autorization_header(auth_header)
    user_id = token.get("user_id")

    return posts_service.get_posts_for_user(db=db, user_id=user_id)


@router.get("/{post_id}", dependencies=[Depends(security)], tags=["posts"])
async def get_post_by_id(
    post_id: str, request: Request, db: Session = Depends(models.get_db)
):
    auth_header = request.headers.get("Authorization")

    token = verify_autorization_header(auth_header)

    post = posts_service.get_post_by_id(post_id=post_id, db=db)

    if str(post.user_id) != token.get("user_id"):
        raise HTTPException(
            status_code=403, detail=f"Forbidden {post.user_id} {token.get('user_id')}"
        )

    return post


@router.get("/", tags=["posts"])
async def get_posts(db: Session = Depends(models.get_db)):
    return posts_service.get_all_posts(db=db)


@router.put("/{post_id}", tags=["posts"])
async def update_post_by_id(
    post_id: str, post: schemas.Post, db: Session = Depends(models.get_db)
):
    return posts_service.update_post(post_id=post_id, db=db, post=post)


@router.delete("/{post_id}", tags=["posts"])
async def delete_post_by_id(post_id: str, db: Session = Depends(models.get_db)):
    return posts_service.delete_post(post_id=post_id, db=db)


@router.delete("/", tags=["posts"])
async def delete_all_posts(db: Session = Depends(models.get_db)):
    return posts_service.delete_all_posts(db=db)
