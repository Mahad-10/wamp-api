from autobahn.wamp import ApplicationError
from autobahn import wamp

from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from sqlalchemy.future import select

from serializers import UserSchema
from models import Base, User


class UserManager:
    def __init__(self):
        self.engine = create_async_engine(
            'sqlite+aiosqlite:///user.db',
            echo=False,
        )
        self.async_session = sessionmaker(
            self.engine, expire_on_commit=False, class_=AsyncSession, autoflush=False
        )

    async def sync_database(self):
        async with self.engine.begin() as conn:
            await conn.run_sync(Base.metadata.create_all)

    @wamp.register('com.thing.user.create', check_types=True)
    async def create(self, fullname: str, age: int, email: str, gender: str):
        user_schema = UserSchema()
        user = User(fullname=fullname, gender=gender, email=email, age=age)
        async with self.async_session() as session:
            async with session.begin():
                session.add(user)
        return user_schema.dump(user)

    @wamp.register('com.thing.user.get', check_types=True)
    async def get(self, email: str):

        query = select(User).where(User.email == email)

        async with self.async_session() as session:
            async with session.begin():
                user_schema = UserSchema()
                user = await session.execute(query)

                result = user.scalars().first()
                if result is None:
                    raise ApplicationError("com.thing.attribute_error", 'email not exists')
                response = user_schema.dump(result)
                return response
