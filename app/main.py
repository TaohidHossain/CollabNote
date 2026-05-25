from contextlib import asynccontextmanager
from fastapi import FastAPI

from app.api.router import api_router
from app.core.config import db_settings, jwt_settings, mongodb_settings
from app.data.postgresql import DATABASE_URL
from app.data.mongodb import MONGODB_URL, close_mongodb, connect_mongodb, get_mongodb_database

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Connect to MongoDB when the application starts
    connect_mongodb()
    yield
    # Close MongoDB connection when the application shuts down
    close_mongodb()

app = FastAPI(lifespan=lifespan)

app.include_router(api_router)

@app.get("/")
async def root():
    return {
        "message": "Hello World",
        "db_settings": {
            "POSTGRES_USER": db_settings.POSTGRES_USER,
            "POSTGRES_PASSWORD": db_settings.POSTGRES_PASSWORD,
            "POSTGRES_SERVER": db_settings.POSTGRES_SERVER,
            "POSTGRES_PORT": db_settings.POSTGRES_PORT,
            "POSTGRES_DATABASE": db_settings.POSTGRES_DATABASE,
        },
        "jwt_settings": {
            "JWT_SECRET": jwt_settings.JWT_SECRET,
            "JWT_ALGORITHM": jwt_settings.JWT_ALGORITHM,
            "JWT_ACCESS_TOKEN_EXPIRE_MINUTES": jwt_settings.JWT_ACCESS_TOKEN_EXPIRE_MINUTES,
        },
        "Db_URL": DATABASE_URL,
        "mongodb_settings": {
            "MONGO_SERVER": mongodb_settings.MONGO_SERVER,
            "MONGO_PORT": mongodb_settings.MONGO_PORT,
            "MONGO_DATABASE": mongodb_settings.MONGO_DATABASE,
        },
        "mongodb_url": MONGODB_URL,
        "test": await get_mongodb_database().notes.find().to_list(length=100)
    }
