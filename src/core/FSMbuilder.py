# Generated from ./Pythonic.g4 by ANTLR 4.13.1
from antlr4 import *
from antlr4.tree.Trees import Trees
from antlr4.tree.Tree import TerminalNodeImpl
from PythonicVisitor import PythonicVisitor
from fsm import FSM

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
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonicParser#protocol.
    def visitProtocol(self, ctx:PythonicParser.ProtocolContext):
        # count = ctx.getChildCount()
        # print(f"In protocol met {count} kinderen")
        # block = ctx.getChild(3)
        # expression = block.getChild(1).getChild(0)
        # print(f"We hebben dan een {expression.getChild(0).getText()}")
        # print(f"In expressie met {expression.getChildCount()} kinderen")
        # for i in range(expression.getChildCount()):
        #     print(expression.getChild(i).getText())
       
        expression = ctx.getChild(3).getChild(1).getChild(0)
        print(f"In protocol en ik geef {expression.getText()} aan visitExpression")
        expression.extraAttribuut = "EVEN TESTEN"
        self.visitExpression(expression)
        # print(f"ik ga controleren op {expression.getChild}")      


    # Visit a parse tree produced by PythonicParser#expression.
    def visitExpression(self, ctx:PythonicParser.ExpressionContext):
        print(ctx.getChild(0).getText())
        match ctx.getChild(0).getText():
            case "sequence:":
                self.visitSequence(ctx)
            case "choice:":
                self.visitChoice(ctx)
            case "shuffle:":
                self.visitShuffle(ctx)
            case "send":
                self.visitSend(ctx)

    # Visit a parse tree produced by PythonicParser#sequence.
    def visitSequence(self, ctx:PythonicParser.SequenceContext):
        expression = ctx.getChild(1)
        for i in range(expression.getChildCount()):
            print(f"kind nummer {i} is {expression.getChild(i).getText()}")
            # self.visitExpression(expression)
        # return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonicParser#shuffle.
    def visitShuffle(self, ctx:PythonicParser.ShuffleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonicParser#choice.
    def visitChoice(self, ctx:PythonicParser.ChoiceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonicParser#send.
    def visitSend(self, ctx:PythonicParser.SendContext):
        naam = ctx.getText()
        parent = ctx.parentCtx.parentCtx.parentCtx.getText()
        print(f"visit Kind {naam} with parent {parent}")
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