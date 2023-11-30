from motor import motor_asyncio as motor
import crud

async def create_user(
        user: dict, 
        session: motor.AsyncIOMotorClientSession
    ):    
    async with session.start_transaction(): 
        if crud.user_collection.count_documents({'username': user.username}) > 0:
            raise 
        await crud.user_collection.insert_one()
