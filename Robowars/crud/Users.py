from motor import motor_asyncio as motor
from crud import Exceptions
import pymongo
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
    new_user = await crud.user_collection.insert_one(
        user.model_dump(by_alias=True, exclude=['id'])
    )
    created_user = await crud.user_collection.find_one({
        '_id': new_user.inserted_id,    
    })
    return created_user

async def get_user(*, id: str):
    return await crud.user_collection.find_one({'_id': bson.ObjectId(id)})

async def update_user(*, id: str, new_user: User):
    update_result = await crud.user_collection.find_one_and_update(
        {'_id': bson.ObjectId(id)},
        {'$set': new_user.model_dump()},
        return_document=pymongo.ReturnDocument.AFTER,
    )
    
    if update_result is not None:
        return update_result
    else:
        raise Exceptions.NotFoundException(f'User(id={id}) not found')
    
async def delete_user(*, id: str):
    delete_res = await crud.user_collection.delete_one(id={'_id': bson.ObjectId(id)})
    
    if delete_res.deleted_count != 1:
        raise Exceptions.NotFoundException(f'User(id={id}) not found')
