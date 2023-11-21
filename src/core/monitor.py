import typing
from antlr4 import *
from antlrFiles.PythonicLexer import PythonicLexer
from antlrFiles.PythonicParser import PythonicParser
from antlrFiles.PythonicErrorListener import PythonicErrorListener
from src.core.FSMbuilder import FSMbuilder
from src.core.transition import Transition, PredicateTransition
from src.core.exceptions.illegaltransitionexception import IllegalTransitionException
from src.core.exceptions.rolemismatchexception import RoleMismatchException
from src.core.exceptions.haltedexception import HaltedException
from src.core.transition import Transition
from src.core.roleBuilder import Rolebuilder
from src.core.fsm import FSM

'''
The monitor module is responsible for verifying that the communication between coroutines
that is forwarded by the instrumentation, is in accordance with a provided specification.

The specification is provided in a .txt file and must be passed to the monitor on creation.
'''

class Monitor():

    def __init__(self, filePath: str):
        self.transitionHistory: list[tuple(Transition, any)] = []
        self.uncheckedReceives: dict[str, Transition] = {}
        tree = self.buildParseTree(filePath)
        self.fsm, used_roles = FSMbuilder().visitSpecification(tree) #I Can't annotated a tuple in typing here
        defined_roles: set[str] = Rolebuilder().visitSpecification(tree)         
        if not used_roles == defined_roles:
            raise RoleMismatchException(used_roles, defined_roles)
        self.initialiseUncheckedReceives(defined_roles)
        self.halted = False

    # Function that checks if a send (Predicate)Transition is allowed in the current possible states
    # returns a HaltedException if FSM was already halted or an IllegalTransitionException if Transition is not allowed    
    def verifySend(self, transition: Transition, item: any) -> None:
        # Exceptions are not immediately raised from event loop. Halted checks if an IllegalTransitionException was raised previously
        if self.halted:
            raise HaltedException()
        self.transitionHistory.append((transition, item))
        transitionsAllowedInFSM: list[Transition] = self.fsm.checkTransition(transition)
        if transitionsAllowedInFSM:
            transitionMade: bool = False
            for allowedTransition in transitionsAllowedInFSM:
                if allowedTransition.isValid(item):
                    self.fsm.makeTransition(allowedTransition)
                    transitionMade = True
                    self.addToUncheckedReceives(allowedTransition)
            if transitionMade:
                self.fsm.updateStates()
            else:
                self.halted = True
                raise IllegalTransitionException(self.transitionHistory)
        else:
            self.halted = True
            raise IllegalTransitionException(self.transitionHistory)
    
    # Function that checks if a receive Transition is allowed by checking if a Transition to the receive was sent earlier
    # returns a HaltedException if FSM was already halted or an IllegalTransitionException if Transition is not allowed  
    def verifyReceive(self, transition: Transition) -> any:
        if self.halted:
            raise HaltedException()
        if transition in self.uncheckedReceives[transition.getReceiver()]:
            self.uncheckedReceives[transition.getReceiver()].remove(transition)
        else:
            self.halted = True
            raise IllegalTransitionException(self.transitionHistory)

    # Function that initiatialises the dictionary of unCheckReceives with an empty list for each role
    def initialiseUncheckedReceives(self, roles: set[str]):
        for role in roles:
            self.uncheckedReceives[role] = []

    # Function that adds a transition to the receiver's list of uncheckReceives
    def addToUncheckedReceives(self, transition: Transition) -> None:
        # create a Transition, so a PredicateTransition is treated equally in the receives
        uncheckedReceive: Transition = Transition(transition.getType(), transition.getSender(), transition.getReceiver())
        self.uncheckedReceives[transition.getReceiver()].append(uncheckedReceive)

    # Function that parses the given specification in the filePath to a parse tree
    def buildParseTree(self, filePath: str):
        input = FileStream(filePath)
        lexer = PythonicLexer(input)
        stream = CommonTokenStream(lexer)
        parser = PythonicParser(stream)
        return parser.specification() 
    