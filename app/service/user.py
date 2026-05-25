from uuid import UUID

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
        hashed_password = pwd_context.hash(credentials.password)
        user.hashed_password = hashed_password
        self.session.add(user)
        await self.session.commit()
        await self.session.refresh(user)
        return user
    
    async def login_user(self, email: str, password: str) -> str | None:
        user = await self.session.execute(select(User).where(User.email == email))
        user = user.scalar_one_or_none()
        if not user or not pwd_context.verify(password, user.hashed_password):
            return None
        token = create_access_token(data={"sub": user.id})
        return token

