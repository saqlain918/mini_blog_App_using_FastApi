from sqlalchemy.orm import Session
from . import models, schemas

def create_user(user_data: schemas.UserCreate, db: Session):
    user = models.User(**user_data.dict())  # Unpack Pydantic data
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

def get_user_by_id(db: Session, user_id: str):
    return db.query(models.User).filter(models.User.id == user_id).first()