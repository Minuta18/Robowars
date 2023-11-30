from motor import motor_asyncio as motor
from os import environ as env
import Exceptions

client = motor.AsyncIOMotorClient(env.get('DB_URI'))
db = client.get_default_database()

async def get_session() -> motor.AsyncIOMotorClientSession:
    async with client.start_session() as session:
        yield session

import Users
