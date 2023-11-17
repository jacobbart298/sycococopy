import sys
import traceback as tb
import logging
import asyncio as asyncio
from src.core.transition import Transition
from src.core.monitor import Monitor
from src.core.exceptions.haltedexception import HaltedException
from src.core.exceptions.illegaltransitionexception import IllegalTransitionException

'''
The instrumentation module is responsible for sending all related communication between coroutines
to the monitor, so it can be checked against a protocol.

The module offers two classes: 
1. Queue, which overrides the asyncio Queue so the instrumentation can be
used as a drop in replacement for the asyncio library (simply import the instrumentation as asyncio)
2. Channel, which provides a more intuitive way of sending messages between coroutines
'''

# list of queues that are linked to the monitor
linked_queues = []

# Function that links a Queue to a sender, receiver and monitor
def link(queue: asyncio.Queue, sender: str, receiver: str, monitor: Monitor):
    queue.sender = sender
    queue.receiver = receiver
    queue.monitor = monitor
    linked_queues.append(queue)

# Function required to pass all non-monitor related asyncio calls through to asyncio   
def __getattr__(name):
    return getattr(asyncio, name)

# Class that overrides asyncio.Queue to allow instrumentation to be used as drop in replacement
class Queue(asyncio.Queue):

    '''
    If the Queue is linked to the monitor, the put function forwards the message to the
    monitor to verify that is is allowed by the protocol before adding the item on the
    Queue. The monitor throws an IllegalTransitionException if the put operation is not allowed.

    If the Queue is not linked, the put operation is handled by the asyncio library.
    '''
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


    '''
    If the Queue is linked to the monitor, the get function forwards the message to the
    monitor to verify that the message is allowed to be received by the protocol before taking the item 
    from the Queue. The monitor throws an IllegalTransitionException if the get operation is not allowed.

    If the Queue is not linked, the get operation is handled by the asyncio library.
    '''
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

# Class that provides an intuitive way of sending messages between coroutines
class Channel():

    '''
    Underlying structure uses an asyncio.Queue for the communication. Default maxsize is set to 0 (unlimited),
    but a user can override as required
    '''
    def __init__(self, sender, receiver, monitor: Monitor, maxsize=0):
        self.queue = asyncio.Queue(maxsize)
        self.sender = sender
        self.receiver = receiver
        self.monitor = monitor
    
    # Function that checks is send is allowed by the monitor and, if so, adds item to the queue
    async def send(self, item):
        transition = Transition(type(item).__name__, self.sender, self.receiver)
        try:
            self.monitor.verifySend(transition, item)
            await self.queue.put(item)
        except HaltedException:
            pass
    
    # Function that checks if receive is allowed by the monitor and, if so, returns the item on the queue
    async def receive(self):
        item = await self.queue.get()
        transition = Transition(type(item).__name__, self.sender, self.receiver)
        try:
            self.monitor.verifyReceive(transition)
            return item
        except HaltedException:
            pass
    
    def close(self):
        pass


legacy_excepthook = sys.excepthook

'''
Function that provides a clean print of the transition history on an illegal transition, 
but the normal stack trace if there was no IllegalTransitionException
'''
def exceptionHandler(type, value, traceback):
    noIllegalTransitionPresent = True
    for exception in value.args[1]:
        if isinstance(exception, IllegalTransitionException):
            print(str(exception))
            noIllegalTransitionPresent = False
    if noIllegalTransitionPresent:
        legacy_excepthook(type, value, traceback)
        

# changes standard Python interperter Exception handler to our exception handler
sys.excepthook = exceptionHandler