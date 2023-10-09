import asyncio as asyncio
from src.core.transition import Transition
from src.core.monitor import Monitor

linked_queues = []

def link(queue: asyncio.Queue, sender: str, receiver: str, monitor: Monitor):
    queue.sender = sender
    queue.receiver = receiver
    queue.monitor = monitor
    linked_queues.append(queue)
    
def __getattr__(name):
    return getattr(asyncio, name)

class Queue(asyncio.Queue):

    async def put(self, item):
        if self in linked_queues:
            transition = Transition(type(item).__name__, self.sender, self.receiver)
            self.monitor.verifySend(transition)
            #throws an exception from monitor if wrong
            await super().put(item)
        else:
            await super().put(item)

    async def get(self):
        if self in linked_queues:
            item = await super().get()
            transition = Transition(type(item).__name__, self.sender, self.receiver)
            self.monitor.verifyReceive(transition)
            return item
        else:
            return await super().get()

class Channel():

    def __init__(self, sender, receiver, monitor: Monitor, maxsize=0):
        self.queue = asyncio.Queue(maxsize)
        self.sender = sender
        self.receiver = receiver
        self.monitor = monitor
    
    async def send(self, item):
        transition = Transition(type(item).__name__, self.sender, self.receiver)
        self.monitor.verifySend(transition)
        #throws an exception from monitor if wrong
        await self.queue.put(item)
    
    async def receive(self):
        item = await self.queue.get()
        transition = Transition(type(item).__name__, self.sender, self.receiver)
        self.monitor.verifyReceive(transition)
        return item