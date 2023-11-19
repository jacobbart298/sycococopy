from antlr4 import *
from antlrFiles.PythonicLexer import PythonicLexer
from antlrFiles.PythonicParser import PythonicParser
from src.core.FSMbuilder import FSMbuilder
from src.core.transition import Transition, PredicateTransition
from src.core.transition import Transition
from src.core.roleBuilder import Rolebuilder
from src.core.exceptions.illegaltransitionexception import IllegalTransitionException
from src.core.exceptions.rolemismatchexception import RoleMismatchException
from src.core.exceptions.haltedexception import HaltedException

class Monitor():

    def __init__(self, filePath):
        self.transitionHistory = []
        self.uncheckedReceives = {}
        tree = self.buildParseTree(filePath)
        self.fsm, used_roles = FSMbuilder().visitSpecification(tree)
        defined_roles = Rolebuilder().visitSpecification(tree)         
        if not used_roles == defined_roles:
            raise RoleMismatchException(used_roles, defined_roles)
        self.initialiseUncheckedReceives(defined_roles)
        self.halted = False
        
    def verifySend(self, transition: Transition, item):
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
    
    def verifyReceive(self, transition: Transition):
        if self.halted:
            raise HaltedException()
        if transition in self.uncheckedReceives[transition.getReceiver()]:
            self.uncheckedReceives[transition.getReceiver()].remove(transition)
        else:
            self.halted = True
            raise IllegalTransitionException(self.transitionHistory)

    def initialiseUncheckedReceives(self, roles):
        for role in roles:
            self.uncheckedReceives[role] = []

    def addToUncheckedReceives(self, transition: Transition):
        uncheckedReceive = Transition(transition.getType(), transition.getSender(), transition.getReceiver())
        self.uncheckedReceives[transition.getReceiver()].append(uncheckedReceive)

    def buildParseTree(self, filePath):
        input = FileStream(filePath)
        lexer = PythonicLexer(input)
        stream = CommonTokenStream(lexer)
        parser = PythonicParser(stream)
        return parser.specification() 
    