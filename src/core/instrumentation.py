import asyncio
from transition import Transition

class Queue(asyncio.Queue):

    def __init__(self, maxsize=0):
        super().__init__(maxsize)
    
    async def put(self, item):
        transition = Transition(item.getType().__name__, self.sender, self.receiver)
        try:
            isTransitionAllowed = self.monitor.makeTransition(transition)
        except:
            print("O jee!")


        if (self.monitor.makeTransition(Transition))
        super().put(item)
    
    async def get(self):
        super().get()

    def put_nowait(item):
        super().put_nowait(item)

    def get_nowait():
        super().get_nowait()
    
    def setSender(self, sender):
        self.sender = sender
    
    def setReceiver(self, receiver):
        self.receiver = receiver

    def setMonitor(self, monitor):
        self.monitor = monitor

def initiate(queue, sender, receiver, monitor):
    queue.setSender(sender)
    queue.setReceiver(receiver)
    queue.setMonitor(monitor)