from antlr4 import *
from antlrFiles.PythonicLexer import PythonicLexer
from antlrFiles.PythonicParser import PythonicParser
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
        
    def verifySend(self, transition: Transition):
        self.transitionHistory.append(transition)
        transitionAllowed = self.fsm.checkTransition(transition) and self.uncheckedReceives[transition.getSender()] == []
        if transitionAllowed:
            self.fsm.makeTransition(transition)
            self.uncheckedReceives[transition.getReceiver()].append(transition)
        else:
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
        print(f"File path = {filePath}")
        input = FileStream(filePath)
        lexer = PythonicLexer(input)
        stream = CommonTokenStream(lexer)
        parser = PythonicParser(stream)
        tree = parser.specification() 
        fsm_builder = FSMbuilder()
        return fsm_builder.visitSpecification(tree)
    