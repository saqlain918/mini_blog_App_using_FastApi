from fastapi import FastAPI
from app.Users import routers as user_routers
from app.Posts import routers as post_routers
from app.Users.models import User

from app.database import Base, engine


Base.metadata.create_all(bind=engine)

app = FastAPI()


app.include_router(user_routers.router, prefix="/users", tags=["Users"])


app.include_router(post_routers.router, prefix="/posts", tags=["Posts"])
