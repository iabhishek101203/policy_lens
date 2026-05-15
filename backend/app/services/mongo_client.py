from motor.motor_asyncio import AsyncIOMotorClient
from app.core.config import settings

client = None
db = None


async def init_mongo():
    global client, db
    client = AsyncIOMotorClient(settings.mongodb_uri)
    db = client[settings.mongodb_db]
    await client.server_info()


def get_policy_collection():
    return db["policies"]


def get_user_collection():
    return db["users"]
