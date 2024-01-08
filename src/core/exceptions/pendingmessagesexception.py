import typing
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
        failedTransition, itemFailedTransition = self.transitionHistory[len(self.transitionHistory) - 1]
        message: str = f"\nPENDING MESSAGE FAILURE: send {failedTransition.getType().__name__}({itemFailedTransition}) from {failedTransition.getSender()} to {failedTransition.getReceiver()} is not allowed.\nThe sender needs to receive the following messages first:\n"
        pendingMessagesCounter: int = 1
        for transition in self.pendingMessages:
            message += f"\t{pendingMessagesCounter}: a message with type {transition.getType().__name__} from {transition.getSender()}\n"
            pendingMessagesCounter += 1
        message += "The following messages were already sent:\n"
        historyCount: int = 1
        for transition, item in self.transitionHistory:
            message += f"\t{str(historyCount)}: send {transition.getType().__name__}({item}) from {transition.getSender()} to {transition.getReceiver()}\n"
            historyCount += 1
        return message