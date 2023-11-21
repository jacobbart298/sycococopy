import typing
from src.core.transition import Transition

'''
IllegalTransitionException is raised when an implementation attempts to operate outside of the protocol
Takes the transition history and prints it for fault finding
'''
class IllegalTransitionException(Exception):

    def __init__(self, transitionHistory: list[tuple(Transition, any)]):
        self.transitionHistory: list[tuple(Transition, any)] = transitionHistory
        
    def __str__(self) -> str:
        failedTransition, itemFailedTransition = self.transitionHistory[len(self.transitionHistory)-1]
        message: str = f"\nTRANSITION FAILURE: send {str(failedTransition.getType())}({str(itemFailedTransition)}) from {str(failedTransition.getSender())} to {str(failedTransition.getReceiver())} is not enabled in current state!\n"
        count: int = 1
        for transition, item in self.transitionHistory:
            message += f"{str(count)}: send {str(transition.getType())}({str(item)}) from {str(transition.getSender())} to {str(transition.getReceiver())}\n"
            count += 1
        return message