from datetime import datetime
from uuid import UUID, uuid4
from sqlmodel import Column, SQLModel, Field
from sqlalchemy.dialects import postgresql as pg

class User(SQLModel, table=True):
    id: UUID = Field(sa_column=Column(pg.UUID(), primary_key=True), default_factory=uuid4)
    username: str = Field(min_length=2, max_length=100)
    email: str = Field(sa_column=Column(pg.VARCHAR(), unique=True, index=True))
    password_hash: str
    created_at: datetime = Field(default_factory=datetime.now)
    is_active: bool = Field(default=True)