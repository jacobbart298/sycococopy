from antlr4 import *
from antlr4.tree.Trees import Trees
from antlr4.tree.Tree import TerminalNodeImpl
from antlrFiles.pythonicvisitor import PythonicVisitor
from src.core.fsm import FSM
from src.core.transition import Transition, PredicateTransition
from src.core.state import State
from itertools import permutations

if "." in __name__:
    from antlrFiles.PythonicParser import PythonicParser
else:
    from antlrFiles.PythonicParser import PythonicParser

# This class builds an FSM using a visitor for a parse tree produced by PythonicParser.

class FSMbuilder(PythonicVisitor):


    def __init__(self):
        self.fsm = FSM()
        self.loop_dictionary = {}
        self.roles_in_fsm = set()


    # Visit a parse tree produced by PythonicParser#specification.
    def visitSpecification(self, ctx:PythonicParser.SpecificationContext):
        self.visitProtocol(ctx.getChild(1))
        return self.fsm, self.roles_in_fsm


    # Visit a parse tree produced by PythonicParser#protocol.
    def visitProtocol(self, ctx:PythonicParser.ProtocolContext):
        expression = ctx.getChild(1).getChild(1).getChild(0)
        expression.startState = self.fsm.getStates()[0]
        expression.endState = State()
        self.visitExpression(expression) 


    # Visit a parse tree produced by PythonicParser#expression.
    def visitExpression(self, ctx:PythonicParser.ExpressionContext):
        expression = ctx.getChild(1)
        expression.startState = ctx.startState
        expression.endState = ctx.endState
        match ctx.getChild(0).getText():
            case "sequence:":
                self.visitSequence(expression)
            case "choice:":
                self.visitChoice(expression)
            case "shuffle:":
                self.visitShuffle(expression)
            case "send":
                self.visitSend(ctx)
            case "close":
                self.visitClose(ctx)
            case "loop":
                self.visitLoop(ctx)

 
    # Visit a parse tree produced by PythonicParser#sequence.
    def visitSequence(self, ctx:PythonicParser.SequenceContext):
        repeat = False
        expressionCount = ctx.getChildCount() - 2    

        # check whether last child is a repeat expression
        lastChild = ctx.getChild(expressionCount).getChild(0)
        if lastChild.getChild(0).getText() == "repeat":
            repeat = True
            expressionCount -= 1    

        currentState = ctx.startState
        expressionIndices = range(1, expressionCount + 1)    
        for index in expressionIndices:
            if index == expressionCount:
                if repeat:
                    loopTag = lastChild.getChild(1).getText() 
                    nextState =  self.loop_dictionary[loopTag]
                else:
                    nextState = ctx.endState
            else:
                nextState = State()
            expression = ctx.getChild(index).getChild(0)
            expression.startState = currentState
            expression.endState = nextState
            self.visitExpression(expression)
            currentState = nextState

    # Visit a parse tree produced by PythonicParser#shuffle.
    def visitShuffle(self, ctx:PythonicParser.ShuffleContext):
        expressionCount = ctx.getChildCount() - 2
        expressionIndices = range(1, expressionCount + 1)
        for indicesPermutation in permutations(expressionIndices):
            counter = 0
            currentState = ctx.startState
            for index in indicesPermutation:
                counter += 1
                if counter == expressionCount:
                    nextState = ctx.endState
                else:
                    nextState = State()
                expression = ctx.getChild(index).getChild(0)
                expression.startState = currentState
                expression.endState = nextState
                self.visitExpression(expression)
                currentState = nextState


    # Visit a parse tree produced by PythonicParser#choice.
    def visitChoice(self, ctx:PythonicParser.ChoiceContext):
        expressionCount = ctx.getChildCount() - 2
        expressionIndices =  range(1, expressionCount + 1)
        for index in expressionIndices:
            expression = ctx.getChild(index).getChild(0)
            expression.startState = ctx.startState
            expression.endState = ctx.endState
            self.visitExpression(expression)
    

     # Visit a parse tree produced by PythonicParser#loop.
    def visitLoop(self, ctx:PythonicParser.LoopContext):
        tag_with_semi_colon = ctx.getChild(1).getText()
        tag = tag_with_semi_colon[0:len(tag_with_semi_colon) - 1]
        self.loop_dictionary[tag] = ctx.startState
        expression = ctx.getChild(2).getChild(1).getChild(0)
        expression.startState = ctx.startState
        expression.endState = ctx.endState
        self.visitExpression(expression)


    # Visit a parse tree produced by PythonicParser#send.
    def visitSend(self, ctx:PythonicParser.SendContext):
        # build transition send without predicate
        if (ctx.getChild(2).getText() == 'from'):
            type = ctx.getChild(1).getText()
            sender = ctx.getChild(3).getText()
            receiver = ctx.getChild(5).getText()
            transition = Transition(type, sender, receiver)
        # build transition send with a non-equal predicate
        elif ctx.getChild(3).getText() in [">", "<", ">=", "<=", "!="]:
            type = ctx.getChild(1).getText()
            comparator = ctx.getChild(3).getText()
            value = ctx.getChild(4).getText()
            sender = ctx.getChild(7).getText()
            receiver = ctx.getChild(9).getText()
            value = self.stringToValue(type, value)
            transition = PredicateTransition(type, sender, receiver, comparator, value)
        # build transition send with an equal comparator
        else :
            type = ctx.getChild(1).getText()
            comparator = "=="
            stringValue = ctx.getChild(3).getText()
            sender = ctx.getChild(6).getText()
            receiver = ctx.getChild(8).getText()
            value = self.stringToValue(type, stringValue)
            transition = PredicateTransition(type, sender, receiver, comparator, value)
        # add transition to state
        ctx.startState.addTransitionToState(transition, ctx.endState)
        self.roles_in_fsm.add(sender)
        self.roles_in_fsm.add(receiver)


    # Visit a parse tree produced by PythonicParser#close.
    def visitClose(self, ctx:PythonicParser.CloseContext):
        return self.visitChildren(ctx)


    def stringToValue(self, type, string):
        match type:
            case "int":
                return int(string)
            case "float":
                return float(string)
            case "bool":
                return string == "True"
            case "str":
                return string


    def dump(self, node, depth=0, ruleNames=None):
        depthStr = '. ' * depth
        if isinstance(node, TerminalNodeImpl):
            print(f'{depthStr}{node.symbol}')
        else:
            print(f'{depthStr}{Trees.getNodeText(node, ruleNames)}')
            for child in node.children:
                self.dump(child, depth + 1, ruleNames)
    
del PythonicParser
