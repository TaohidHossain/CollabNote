from uuid import UUID

from fastapi import HTTPException, status
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from passlib.context import CryptContext

from app.model.user import User
from app.api.schemas.user import UserCreateRequest
from app.core.utils import create_access_token

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class UserService:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def get(self, id: UUID) -> User | None:
        user = await self.session.get(User, id)
        return user

    async def add(self, credentials: UserCreateRequest) -> User:
        user = User(**credentials.model_dump(exclude={"password"}))
        password_hash = pwd_context.hash(credentials.password)
        user.password_hash = password_hash
        try:    
            self.session.add(user)
            await self.session.commit()
            await self.session.refresh(user)
        except Exception as e:
            await self.session.rollback()
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="User with this email already exists")
        return user
    
    async def login(self, email: str, password: str) -> str | None:
        user = await self.session.execute(select(User).where(User.email == email))
        user = user.scalar_one_or_none()
        if not user or not pwd_context.verify(password, user.password_hash):
            return None
        token = create_access_token(data={"sub": str(user.id)})
        return token

