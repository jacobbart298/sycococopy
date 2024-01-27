import sys
from src.core.fsmBuilder import FsmBuilder
from src.core.transition import Transition
from src.core.exceptions.illegaltransitionexception import IllegalTransitionException
from src.core.exceptions.haltedexception import HaltedException
from src.core.exceptions.sycococopyexception import SycococopyException
from src.core.exceptions.pendingmessagesexception import PendingMessagesException

'''
The monitor module is responsible for verifying that the communication between coroutines
that is forwarded by the instrumentation is in accordance with a given specification.

The specification must be passed to the monitor as a txt file on creation.
'''
class Monitor():

    # Set checkCausality to False if senders are allowed to send while there are still messages incoming.
    # Set checkLostMessages to False if the program is allowed to terminate while there are still messages that
    # haven't been received.
    def __init__(self, filePath: str, checkCausality = True):
        self.halted: bool = False
        self.checkCausality = checkCausality
        self.setExceptionHook()
        self.transitionHistory: list[tuple[Transition, any]] = []
        self.uncheckedReceives: dict[str, Transition] = {}
        self.fsm = FsmBuilder().buildFsm(filePath)

    # Destructor method. Prints error message to console if there are still messages that haven't been
    # received or if the FSM is not in a final state.
    def __del__(self):
        if not self.halted:
            fsmInFinalState: bool = self.fsm.isInFinalState()
            lostMessages: list[Transition] = []
            for uncheckedReceives in self.uncheckedReceives.values():
                lostMessages.extend(uncheckedReceives) 
            if lostMessages or not fsmInFinalState:
                print(self.buildErrorMessage(lostMessages, fsmInFinalState))

    # Checks if the given send Transition is allowed in the Monitor's FSM.
    # Throws a HaltedException if the FSM was already halted or an IllegalTransitionException if the given 
    # Transition is not allowed.    
    def verifySend(self, transition: Transition, item: any) -> None:
        if self.halted:
            raise HaltedException()     
        self.transitionHistory.append((transition, item))
        # sending is not allowed if the sender is waiting for any messages and enforceCausality is True
        if self.checkCausality and transition.getSender() in self.uncheckedReceives and self.uncheckedReceives[transition.getSender()]:
            self.halted = True
            raise PendingMessagesException(self.transitionHistory, self.uncheckedReceives[transition.getSender()])        
        transitionMade = self.fsm.makeTransition(transition, item)
        if transitionMade:
            self.addToUncheckedReceives(transition)
        else:
            self.halted = True
            raise IllegalTransitionException(self.transitionHistory)
    
    # Checks if the given receive Transition is allowed by checking if the corresponding send Transition has already occurred.
    # Returns a HaltedException if FSM was already halted or an IllegalTransitionException if the given Transition is not allowed.
    def verifyReceive(self, transition: Transition) -> any:
        if self.halted:
            raise HaltedException()
        if transition.getReceiver() in self.uncheckedReceives and transition in self.uncheckedReceives[transition.getReceiver()]:
            self.uncheckedReceives[transition.getReceiver()].remove(transition)
        else:
            self.halted = True
            raise IllegalTransitionException(self.transitionHistory)

    # Adds a transition to the receiver's list of uncheckedReceives.
    def addToUncheckedReceives(self, transition: Transition) -> None:
        if transition.getReceiver() in self.uncheckedReceives:
            self.uncheckedReceives[transition.getReceiver()].append(transition)
        else:
            self.uncheckedReceives[transition.getReceiver()] = [transition]
    
    # Method that builds the errorMessage in case the program terminates prematurely.
    def buildErrorMessage(self, lostMessages, hasTerminated):
        message: str = "\nUNEXPECTED TERMINATION!\n" 
        if not hasTerminated:
            message += "The program failed to reach the end of the protocol. Only the following messages were sent:\n"
            count: int = 1
            for transition, item in self.transitionHistory:
                message += f"\t{count}: send {transition.getType().__name__}({item}) from {transition.getSender()} to {transition.getReceiver()}\n"
                count += 1
        if len(lostMessages) > 0:
            message += "The following messages were lost:\n"
            for transition in lostMessages:
                message += f"\t{transition.getType().__name__} from {transition.getSender()} to {transition.getReceiver()}\n"
        return message

    # method that changes the standard excepthook to a sycococopy version.   
    def setExceptionHook(self) -> None:
        legacy_excepthook = sys.excepthook

        '''
        Method that provides a clear error message when the exception is caused by the framework, 
        but the normal stack trace if there was no SycococopyException.
        '''
        def exceptionHandler(type, value, traceback):
            SycococopyExceptionPresent = False
            self.halted = True
            if isinstance(value, ExceptionGroup):
                for exception in value.args[1]:
                    if isinstance(exception, SycococopyException):
                        print(str(exception))
                        SycococopyExceptionPresent = True
            elif isinstance(value, SycococopyException):
                print(str(value))
                SycococopyExceptionPresent = True
            if not SycococopyExceptionPresent:
                legacy_excepthook(type, value, traceback)
            
        # changes the default exception handler to our custom exception handler
        sys.excepthook = exceptionHandler