import asyncio

class SynchronousChannel(asyncio.Queue):
    
    def __init__(self):
        super().__init__(1)

    async def send(self, item):
        await super().put(item)
        # await receival
        await super().join()

    async def receive(self):
        item = await super().get()
        # signal receival
        super().task_done()
        return item
