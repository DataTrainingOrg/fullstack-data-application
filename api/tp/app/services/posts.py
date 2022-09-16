from typing import List

from sqlalchemy.orm import Session
from fastapi import HTTPException
from datetime import datetime
from .. import models, schemas


def get_all_posts(db: Session, skip: int = 0, limit: int = 10) -> List[models.Post]:
    records = db.query(models.Post).filter().offset(skip).limit(limit).all()
    for record in records:
        record.id = str(record.id)
    return records


def get_post_by_id(post_id: str, db: Session) -> models.Post:
    record = db.query(models.Post).filter(models.Post.id == post_id).first()
    if not record:
        raise HTTPException(status_code=404, detail="Not Found") 
    record.id = str(record.id)
    return record


def get_posts_by_title(title: str, db: Session) -> List[models.Post]:
    records = db.query(models.Post).filter(models.Post.title == title).all()
    for record in records:
        record.id = str(record.id)
    return records


def update_post(post_id: str, db: Session, post: schemas.Post) -> models.Post:
    db_post = get_post_by_id(post_id=post_id, db=db)
    for var, value in vars(post).items():
        setattr(db_post, var, value) if value else None
    db_post.updated_at = datetime.now()
    db.add(db_post)
    db.commit()
    db.refresh(db_post)
    return db_post


def delete_post(post_id: str, db: Session) -> models.Post:
    db_post = get_post_by_id(post_id=post_id, db=db)
    db.delete(db_post)
    db.commit()
    return db_post


def delete_all_posts(db: Session) -> List[models.Post]:
    records = db.query(models.Post).filter()
    for record in records:
        db.delete(record)
    db.commit()
    return records


def create_post(db: Session, post: schemas.Post) -> models.Post:
    record = db.query(models.Post).filter(models.Post.id == post.id).first()
    if record:
        raise HTTPException(status_code=409, detail="Already exists")
    db_post = models.Post(**post.dict())
    db.add(db_post)
    db.commit()
    db.refresh(db_post)
    db_post.id = str(db_post.id)
    return db_post
