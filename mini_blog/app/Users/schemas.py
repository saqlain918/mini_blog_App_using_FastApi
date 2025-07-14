from pydantic import BaseModel, EmailStr
from uuid import UUID

class UserCreate(BaseModel):
    username: str
    email: EmailStr

class UserResponse(BaseModel):
    id: UUID
    username: str
    email: EmailStr

    class Config:
        orm_mode = True
