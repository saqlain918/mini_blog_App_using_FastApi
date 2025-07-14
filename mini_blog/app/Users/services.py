from sqlalchemy.orm import Session
from . import schemas, repository

def create_new_user(db: Session, user: schemas.UserCreate):
    return repository.create_user(db, user)


def get_user(user_id: str, db: Session):
    return repository.get_user_by_id(db, user_id)