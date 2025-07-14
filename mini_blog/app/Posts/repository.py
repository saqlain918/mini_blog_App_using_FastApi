from sqlalchemy.orm import Session
from . import models, schemas
from uuid import UUID

def create_post(db: Session, post_data: schemas.PostCreate, user_id: UUID):
    post = models.Post(**post_data.model_dump(), owner_id=user_id)
    db.add(post)
    db.commit()
    db.refresh(post)
    return post

def get_all_posts_by_user(db: Session, user_id: UUID):
    return db.query(models.Post).filter(models.Post.owner_id == user_id).all()

def get_post_by_id(db: Session, post_id: UUID):
    return db.query(models.Post).filter(models.Post.id == post_id).first()
