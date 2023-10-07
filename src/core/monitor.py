from antlr4 import *
from antlrFiles.PythonicLexer import PythonicLexer
from antlrFiles.PythonicParser import PythonicParser
from antlrFiles.PythonicErrorListener import PythonicErrorListener
from src.core.FSMbuilder import FSMbuilder
from src.core.transition import Transition
from src.core.exceptions.illegaltransitionexception import IllegalTransitionException
from src.core.transition import Transition

class Monitor():

    def __init__(self, filePath):
        self.transitionHistory = []
        self.uncheckedReceives = {}
        self.fsm, roles = self.buildFSM(filePath)
        self.initialiseUncheckedReceives(roles)
        self.halted = False
        
    def verifySend(self, transition: Transition):
        # Exceptions are not immediately raised from event loop. Halted checks if exception was raised already
        if self.halted:
            return
        self.transitionHistory.append(transition)
        transitionAllowed = self.fsm.checkTransition(transition) and self.uncheckedReceives[transition.getSender()] == []
        if transitionAllowed:
            self.fsm.makeTransition(transition)
            self.uncheckedReceives[transition.getReceiver()].append(transition)
        else:
            self.halted = True
            raise IllegalTransitionException(self.transitionHistory)
    
    def verifyReceive(self, transition: Transition):
        if transition in self.uncheckedReceives[transition.getReceiver()]:
            self.uncheckedReceives[transition.getReceiver()].remove(transition)
        else:
            raise IllegalTransitionException(self.transitionHistory)

    def initialiseUncheckedReceives(self, roles):
        for role in roles:
            self.uncheckedReceives[role] = []

    def buildFSM(self, filePath):
        input = FileStream(filePath)
        lexer = PythonicLexer(input)
        stream = CommonTokenStream(lexer)
        parser = PythonicParser(stream)
        # Remove the default error listener, so we don't output to terminal automatically
        parser.removeErrorListeners()
        # Add our own ErrorListener
        parser.addErrorListener(PythonicErrorListener())
        tree = parser.specification() 
        fsm_builder = FSMbuilder()
        return fsm_builder.visitSpecification(tree)
    