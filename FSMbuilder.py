# Generated from ./Pythonic.g4 by ANTLR 4.13.1
from antlr4 import *
from antlr4.tree.Trees import Trees
from antlr4.tree.Tree import TerminalNodeImpl
from PythonicVisitor import PythonicVisitor
if "." in __name__:
    from .PythonicParser import PythonicParser
else:
    from PythonicParser import PythonicParser

# This class defines a complete generic visitor for a parse tree produced by PythonicParser.

class FSMbuilder(PythonicVisitor):

    def __init__(self):
        

    # Visit a parse tree produced by PythonicParser#specification.
    def visitSpecification(self, ctx:PythonicParser.SpecificationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonicParser#protocol.
    def visitProtocol(self, ctx:PythonicParser.ProtocolContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonicParser#expression.
    def visitExpression(self, ctx:PythonicParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonicParser#sequence.
    def visitSequence(self, ctx:PythonicParser.SequenceContext):
        print("Visit sequence")
        block = ctx.getChild(1)
        childNotes = block.getChildCount()
        print(f"The sequence has {childNotes} children")
        for i in range(childNotes):
            print(f"Number {i} node = " + block.getChild(i).getText())
        self.dump(block.getChild(1))
        # kind2 =block.getChild(1)
        # self.visit(kind2)
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