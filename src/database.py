from beanie import init_beanie
from motor.motor_asyncio import AsyncIOMotorClient
from dotenv import dotenv_values
from users.users_model import User

config = dotenv_values("../.env")
models = [User]


async def init_db():
    mongodb_client = AsyncIOMotorClient(config["MONGODB_URI"])
    mongodb_database = mongodb_client[config["DB_NAME"]]
    await init_beanie(database=mongodb_database, document_models=models)
