from motor import motor_asyncio as motor
import crud
import passlib

crypt_context = passlib.context.CryptContext(schemes=["bcrypt"], deprecated="auto")

class User:
    def __init__(self, *, username: str, password: str, email: str=None):
        self.username = username
        self.password = self._get_password_hash(password)
        self.email = email
        
    # @staticmethod TODO
    # async def find_user(self, username)
        
    @staticmethod
    async def authenticate(self, login: str, password: str, session: motor.AsyncIOMotorClientSession) -> crud.Users.User|None:
        async with session.start_transaction() as transaction:
            users = crud.db.get_collection('users').find({'username': login}).to_list()
            if len(users) == 0:
                users = crud.db.get_collection('users').find({'emial': login}).to_list()
                if len(users) == 0:
                    return None
            usr = users[0]
            
        
    def _get_password_hash(self, password: str) -> str:
        return crypt_context.hash(password)
    
    def _verify_password(self, hashed_password: str, plain_password: str) -> bool:
        return crypt_context.verify(plain_password, hashed_password)
        
    def __dict__(self):
        return {
            'username': self.username,
            'password': self.password,
        }

async def create_user(
        user: dict, 
        session: motor.AsyncIOMotorClientSession
    ):    
    async with session.start_transaction(): 
        if crud.user_collection.count_documents({'username': user.username}) > 0:
            raise crud.Exceptions.AlreadyExistsException(f'User with username "{user.username}" already exists')
        await crud.user_collection.insert_one()
