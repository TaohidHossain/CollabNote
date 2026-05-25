from motor.motor_asyncio import AsyncIOMotorClient
from app.core.config import mongodb_settings

MONGODB_URL = f"mongodb://{mongodb_settings.MONGO_SERVER}:{mongodb_settings.MONGO_PORT}"

client: AsyncIOMotorClient = None
database = None

def connect_mongodb():
    global client, database
    if client is None:
        client = AsyncIOMotorClient(MONGODB_URL)
    database = client[mongodb_settings.MONGO_DATABASE]

def close_mongodb():
    global client
    if client is not None:
        client.close()
        client = None

def get_mongodb_database():
    return database