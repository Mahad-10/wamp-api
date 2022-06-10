import txaio
import uvloop

uvloop.install() # noqa
txaio.use_asyncio() # noqa

from autobahn.asyncio.wamp import ApplicationSession, ApplicationRunner
from apis import UserManager


class UserAccount(ApplicationSession):
    async def onJoin(self, details):
        user_manager = UserManager()
        await user_manager.sync_database()

        regs = await self.register(user_manager)
        for reg in regs:
            print("Procedure registered: ", reg.procedure)
        print('Methods are registered; ready for frontend.')


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    runner = ApplicationRunner('ws://0.0.0.0:8080/ws', 'realm1')
    runner.run(UserAccount)

