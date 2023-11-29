from motor import motor_asyncio as motor
from os import environ as env

client = motor.AsyncIOMotorClient(env.get('DB_URI'))
db = client.get_default_database()
