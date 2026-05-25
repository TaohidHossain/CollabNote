from pydantic_settings import BaseSettings, SettingsConfigDict


_base_config = SettingsConfigDict(
    env_file=".env",
    env_file_encoding="utf-8",
    extra="ignore",
    env_ignore_empty=True,
    )


class DB_Settings(BaseSettings):
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_SERVER: str
    POSTGRES_PORT: int
    POSTGRES_DATABASE: str

    model_config = _base_config

class JWT_Settings(BaseSettings):
    JWT_SECRET: str
    JWT_ALGORITHM: str
    JWT_ACCESS_TOKEN_EXPIRE_MINUTES: int

    model_config = _base_config

class MongoDB_Settings(BaseSettings):
    MONGO_SERVER: str
    MONGO_PORT: int
    MONGO_DATABASE: str

    model_config = _base_config


db_settings = DB_Settings()
jwt_settings = JWT_Settings()
mongodb_settings = MongoDB_Settings()