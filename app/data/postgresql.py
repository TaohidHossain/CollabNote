from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from sqlalchemy import URL

from app.core.config import db_settings

DATABASE_URL = URL.create(
    drivername="postgresql+asyncpg",
    username=db_settings.POSTGRES_USER,
    password=db_settings.POSTGRES_PASSWORD,
    host=db_settings.POSTGRES_SERVER,
    port=db_settings.POSTGRES_PORT,
    database=db_settings.POSTGRES_DATABASE
).render_as_string(hide_password=False)

engine = create_async_engine(
    url= DATABASE_URL,
    echo=True
    )

async_session = sessionmaker(
    bind=engine,
    expire_on_commit=False,
    class_=AsyncSession
)

async def get_session():
    async with async_session() as session:
        yield session