import typing
from src.core.exceptions.sycococopyexception import SycococopyException
from src.core.transition import Transition

'''
IllegalTransitionException is raised when an implementation attempts to operate outside of the protocol
Takes the transition history and prints it for fault finding
'''
class IllegalTransitionException(SycococopyException):

    def __init__(self, transitionHistory: list[tuple[Transition, any]]):
        self.transitionHistory: list[tuple[Transition, any]] = transitionHistory
        
    def __str__(self) -> str:
        failedTransition, itemFailedTransition = self.transitionHistory[len(self.transitionHistory)-1]
        message: str = f"\nILLEGAL SEND: send {str(failedTransition.getType().__name__)}({str(itemFailedTransition)}) from {str(failedTransition.getSender())} to {str(failedTransition.getReceiver())} is not allowed at this point!\n"
        count: int = 1
        for transition, item in self.transitionHistory:
            message += f"\t{str(count)}: send {str(transition.getType().__name__)}({str(item)}) from {str(transition.getSender())} to {str(transition.getReceiver())}\n"
            count += 1
        return message