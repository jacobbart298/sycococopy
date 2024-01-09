from src.core.exceptions.sycococopyexception import SycococopyException
from src.core.transition import Transition

'''
PendingMessagesException is raised when an attempt is made to send but the sender is 
required to receive pending messages first. 
'''
class PendingMessagesException(SycococopyException):

    def __init__(self, transitionHistory: list[tuple[Transition, any]], pendingMessages: list[Transition]):
        self.transitionHistory: list[tuple[Transition, any]] = transitionHistory
        self.pendingMessages: list[Transition] = pendingMessages
        
    def __str__(self) -> str:
        failedTransition, itemFailedTransition = self.transitionHistory[len(self.transitionHistory)-1]
        message: str = f"\nPENDING MESSAGE FAILURE: send {str(failedTransition.getType().__name__)}({str(itemFailedTransition)}) from {str(failedTransition.getSender())} to {str(failedTransition.getReceiver())} is not allowed, because the following messages need to be received first: \n"
        pendingMessagesCounter: int = 1
        for transition in self.pendingMessages:
            message += f"\t{str(pendingMessagesCounter)}: a message with type {str(transition.getType().__name__)} from {str(transition.getSender())}\n"
            pendingMessagesCounter +=1
        message += "\n\nThe following messages were already sent:\n"
        historyCount: int = 1
        for transition, item in self.transitionHistory:
            message += f"\t{str(historyCount)}: send {str(transition.getType().__name__)}({str(item)}) from {str(transition.getSender())} to {str(transition.getReceiver())}\n"
            historyCount += 1
        return message