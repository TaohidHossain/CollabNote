from datetime import datetime
from uuid import UUID, uuid4
from sqlmodel import Column, SQLModel, Field
from sqlalchemy.dialects import postgresql as pg
from pydantic import EmailStr

class User(SQLModel, table=True):
    id: UUID = Field(sa_column=Column(pg.UUID(), primary_key=True), default_factory=uuid4)
    username: str
    email: EmailStr
    password_hash: str
    created_at: datetime = Field(default_factory=datetime.now)
    is_active: bool = Field(default=True)