from src.core.exceptions.sycococopyexception import SycococopyException
from src.core.transition import Transition

'''
IllegalTransitionException is raised when an illegal send or receive operation occurs.
'''
class IllegalTransitionException(SycococopyException):

    def __init__(self, transitionHistory: list[tuple[Transition, any]]):
        self.transitionHistory: list[tuple[Transition, any]] = transitionHistory
        
    def __str__(self) -> str:
        failedTransition, failedTransitionTtem = self.transitionHistory[len(self.transitionHistory) - 1]
        message: str = f"\nILLEGAL SEND: send {failedTransition.getType().__name__}({failedTransitionTtem}) from {failedTransition.getSender()} to {failedTransition.getReceiver()} is not allowed at this point!\n"
        count: int = 1
        for transition, item in self.transitionHistory:
            message += f"\t{count}: send {transition.getType().__name__}({item}) from {transition.getSender()} to {transition.getReceiver()}\n"
            count += 1
        return message