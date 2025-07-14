from sqlalchemy.orm import Session
from . import repository, schemas
from uuid import UUID

def create_new_post(post: schemas.PostCreate, db: Session, user_id: UUID):
    return repository.create_post(db, post, user_id)

def get_user_posts(db: Session, user_id: UUID):
    return repository.get_all_posts_by_user(db, user_id)

def get_post(db: Session, post_id: UUID):
    return repository.get_post_by_id(db, post_id)
