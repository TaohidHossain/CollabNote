from fastapi import FastAPI

from app.config import db_settings, jwt_settings

app = FastAPI()

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
        }
    }
