from PythonicVisitor import PythonicVisitor
from fsm import FSM
from transition import Transition
from state import State
from itertools import permutations

if "." in __name__:
    from .PythonicParser import PythonicParser
else:
    from PythonicParser import PythonicParser

# This class builds an FSM using a visitor for a parse tree produced by PythonicParser.

class FSMbuilder(PythonicVisitor):

    def __init__(self):
        self.fsm = FSM()

    # Visit a parse tree produced by PythonicParser#specification.
    def visitSpecification(self, ctx:PythonicParser.SpecificationContext):
        self.visitChildren(ctx)
        return self.fsm


    # Visit a parse tree produced by PythonicParser#protocol.
    def visitProtocol(self, ctx:PythonicParser.ProtocolContext):       
        expression = ctx.getChild(3).getChild(1).getChild(0)
        expression.startState = self.fsm.getState()
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


    # Visit a parse tree produced by PythonicParser#sequence.
    def visitSequence(self, ctx:PythonicParser.SequenceContext):
        counter = 0
        currentState = ctx.startState
        expressionCount = ctx.getChildCount() - 2
        expressionIndices =  range(1, expressionCount + 1)
        for index in expressionIndices:
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
    

    # Visit a parse tree produced by PythonicParser#send.
    def visitSend(self, ctx:PythonicParser.SendContext):
        type = ctx.getChild(1).getText()
        sender = ctx.getChild(3).getText()
        receiver = ctx.getChild(5).getText()
        transition = Transition(type, sender, receiver)
        ctx.startState.addTransitionToState(transition, ctx.endState)


    # Visit a parse tree produced by PythonicParser#close.
    def visitClose(self, ctx:PythonicParser.CloseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonicParser#block.
    def visitBlock(self, ctx:PythonicParser.BlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonicParser#role.
    def visitRole(self, ctx:PythonicParser.RoleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonicParser#roles.
    def visitRoles(self, ctx:PythonicParser.RolesContext):
        return self.visitChildren(ctx)

del PythonicParser
