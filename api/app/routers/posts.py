from fastapi import APIRouter, Depends
from ..services import posts as posts_service
from .. import schemas, models
from sqlalchemy.orm import Session

router = APIRouter(prefix="/posts")


@router.post("/", tags=["posts"])
async def create_post(post: schemas.Post, db: Session = Depends(models.get_db)):
    return posts_service.create_post(post=post, db=db)


@router.get("/{post_id}", tags=["posts"])
async def get_post_by_id(post_id: str, db: Session = Depends(models.get_db)):
    return posts_service.get_post_by_id(post_id=post_id, db=db)


@router.get("/", tags=["posts"])
async def get_posts_by_title(title: str = None, db: Session = Depends(models.get_db)):
    if title:
        return posts_service.get_all_posts(db=db)
    else:
        return posts_service.get_posts_by_title(title=title, db=db)


@router.put("/{post_id}", tags=["posts"])
async def update_post_by_id(post_id: str, post: schemas.Post,
                            db: Session = Depends(models.get_db)):
    return posts_service.update_post(post_id=post_id, db=db, post=post)


@router.delete("/{post_id}", tags=["posts"])
async def delete_post_by_id(post_id: str, db: Session = Depends(models.get_db)):
    return posts_service.delete_post(post_id=post_id, db=db)


@router.delete("/", tags=["posts"])
async def delete_all_posts(db: Session = Depends(models.get_db)):
    return posts_service.delete_all_posts(db=db)
