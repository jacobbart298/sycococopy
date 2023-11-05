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
        # Exceptions are not immediately raised from event loop. Halted checks if exception was raised already
        if self.halted:
            raise HaltedException()
        self.transitionHistory.append((transition, item))
        transitionsAllowedInFSM = self.fsm.checkTransition(transition)
        if transitionsAllowedInFSM:
            transitionMade = False
            for allowedTransition in transitionsAllowedInFSM:
                if isinstance(allowedTransition, PredicateTransition):
                    if self.checkPredicate(allowedTransition.getComparator(), item, allowedTransition.getValue()):
                        self.fsm.makeTransition(allowedTransition)
                        transitionMade = True
                        self.uncheckedReceives[allowedTransition.getReceiver()].append(allowedTransition.toSuper())
                    else:
                        self.fsm.removePredicateTransition(allowedTransition)
                else:
                    self.fsm.makeTransition(allowedTransition)
                    transitionMade = True
                    self.uncheckedReceives[allowedTransition.getReceiver()].append(allowedTransition)
            if transitionMade:
                self.fsm.updateStates()
            else:
                self.halted = True
                raise IllegalTransitionException(self.transitionHistory)
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

    def checkPredicate(self, operator, value1, value2):
        match operator:
            case '<':
                return value1 < value2
            case '<=':
                return value1 <= value2
            case '>':
                return value1 > value2
            case '>=':
                return value1 >= value2
            case '!=':
                return value1 != value2
            case '==':
                return value1 == value2

    def buildParseTree(self, filePath):
        input = FileStream(filePath)
        lexer = PythonicLexer(input)
        stream = CommonTokenStream(lexer)
        parser = PythonicParser(stream)
        # Remove the default error listener, so we don't output to terminal automatically
        # parser.removeErrorListeners()
        # Add our own ErrorListener
        # parser.addErrorListener(PythonicErrorListener())
        return parser.specification() 
    