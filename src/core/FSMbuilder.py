# Generated from ./Pythonic.g4 by ANTLR 4.13.1
from antlr4 import *
from antlr4.tree.Trees import Trees
from antlr4.tree.Tree import TerminalNodeImpl
from PythonicVisitor import PythonicVisitor
from fsm import FSM
from transition import Transition
from state import State

if "." in __name__:
    from .PythonicParser import PythonicParser
else:
    from PythonicParser import PythonicParser

# This class defines a complete generic visitor for a parse tree produced by PythonicParser.

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
        childCount = ctx.getChildCount()
        currentState = ctx.startState
        for i in range(1, childCount - 1):
            counter += 1
            if counter == childCount:
                nextState = ctx.endState
            else:
                nextState = State()
            child = ctx.getChild(i).getChild(0)
            child.startState = currentState
            child.endState = nextState
            self.visitExpression(child)
            currentState = nextState


    # Visit a parse tree produced by PythonicParser#shuffle.
    def visitShuffle(self, ctx:PythonicParser.ShuffleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonicParser#choice.
    def visitChoice(self, ctx:PythonicParser.ChoiceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonicParser#send.
    def visitSend(self, ctx:PythonicParser.SendContext):
        transition = Transition(ctx.getChild(1).getText(), ctx.getChild(3).getText(), ctx.getChild(5).getText())
        ctx.startState.addTransitionToState(transition, ctx.endState)
        return self.visitChildren(ctx)


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

    def dump(self, node, depth=0, ruleNames=None):
        depthStr = '. ' * depth
        if isinstance(node, TerminalNodeImpl):
            print(f'{depthStr}{node.symbol}')
        else:
            print(f'{depthStr}{Trees.getNodeText(node, ruleNames)}')
            for child in node.children:
                self.dump(child, depth + 1, ruleNames)



del PythonicParser