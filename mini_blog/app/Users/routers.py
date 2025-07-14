# app/users/routers.py

from fastapi import APIRouter, Depends,HTTPException
from sqlalchemy.orm import Session
from app.Users import services, schemas
from app.database import SessionLocal

router = APIRouter()

# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/create-user", response_model=schemas.UserResponse)
def create_user_route(user: schemas.UserCreate, db: Session = Depends(get_db)):
    return services.create_new_user(user, db)
@router.get("/{user_id}", response_model=schemas.UserResponse)
def get_user(user_id: str, db: Session = Depends(get_db)):
    user = services.get_user(user_id, db)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user