# Generated from Pythonic.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .PythonicParser import PythonicParser
else:
    from PythonicParser import PythonicParser

# This class defines a complete generic visitor for a parse tree produced by PythonicParser.

class PythonicVisitor(ParseTreeVisitor):

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
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonicParser#shuffle.
    def visitShuffle(self, ctx:PythonicParser.ShuffleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonicParser#choice.
    def visitChoice(self, ctx:PythonicParser.ChoiceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonicParser#send.
    def visitSend(self, ctx:PythonicParser.SendContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonicParser#close.
    def visitClose(self, ctx:PythonicParser.CloseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonicParser#block.
    def visitBlock(self, ctx:PythonicParser.BlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonicParser#roles.
    def visitRoles(self, ctx:PythonicParser.RolesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonicParser#roleblock.
    def visitRoleblock(self, ctx:PythonicParser.RoleblockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonicParser#role.
    def visitRole(self, ctx:PythonicParser.RoleContext):
        return self.visitChildren(ctx)



del PythonicParser