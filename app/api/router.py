from fastapi import APIRouter

from .routers import user
from .schemas.user import UserResponse
from .dependancies import UserDep
api_router = APIRouter(
    prefix="/api/v1",
)

api_router.include_router(user.router)

@api_router.get("/profile", response_model=UserResponse)
def get_profile(user: UserDep):
    return user
