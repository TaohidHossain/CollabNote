from uuid import UUID
from pydantic import BaseModel, EmailStr, Field

class UserCreateRequest(BaseModel):
    username: str = Field(..., min_length=2, max_length=100, example="user")
    email: EmailStr = Field(..., example="a@b.c")
    password: str = Field(..., min_length=8, example="password")

class UserResponse(BaseModel):
    id: UUID
    username: str
    email: EmailStr

    class Config:
        from_attributes = True