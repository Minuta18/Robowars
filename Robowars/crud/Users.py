from motor import motor_asyncio as motor
import pydantic
import crud
import typing
import bson

class User(pydantic.BaseModel):
    id: typing.Optional[crud.PyObjectId] = pydantic.Field(alias='_id', default=None)
    username: str = pydantic.Field(...)
    email: str = pydantic.Field(...)
    hashed_password: str = pydantic.Field(...)

async def create_user(*, user: User):
    '''
    Creates a new user
    '''
    new_user = await crud.user_collection.insert_one(
        user.model_dump(by_alias=True, exclude=['id'])
    )
    created_user = await crud.user_collection.find_one({
        '_id': new_user.inserted_id,    
    })
    return created_user

async def get_users(*, start_index: int, page_size: int): # TODO
    '''
    Returns multiple users
    '''
    return await crud.user_collection.find().to_list()

async def get_user(*, id: str):
    '''
    Retruns single user
    '''
    return await crud.user_collection.find_one({'_id': bson.ObjectId(id)})

async def update_user(*, id: str, new_user: User):
    '''
    Edits user 
    ''' # TODO
