import asyncio as asyncio
from src.core.transition import Transition
from src.core.monitor import Monitor
from src.core.exceptions.haltedexception import HaltedException

'''
The instrumentation module is responsible for sending all related communication between coroutines
to the monitor, so it can be checked against a protocol.

The module offers two classes: 
1. Queue, which overrides the asyncio Queue so the instrumentation can be
used as a drop in replacement for the asyncio library (simply import the instrumentation as asyncio)
2. Channel, which provides a more intuitive way of sending messages between coroutines
'''

# list of queues that are linked to the monitor.
linked_queues: set[asyncio.Queue] = set()

# Function that links a Queue to a sender, receiver and monitor.
def link(queue: asyncio.Queue, sender: str, receiver: str, monitor: Monitor) -> None:
    queue.sender = sender
    queue.receiver = receiver
    queue.monitor = monitor
    linked_queues.add(queue)

# Function required to pass all non-monitor related asyncio calls through to asyncio.
def __getattr__(name):
    return getattr(asyncio, name)

# Class that overrides asyncio.Queue to allow instrumentation to be used as drop in replacement.
class Queue(asyncio.Queue):

    '''
    If the Queue is linked to the monitor, the put function forwards the message to the
    monitor to verify that is is allowed by the protocol before adding the item on the
    Queue. The monitor raises a HaltedException if it was already halted by a previous 
    attempt to send.

    If the Queue is not linked, the put operation is handled by the asyncio library.
    '''
    async def put(self, item: any) -> None:
        if self in linked_queues:
            transition: Transition = Transition(type(item), self.sender, self.receiver)
            try:
                self.monitor.verifySend(transition, item)
                await super().put(item)
            except HaltedException:
                pass
        else:
            await super().put(item)

    '''
    If the Queue is linked to the monitor, the get function forwards the message to the
    monitor to verify that the message is allowed to be received by the protocol before taking the item 
    from the Queue. The monitor raises a HaltedException if it was already halted by a previous 
    attempt to send.

    If the Queue is not linked, the get operation is handled by the asyncio library.
    '''
    async def get(self) -> any:
        if self in linked_queues:
            item: any = await super().get()
            transition: Transition = Transition(type(item), self.sender, self.receiver)
            try: 
                self.monitor.verifyReceive(transition)
                return item
            except HaltedException:
                pass
        else:
            return await super().get()


# Class that provides an intuitive way of sending messages between coroutines.
class Channel():

    '''
    Underlying structure uses an asyncio.Queue for the communication. Default maxsize is set to 0 (unlimited),
    but a user can override as required
    '''
    def __init__(self, sender: str, receiver: str, monitor: Monitor, maxsize=0):
        self.queue = asyncio.Queue(maxsize)
        self.sender = sender
        self.receiver = receiver
        self.monitor = monitor
    
    # Checks if send is allowed by the monitor and, if so, adds item to the queue.
    async def send(self, item: any) -> None:
        transition: Transition = Transition(type(item), self.sender, self.receiver)
        try:
            self.monitor.verifySend(transition, item)
            await self.queue.put(item)
        except HaltedException:
            pass
    
    # Checks if receive is allowed by the monitor and, if so, returns the item from the queue.
    async def receive(self) -> any:
        item: any = await self.queue.get()
        transition: Transition = Transition(type(item), self.sender, self.receiver)
        try:
            self.monitor.verifyReceive(transition)
            return item
        except HaltedException:
            pass

    # Checks whether the channel is empty. Returns True if it is, otherwise False.   
    def empty(self) -> bool:
        return self.queue.empty()
    
    # Checks whether the channel is full. Returns True if it is, otherwise False.   
    def full(self) -> bool:
        return self.queue.full()
    
    # Returns the number of items in the channel
    def size(self) -> int:
        return self.queue.qsize()
