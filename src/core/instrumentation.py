from asyncio import Queue
from src.core.transition import Transition

class Channel():

    def __init__(self, sender, receiver, maxsize):
        self.queue = Queue(maxsize)
    
    async def send(self, item):
        transition = Transition(item.getType().__name__, self.sender, self.receiver)
        if self.monitor.checkTransition(transition):
            self.monitor.makeTransition(transition)
             #throws an exception from FSM if wrong, for now no try / catch as the exception already halt program
            await self.queue.put(item)
        else:
            print("INVALID SEND")
    
    async def receive(self):
        item = await self.queue.get()
        transition = Transition(item.getType().__name__, self.sender, self.receiver)
        if self.monitor.checkReceive(transition):
            self.monitor.removeFromUncheckedReceives(transition)
            return item
        else:
            print("INVALID RECEIVE")
    
    def setSender(self, sender):
        self.sender = sender
    
    def setReceiver(self, receiver):
        self.receiver = receiver

    def setMonitor(self, monitor):
        self.monitor = monitor
        
    def initialise(self, sender, receiver, monitor):
        self.setSender(sender)
        self.setReceiver(receiver)
        self.setMonitor(monitor)