import sys
import traceback as tb
import asyncio as asyncio
from src.core.transition import Transition
from src.core.monitor import Monitor
from src.core.exceptions.haltedexception import HaltedException
from src.core.exceptions.illegaltransitionexception import IllegalTransitionException

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
            try:
                self.monitor.verifySend(transition, item)
                await super().put(item)
            except HaltedException:
                pass
        else:
            await super().put(item)

    async def get(self):
        if self in linked_queues:
            item = await super().get()
            transition = Transition(type(item).__name__, self.sender, self.receiver)
            try: 
                self.monitor.verifyReceive(transition)
                return item
            except HaltedException:
                pass
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
        try:
            self.monitor.verifySend(transition, item)
            await self.queue.put(item)
        except HaltedException:
            pass
    
    async def receive(self):
        item = await self.queue.get()
        transition = Transition(type(item).__name__, self.sender, self.receiver)
        try:
            self.monitor.verifyReceive(transition)
            return item
        except HaltedException:
            pass

def imposter_syndrome(type, value, traceback):
    # print("I am a bad coder ☹️")
    print(f"{type} of error has occurred, the value: {value}, and you can see traceback: {traceback}")
    tb.print_exception(exc= value, tb=traceback)

sys.excepthook = imposter_syndrome