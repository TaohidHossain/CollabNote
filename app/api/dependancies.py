from typing import Annotated
from fastapi import Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.utils import decode_access_token
from app.data.postgresql import get_session
from app.model.user import User
from app.service.user import UserService
from app.core.security import oauth2_scheme


SessionDep = Annotated[AsyncSession, Depends(get_session)]

def get_user_service(session: SessionDep):
    return UserService(session)

UserServiceDep = Annotated[UserService, Depends(get_user_service)]

async def get_current_user(service: UserServiceDep, token: Annotated[str, Depends(oauth2_scheme)]):
    data = decode_access_token(token)
    if not data:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid token or expired token")
    
    user_id = service.get_user_by_id(data["sub"]["user_id"])
    if not user_id:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid token or expired token")
    
    return await UserService.get(user_id) # may need to cast str to UUID

UserDep = Annotated[User, Depends(get_current_user)]
    