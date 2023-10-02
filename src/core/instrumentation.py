from asyncio import Queue
from src.core.transition import Transition
from src.core.monitor import Monitor

class Channel():

    def __init__(self, sender, receiver, monitor: Monitor, maxsize):
        self.queue = Queue(maxsize)
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
