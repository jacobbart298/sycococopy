import typing
from antlr4 import *
from antlrFiles.PythonicLexer import PythonicLexer
from antlrFiles.PythonicParser import PythonicParser
from src.core.FSMbuilder import FSMbuilder
from src.core.transition import Transition
from src.core.roleBuilder import Rolebuilder
from src.core.fsm import FSM
from src.core.exceptions.illegaltransitionexception import IllegalTransitionException
from src.core.exceptions.rolemismatchexception import RoleMismatchException
from src.core.exceptions.haltedexception import HaltedException

'''
The monitor module is responsible for verifying that the communication between coroutines
that is forwarded by the instrumentation is in accordance with a given specification.

The specification must be passed to the monitor as a txt file on creation.
'''

class Monitor():

    def __init__(self, filePath: str):
        self.transitionHistory: list[tuple[Transition, any]] = []
        self.uncheckedReceives: dict[str, Transition] = {}
        tree = self.buildParseTree(filePath)
        self.fsm, used_roles = FSMbuilder().visitSpecification(tree)
        defined_roles: set[str] = Rolebuilder().visitSpecification(tree)         
        if not used_roles == defined_roles:
            raise RoleMismatchException(used_roles, defined_roles)
        self.initialiseUncheckedReceives(defined_roles)
        self.halted: bool = False

    # Checks if the given send Transition is allowed in the Monitor's FSM.
    # Throws a HaltedException if the FSM was already halted or an IllegalTransitionException if the given Transition is not allowed.    
    def verifySend(self, transition: Transition, item: any) -> None:
        if self.halted:
            raise HaltedException()     
        self.transitionHistory.append((transition, item))
        # sending is not allowed if the sender is waiting for any messages
        if self.uncheckedReceives[transition.getSender()]:
            self.halted = True
            raise IllegalTransitionException(self.transitionHistory)        
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
        if transition in self.uncheckedReceives[transition.getReceiver()]:
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
        uncheckedReceive: Transition = Transition(transition.getType(), transition.getSender(), transition.getReceiver())
        self.uncheckedReceives[transition.getReceiver()].append(uncheckedReceive)

    # Parses the given specification in the filePath to a parse tree.
    def buildParseTree(self, filePath: str):
        input = FileStream(filePath)
        lexer = PythonicLexer(input)
        stream = CommonTokenStream(lexer)
        parser = PythonicParser(stream)
        return parser.specification() 
    