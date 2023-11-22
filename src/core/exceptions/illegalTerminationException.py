import typing
from src.core.transition import Transition

class IllegalTerminationException(Exception):

    def __init__(self, transitionHistory, lostMessages, hasTerminated):
        self.transitionHistory: list[tuple[Transition, any]] = transitionHistory
        self.lostMessages: list[Transition] = lostMessages
        self.hasTerminated = hasTerminated

    def __str__(self) -> str:
        message: str = "\nUNEXPECTED TERMINATION:" 
        if not self.hasTerminated:
            message += "\nProgram failed to reach end of protocol!\n"
            count: int = 1
            for transition, item in self.transitionHistory:
                message += f"{str(count)}: send {str(transition.getType())}({str(item)}) from {str(transition.getSender())} to {str(transition.getReceiver())}\n"
                count += 1
        if len(self.lostMessages) > 0:
            message += "\nThe following messages were lost:\n"
            for transition in self.lostMessages:
                message += f"{str(transition.getReceiver())} is waiting for a message of type {str(transition.getType())} from {str(transition.getSender())}\n"
        return message