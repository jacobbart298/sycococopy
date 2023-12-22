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

    def __init__(self, filePath: str):
        self.halted: bool = False
        self.setExceptionHook()
        self.transitionHistory: list[tuple[Transition, any]] = []
        self.uncheckedReceives: dict[str, Transition] = {}
        self.fsm = FsmBuilder().buildFsm(filePath)

    # Destructor method. Note that a destructor does not raise but silences exceptions.
    def __del__(self):
        if not self.halted:
            fsmInFinalState: bool = self.fsm.inFinalState()
            lostMessages: list[Transition] = []
            for uncheckedReceives in self.uncheckedReceives.values():
                lostMessages.extend(uncheckedReceives) 
            if lostMessages or not fsmInFinalState:
                print(self.buildErrorMessage(lostMessages, fsmInFinalState))

    # Checks if the given send Transition is allowed in the Monitor's FSM.
    # Throws a HaltedException if the FSM was already halted or an IllegalTransitionException if the given Transition is not allowed.    
    def verifySend(self, transition: Transition, item: any) -> None:
        if self.halted:
            raise HaltedException()     
        self.transitionHistory.append((transition, item))
        # sending is not allowed if the sender is waiting for any messages
        if transition.getSender() in self.uncheckedReceives and self.uncheckedReceives[transition.getSender()]:
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

    # Initiatialises the dictionary of uncheckedReceives with an empty list for each role.
    def initialiseUncheckedReceives(self, roles: set[str]):
        for role in roles:
            self.uncheckedReceives[role] = []

    # Adds a transition to the receiver's list of uncheckedReceives.
    def addToUncheckedReceives(self, transition: Transition) -> None:
        if transition.getReceiver() in self.uncheckedReceives:
            self.uncheckedReceives[transition.getReceiver()].append(transition)
        else:
            self.uncheckedReceives[transition.getReceiver()] = [transition]
    
    # Function that builds the errorMessage in case the program terminates prematurely.
    def buildErrorMessage(self, lostMessages, hasTerminated):
        message: str = "\nUNEXPECTED TERMINATION:" 
        if not hasTerminated:
            message += "\nProgram failed to reach end of protocol!\n"
            count: int = 1
            for transition, item in self.transitionHistory:
                message += f"{str(count)}: send {str(transition.getType())}({str(item)}) from {str(transition.getSender())} to {str(transition.getReceiver())}\n"
                count += 1
        if len(lostMessages) > 0:
            message += "\nThe following messages were lost:\n"
            for transition in lostMessages:
                message += f"{str(transition.getReceiver())} is waiting for a message of type {str(transition.getType())} from {str(transition.getSender())}\n"
        return message
        
    def setExceptionHook(self) -> None:
        legacy_excepthook = sys.excepthook

        '''
        Function that provides a clean print of the transition history on an illegal transition, 
        but the normal stack trace if there was no IllegalTransitionException
        '''
        def exceptionHandler(type, value, traceback):
            noSycocopyExceptionPresent = True
            self.halted = True
            if isinstance(value, ExceptionGroup):
                for exception in value.args[1]:
                    if isinstance(exception, SycococopyException):
                        print(str(exception))
                        noSycocopyExceptionPresent = False
            elif isinstance(value, SycococopyException):
                print(str(value))
                noSycocopyExceptionPresent = False
            if noSycocopyExceptionPresent:
                legacy_excepthook(type, value, traceback)
            
        # changes standard Python interperter Exception handler to our exception handler
        sys.excepthook = exceptionHandler