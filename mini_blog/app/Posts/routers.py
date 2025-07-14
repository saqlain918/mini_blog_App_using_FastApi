from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.Posts import schemas, services
from app.database import SessionLocal
from app.Users.models import User
from uuid import UUID

router = APIRouter()

# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
from uuid import UUID

HARDCODED_USER_ID = UUID("debb833a-0bbf-4535-a5d7-e94d94e90d58")

def get_current_user(db: Session = Depends(get_db)) -> User:
    user = db.query(User).filter(User.id == HARDCODED_USER_ID).first()
    if not user:
        raise HTTPException(status_code=401, detail="User not found (simulate auth)")
    return user



@router.post("/", response_model=schemas.PostResponse)
def create_post(
    post: schemas.PostCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    return services.create_new_post(post, db, current_user.id)


@router.get("/", response_model=list[schemas.PostResponse])
def get_all_posts(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    return services.get_user_posts(db, current_user.id)

@router.get("/{post_id}", response_model=schemas.PostResponse)
def get_post_by_id(
    post_id: UUID,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    post = services.get_post(db, post_id)
    if not post or post.owner_id != current_user.id:
        raise HTTPException(status_code=404, detail="Post not found")
    return post
