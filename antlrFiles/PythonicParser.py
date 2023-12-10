# Generated from ./Pythonic.g4 by ANTLR 4.13.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,25,109,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        1,0,1,0,1,0,1,0,1,1,1,1,1,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,3,2,43,8,
        2,1,3,1,3,1,3,1,4,1,4,1,4,1,5,1,5,1,5,1,6,1,6,1,6,1,6,1,7,1,7,1,
        7,1,7,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,3,8,72,8,8,1,8,1,8,
        1,8,1,8,1,8,1,8,1,9,1,9,1,9,1,9,1,9,1,9,1,10,1,10,4,10,88,8,10,11,
        10,12,10,89,1,10,1,10,1,11,1,11,1,11,1,12,1,12,1,12,4,12,100,8,12,
        11,12,12,12,101,1,12,1,12,1,13,1,13,1,13,1,13,0,0,14,0,2,4,6,8,10,
        12,14,16,18,20,22,24,26,0,1,1,0,15,16,104,0,28,1,0,0,0,2,32,1,0,
        0,0,4,42,1,0,0,0,6,44,1,0,0,0,8,47,1,0,0,0,10,50,1,0,0,0,12,53,1,
        0,0,0,14,57,1,0,0,0,16,61,1,0,0,0,18,79,1,0,0,0,20,85,1,0,0,0,22,
        93,1,0,0,0,24,96,1,0,0,0,26,105,1,0,0,0,28,29,3,22,11,0,29,30,3,
        2,1,0,30,31,5,0,0,1,31,1,1,0,0,0,32,33,5,1,0,0,33,34,3,20,10,0,34,
        3,1,0,0,0,35,43,3,16,8,0,36,43,3,6,3,0,37,43,3,8,4,0,38,43,3,10,
        5,0,39,43,3,18,9,0,40,43,3,12,6,0,41,43,3,14,7,0,42,35,1,0,0,0,42,
        36,1,0,0,0,42,37,1,0,0,0,42,38,1,0,0,0,42,39,1,0,0,0,42,40,1,0,0,
        0,42,41,1,0,0,0,43,5,1,0,0,0,44,45,5,6,0,0,45,46,3,20,10,0,46,7,
        1,0,0,0,47,48,5,7,0,0,48,49,3,20,10,0,49,9,1,0,0,0,50,51,5,8,0,0,
        51,52,3,20,10,0,52,11,1,0,0,0,53,54,5,10,0,0,54,55,5,12,0,0,55,56,
        3,20,10,0,56,13,1,0,0,0,57,58,5,9,0,0,58,59,5,21,0,0,59,60,5,23,
        0,0,60,15,1,0,0,0,61,62,5,5,0,0,62,71,5,21,0,0,63,64,5,13,0,0,64,
        65,5,20,0,0,65,66,5,16,0,0,66,72,5,14,0,0,67,68,5,13,0,0,68,69,7,
        0,0,0,69,72,5,14,0,0,70,72,1,0,0,0,71,63,1,0,0,0,71,67,1,0,0,0,71,
        70,1,0,0,0,72,73,1,0,0,0,73,74,5,4,0,0,74,75,5,21,0,0,75,76,5,3,
        0,0,76,77,5,21,0,0,77,78,5,23,0,0,78,17,1,0,0,0,79,80,5,11,0,0,80,
        81,5,21,0,0,81,82,5,3,0,0,82,83,5,21,0,0,83,84,5,23,0,0,84,19,1,
        0,0,0,85,87,5,24,0,0,86,88,3,4,2,0,87,86,1,0,0,0,88,89,1,0,0,0,89,
        87,1,0,0,0,89,90,1,0,0,0,90,91,1,0,0,0,91,92,5,25,0,0,92,21,1,0,
        0,0,93,94,5,2,0,0,94,95,3,24,12,0,95,23,1,0,0,0,96,97,5,24,0,0,97,
        99,3,26,13,0,98,100,3,26,13,0,99,98,1,0,0,0,100,101,1,0,0,0,101,
        99,1,0,0,0,101,102,1,0,0,0,102,103,1,0,0,0,103,104,5,25,0,0,104,
        25,1,0,0,0,105,106,5,21,0,0,106,107,5,23,0,0,107,27,1,0,0,0,4,42,
        71,89,101
    ]

class PythonicParser ( Parser ):

    grammarFileName = "Pythonic.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'protocol:'", "'roles:'", "'to'", "'from'", 
                     "'send'", "'sequence:'", "'shuffle:'", "'choice:'", 
                     "'repeat'", "'loop'", "'close'", "<INVALID>", "'('", 
                     "')'" ]

    symbolicNames = [ "<INVALID>", "PROTOCOL", "ROLES", "TO", "FROM", "SEND", 
                      "SEQUENCE", "SHUFFLE", "CHOICE", "REPEAT", "LOOP", 
                      "CLOSE", "LOOPLABEL", "OPENINGBRACKET", "CLOSINGBRACKET", 
                      "BOOLEAN", "PRIMITIVE", "INTEGER", "STRING", "FLOAT", 
                      "COMPARATOR", "WORD", "WS", "NL", "INDENT", "DEDENT" ]

    RULE_specification = 0
    RULE_protocol = 1
    RULE_expression = 2
    RULE_sequence = 3
    RULE_shuffle = 4
    RULE_choice = 5
    RULE_loop = 6
    RULE_repeat = 7
    RULE_send = 8
    RULE_close = 9
    RULE_block = 10
    RULE_roles = 11
    RULE_roleblock = 12
    RULE_role = 13

    ruleNames =  [ "specification", "protocol", "expression", "sequence", 
                   "shuffle", "choice", "loop", "repeat", "send", "close", 
                   "block", "roles", "roleblock", "role" ]

    EOF = Token.EOF
    PROTOCOL=1
    ROLES=2
    TO=3
    FROM=4
    SEND=5
    SEQUENCE=6
    SHUFFLE=7
    CHOICE=8
    REPEAT=9
    LOOP=10
    CLOSE=11
    LOOPLABEL=12
    OPENINGBRACKET=13
    CLOSINGBRACKET=14
    BOOLEAN=15
    PRIMITIVE=16
    INTEGER=17
    STRING=18
    FLOAT=19
    COMPARATOR=20
    WORD=21
    WS=22
    NL=23
    INDENT=24
    DEDENT=25

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class SpecificationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def roles(self):
            return self.getTypedRuleContext(PythonicParser.RolesContext,0)


        def protocol(self):
            return self.getTypedRuleContext(PythonicParser.ProtocolContext,0)


        def EOF(self):
            return self.getToken(PythonicParser.EOF, 0)

        def getRuleIndex(self):
            return PythonicParser.RULE_specification

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSpecification" ):
                listener.enterSpecification(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSpecification" ):
                listener.exitSpecification(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSpecification" ):
                return visitor.visitSpecification(self)
            else:
                return visitor.visitChildren(self)




    def specification(self):

        localctx = PythonicParser.SpecificationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_specification)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 28
            self.roles()
            self.state = 29
            self.protocol()
            self.state = 30
            self.match(PythonicParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ProtocolContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PROTOCOL(self):
            return self.getToken(PythonicParser.PROTOCOL, 0)

        def block(self):
            return self.getTypedRuleContext(PythonicParser.BlockContext,0)


        def getRuleIndex(self):
            return PythonicParser.RULE_protocol

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProtocol" ):
                listener.enterProtocol(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProtocol" ):
                listener.exitProtocol(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProtocol" ):
                return visitor.visitProtocol(self)
            else:
                return visitor.visitChildren(self)




    def protocol(self):

        localctx = PythonicParser.ProtocolContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_protocol)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 32
            self.match(PythonicParser.PROTOCOL)
            self.state = 33
            self.block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def send(self):
            return self.getTypedRuleContext(PythonicParser.SendContext,0)


        def sequence(self):
            return self.getTypedRuleContext(PythonicParser.SequenceContext,0)


        def shuffle(self):
            return self.getTypedRuleContext(PythonicParser.ShuffleContext,0)


        def choice(self):
            return self.getTypedRuleContext(PythonicParser.ChoiceContext,0)


        def close(self):
            return self.getTypedRuleContext(PythonicParser.CloseContext,0)


        def loop(self):
            return self.getTypedRuleContext(PythonicParser.LoopContext,0)


        def repeat(self):
            return self.getTypedRuleContext(PythonicParser.RepeatContext,0)


        def getRuleIndex(self):
            return PythonicParser.RULE_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpression" ):
                listener.enterExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpression" ):
                listener.exitExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression" ):
                return visitor.visitExpression(self)
            else:
                return visitor.visitChildren(self)




    def expression(self):

        localctx = PythonicParser.ExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 42
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [5]:
                self.state = 35
                self.send()
                pass
            elif token in [6]:
                self.state = 36
                self.sequence()
                pass
            elif token in [7]:
                self.state = 37
                self.shuffle()
                pass
            elif token in [8]:
                self.state = 38
                self.choice()
                pass
            elif token in [11]:
                self.state = 39
                self.close()
                pass
            elif token in [10]:
                self.state = 40
                self.loop()
                pass
            elif token in [9]:
                self.state = 41
                self.repeat()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SequenceContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SEQUENCE(self):
            return self.getToken(PythonicParser.SEQUENCE, 0)

        def block(self):
            return self.getTypedRuleContext(PythonicParser.BlockContext,0)


        def getRuleIndex(self):
            return PythonicParser.RULE_sequence

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSequence" ):
                listener.enterSequence(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSequence" ):
                listener.exitSequence(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSequence" ):
                return visitor.visitSequence(self)
            else:
                return visitor.visitChildren(self)




    def sequence(self):

        localctx = PythonicParser.SequenceContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_sequence)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 44
            self.match(PythonicParser.SEQUENCE)
            self.state = 45
            self.block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ShuffleContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SHUFFLE(self):
            return self.getToken(PythonicParser.SHUFFLE, 0)

        def block(self):
            return self.getTypedRuleContext(PythonicParser.BlockContext,0)


        def getRuleIndex(self):
            return PythonicParser.RULE_shuffle

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterShuffle" ):
                listener.enterShuffle(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitShuffle" ):
                listener.exitShuffle(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitShuffle" ):
                return visitor.visitShuffle(self)
            else:
                return visitor.visitChildren(self)




    def shuffle(self):

        localctx = PythonicParser.ShuffleContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_shuffle)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 47
            self.match(PythonicParser.SHUFFLE)
            self.state = 48
            self.block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ChoiceContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CHOICE(self):
            return self.getToken(PythonicParser.CHOICE, 0)

        def block(self):
            return self.getTypedRuleContext(PythonicParser.BlockContext,0)


        def getRuleIndex(self):
            return PythonicParser.RULE_choice

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterChoice" ):
                listener.enterChoice(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitChoice" ):
                listener.exitChoice(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitChoice" ):
                return visitor.visitChoice(self)
            else:
                return visitor.visitChildren(self)




    def choice(self):

        localctx = PythonicParser.ChoiceContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_choice)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 50
            self.match(PythonicParser.CHOICE)
            self.state = 51
            self.block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LoopContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LOOP(self):
            return self.getToken(PythonicParser.LOOP, 0)

        def LOOPLABEL(self):
            return self.getToken(PythonicParser.LOOPLABEL, 0)

        def block(self):
            return self.getTypedRuleContext(PythonicParser.BlockContext,0)


        def getRuleIndex(self):
            return PythonicParser.RULE_loop

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLoop" ):
                listener.enterLoop(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLoop" ):
                listener.exitLoop(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLoop" ):
                return visitor.visitLoop(self)
            else:
                return visitor.visitChildren(self)




    def loop(self):

        localctx = PythonicParser.LoopContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_loop)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 53
            self.match(PythonicParser.LOOP)
            self.state = 54
            self.match(PythonicParser.LOOPLABEL)
            self.state = 55
            self.block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RepeatContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def REPEAT(self):
            return self.getToken(PythonicParser.REPEAT, 0)

        def WORD(self):
            return self.getToken(PythonicParser.WORD, 0)

        def NL(self):
            return self.getToken(PythonicParser.NL, 0)

        def getRuleIndex(self):
            return PythonicParser.RULE_repeat

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRepeat" ):
                listener.enterRepeat(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRepeat" ):
                listener.exitRepeat(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRepeat" ):
                return visitor.visitRepeat(self)
            else:
                return visitor.visitChildren(self)




    def repeat(self):

        localctx = PythonicParser.RepeatContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_repeat)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 57
            self.match(PythonicParser.REPEAT)
            self.state = 58
            self.match(PythonicParser.WORD)
            self.state = 59
            self.match(PythonicParser.NL)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SendContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SEND(self):
            return self.getToken(PythonicParser.SEND, 0)

        def WORD(self, i:int=None):
            if i is None:
                return self.getTokens(PythonicParser.WORD)
            else:
                return self.getToken(PythonicParser.WORD, i)

        def FROM(self):
            return self.getToken(PythonicParser.FROM, 0)

        def TO(self):
            return self.getToken(PythonicParser.TO, 0)

        def NL(self):
            return self.getToken(PythonicParser.NL, 0)

        def OPENINGBRACKET(self):
            return self.getToken(PythonicParser.OPENINGBRACKET, 0)

        def COMPARATOR(self):
            return self.getToken(PythonicParser.COMPARATOR, 0)

        def PRIMITIVE(self):
            return self.getToken(PythonicParser.PRIMITIVE, 0)

        def CLOSINGBRACKET(self):
            return self.getToken(PythonicParser.CLOSINGBRACKET, 0)

        def BOOLEAN(self):
            return self.getToken(PythonicParser.BOOLEAN, 0)

        def getRuleIndex(self):
            return PythonicParser.RULE_send

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSend" ):
                listener.enterSend(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSend" ):
                listener.exitSend(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSend" ):
                return visitor.visitSend(self)
            else:
                return visitor.visitChildren(self)




    def send(self):

        localctx = PythonicParser.SendContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_send)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 61
            self.match(PythonicParser.SEND)
            self.state = 62
            self.match(PythonicParser.WORD)
            self.state = 71
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.state = 63
                self.match(PythonicParser.OPENINGBRACKET)
                self.state = 64
                self.match(PythonicParser.COMPARATOR)
                self.state = 65
                self.match(PythonicParser.PRIMITIVE)
                self.state = 66
                self.match(PythonicParser.CLOSINGBRACKET)
                pass

            elif la_ == 2:
                self.state = 67
                self.match(PythonicParser.OPENINGBRACKET)
                self.state = 68
                _la = self._input.LA(1)
                if not(_la==15 or _la==16):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 69
                self.match(PythonicParser.CLOSINGBRACKET)
                pass

            elif la_ == 3:
                pass


            self.state = 73
            self.match(PythonicParser.FROM)
            self.state = 74
            self.match(PythonicParser.WORD)
            self.state = 75
            self.match(PythonicParser.TO)
            self.state = 76
            self.match(PythonicParser.WORD)
            self.state = 77
            self.match(PythonicParser.NL)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CloseContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CLOSE(self):
            return self.getToken(PythonicParser.CLOSE, 0)

        def WORD(self, i:int=None):
            if i is None:
                return self.getTokens(PythonicParser.WORD)
            else:
                return self.getToken(PythonicParser.WORD, i)

        def TO(self):
            return self.getToken(PythonicParser.TO, 0)

        def NL(self):
            return self.getToken(PythonicParser.NL, 0)

        def getRuleIndex(self):
            return PythonicParser.RULE_close

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterClose" ):
                listener.enterClose(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitClose" ):
                listener.exitClose(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitClose" ):
                return visitor.visitClose(self)
            else:
                return visitor.visitChildren(self)




    def close(self):

        localctx = PythonicParser.CloseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_close)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 79
            self.match(PythonicParser.CLOSE)
            self.state = 80
            self.match(PythonicParser.WORD)
            self.state = 81
            self.match(PythonicParser.TO)
            self.state = 82
            self.match(PythonicParser.WORD)
            self.state = 83
            self.match(PythonicParser.NL)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BlockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INDENT(self):
            return self.getToken(PythonicParser.INDENT, 0)

        def DEDENT(self):
            return self.getToken(PythonicParser.DEDENT, 0)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PythonicParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(PythonicParser.ExpressionContext,i)


        def getRuleIndex(self):
            return PythonicParser.RULE_block

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBlock" ):
                listener.enterBlock(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBlock" ):
                listener.exitBlock(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlock" ):
                return visitor.visitBlock(self)
            else:
                return visitor.visitChildren(self)




    def block(self):

        localctx = PythonicParser.BlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_block)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 85
            self.match(PythonicParser.INDENT)
            self.state = 87 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 86
                self.expression()
                self.state = 89 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 4064) != 0)):
                    break

            self.state = 91
            self.match(PythonicParser.DEDENT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RolesContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ROLES(self):
            return self.getToken(PythonicParser.ROLES, 0)

        def roleblock(self):
            return self.getTypedRuleContext(PythonicParser.RoleblockContext,0)


        def getRuleIndex(self):
            return PythonicParser.RULE_roles

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRoles" ):
                listener.enterRoles(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRoles" ):
                listener.exitRoles(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRoles" ):
                return visitor.visitRoles(self)
            else:
                return visitor.visitChildren(self)




    def roles(self):

        localctx = PythonicParser.RolesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_roles)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 93
            self.match(PythonicParser.ROLES)
            self.state = 94
            self.roleblock()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RoleblockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INDENT(self):
            return self.getToken(PythonicParser.INDENT, 0)

        def role(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PythonicParser.RoleContext)
            else:
                return self.getTypedRuleContext(PythonicParser.RoleContext,i)


        def DEDENT(self):
            return self.getToken(PythonicParser.DEDENT, 0)

        def getRuleIndex(self):
            return PythonicParser.RULE_roleblock

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRoleblock" ):
                listener.enterRoleblock(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRoleblock" ):
                listener.exitRoleblock(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRoleblock" ):
                return visitor.visitRoleblock(self)
            else:
                return visitor.visitChildren(self)




    def roleblock(self):

        localctx = PythonicParser.RoleblockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_roleblock)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 96
            self.match(PythonicParser.INDENT)
            self.state = 97
            self.role()
            self.state = 99 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 98
                self.role()
                self.state = 101 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==21):
                    break

            self.state = 103
            self.match(PythonicParser.DEDENT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RoleContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WORD(self):
            return self.getToken(PythonicParser.WORD, 0)

        def NL(self):
            return self.getToken(PythonicParser.NL, 0)

        def getRuleIndex(self):
            return PythonicParser.RULE_role

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRole" ):
                listener.enterRole(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRole" ):
                listener.exitRole(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRole" ):
                return visitor.visitRole(self)
            else:
                return visitor.visitChildren(self)




    def role(self):

        localctx = PythonicParser.RoleContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_role)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 105
            self.match(PythonicParser.WORD)
            self.state = 106
            self.match(PythonicParser.NL)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





