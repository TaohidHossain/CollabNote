from typing import Annotated

from alembic.util import status
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm

from app.api.dependancies import UserServiceDep
from ..schemas.user import UserCreateRequest, UserResponse

router = APIRouter(
    prefix="/auth",
    tags=["users"],)

@router.post("/signup", response_model=UserResponse)
async def signup(
    request: UserCreateRequest,
    service: UserServiceDep
):
    return await service.add(request)

@router.post("/login")
async def login(
    request_form: Annotated[OAuth2PasswordRequestForm, Depends()],
    service: UserServiceDep
):
    token = await service.login(request_form.username, request_form.password)
    if not token:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")
    return {"access_token": token, "token_type": "bearer"}