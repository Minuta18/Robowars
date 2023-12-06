from motor import motor_asyncio as motor
from os import environ as env
import Exceptions
import passlib
import pydantic
import typing_extensions

client = motor.AsyncIOMotorClient(env.get('DB_URI'))
db = client.get_default_database()
user_collection = db.get_collection('users')

crypt_context = passlib.context.CryptContext(schemes=["bcrypt"], deprecated="auto")
PyObjectId = typing_extensions.Annotated[str, 
    pydantic.functional_validators.BeforeValidator]

async def get_session() -> motor.AsyncIOMotorClientSession:
    async with client.start_session() as session:
        yield session

import Users
