from uuid import UUID
from datetime import datetime
from pydantic import BaseModel, EmailStr

class UserCreateRequest(BaseModel):
    username: str
    email: EmailStr
    password: str

class UserResponse(BaseModel):
    id: UUID
    username: str
    email: EmailStr

    class Config:
        from_attributes = True