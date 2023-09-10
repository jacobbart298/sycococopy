# Generated from ./Pythonic.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .PythonicParser import PythonicParser
else:
    from PythonicParser import PythonicParser

# This class defines a complete listener for a parse tree produced by PythonicParser.
class PythonicListener(ParseTreeListener):

    # Enter a parse tree produced by PythonicParser#specification.
    def enterSpecification(self, ctx:PythonicParser.SpecificationContext):
        pass

    # Exit a parse tree produced by PythonicParser#specification.
    def exitSpecification(self, ctx:PythonicParser.SpecificationContext):
        pass


    # Enter a parse tree produced by PythonicParser#protocol.
    def enterProtocol(self, ctx:PythonicParser.ProtocolContext):
        pass

    # Exit a parse tree produced by PythonicParser#protocol.
    def exitProtocol(self, ctx:PythonicParser.ProtocolContext):
        pass


    # Enter a parse tree produced by PythonicParser#expression.
    def enterExpression(self, ctx:PythonicParser.ExpressionContext):
        pass

    # Exit a parse tree produced by PythonicParser#expression.
    def exitExpression(self, ctx:PythonicParser.ExpressionContext):
        pass


    # Enter a parse tree produced by PythonicParser#sequence.
    def enterSequence(self, ctx:PythonicParser.SequenceContext):
        pass

    # Exit a parse tree produced by PythonicParser#sequence.
    def exitSequence(self, ctx:PythonicParser.SequenceContext):
        pass


    # Enter a parse tree produced by PythonicParser#shuffle.
    def enterShuffle(self, ctx:PythonicParser.ShuffleContext):
        pass

    # Exit a parse tree produced by PythonicParser#shuffle.
    def exitShuffle(self, ctx:PythonicParser.ShuffleContext):
        pass


    # Enter a parse tree produced by PythonicParser#choice.
    def enterChoice(self, ctx:PythonicParser.ChoiceContext):
        pass

    # Exit a parse tree produced by PythonicParser#choice.
    def exitChoice(self, ctx:PythonicParser.ChoiceContext):
        pass


    # Enter a parse tree produced by PythonicParser#send.
    def enterSend(self, ctx:PythonicParser.SendContext):
        pass

    # Exit a parse tree produced by PythonicParser#send.
    def exitSend(self, ctx:PythonicParser.SendContext):
        pass


    # Enter a parse tree produced by PythonicParser#close.
    def enterClose(self, ctx:PythonicParser.CloseContext):
        pass

    # Exit a parse tree produced by PythonicParser#close.
    def exitClose(self, ctx:PythonicParser.CloseContext):
        pass


    # Enter a parse tree produced by PythonicParser#block.
    def enterBlock(self, ctx:PythonicParser.BlockContext):
        pass

    # Exit a parse tree produced by PythonicParser#block.
    def exitBlock(self, ctx:PythonicParser.BlockContext):
        pass


    # Enter a parse tree produced by PythonicParser#role.
    def enterRole(self, ctx:PythonicParser.RoleContext):
        pass

    # Exit a parse tree produced by PythonicParser#role.
    def exitRole(self, ctx:PythonicParser.RoleContext):
        pass


    # Enter a parse tree produced by PythonicParser#roles.
    def enterRoles(self, ctx:PythonicParser.RolesContext):
        pass

    # Exit a parse tree produced by PythonicParser#roles.
    def exitRoles(self, ctx:PythonicParser.RolesContext):
        pass



del PythonicParser