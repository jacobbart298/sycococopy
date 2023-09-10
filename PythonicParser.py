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
        4,1,14,63,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,1,0,1,0,1,0,1,0,1,0,1,0,1,1,1,1,1,1,1,1,1,1,4,1,28,8,1,
        11,1,12,1,29,1,2,1,2,1,2,1,3,1,3,1,3,1,4,1,4,1,4,1,5,1,5,1,5,1,5,
        1,5,1,5,1,5,1,5,1,6,1,6,1,6,1,6,1,6,1,6,1,7,1,7,4,7,57,8,7,11,7,
        12,7,58,1,7,1,7,1,7,0,0,8,0,2,4,6,8,10,12,14,0,0,60,0,16,1,0,0,0,
        2,27,1,0,0,0,4,31,1,0,0,0,6,34,1,0,0,0,8,37,1,0,0,0,10,40,1,0,0,
        0,12,48,1,0,0,0,14,54,1,0,0,0,16,17,5,1,0,0,17,18,5,10,0,0,18,19,
        5,2,0,0,19,20,3,14,7,0,20,21,5,0,0,1,21,1,1,0,0,0,22,28,3,10,5,0,
        23,28,3,4,2,0,24,28,3,6,3,0,25,28,3,8,4,0,26,28,3,12,6,0,27,22,1,
        0,0,0,27,23,1,0,0,0,27,24,1,0,0,0,27,25,1,0,0,0,27,26,1,0,0,0,28,
        29,1,0,0,0,29,27,1,0,0,0,29,30,1,0,0,0,30,3,1,0,0,0,31,32,5,6,0,
        0,32,33,3,14,7,0,33,5,1,0,0,0,34,35,5,7,0,0,35,36,3,14,7,0,36,7,
        1,0,0,0,37,38,5,8,0,0,38,39,3,14,7,0,39,9,1,0,0,0,40,41,5,5,0,0,
        41,42,5,10,0,0,42,43,5,4,0,0,43,44,5,10,0,0,44,45,5,3,0,0,45,46,
        5,10,0,0,46,47,5,12,0,0,47,11,1,0,0,0,48,49,5,9,0,0,49,50,5,10,0,
        0,50,51,5,3,0,0,51,52,5,10,0,0,52,53,5,12,0,0,53,13,1,0,0,0,54,56,
        5,13,0,0,55,57,3,2,1,0,56,55,1,0,0,0,57,58,1,0,0,0,58,56,1,0,0,0,
        58,59,1,0,0,0,59,60,1,0,0,0,60,61,5,14,0,0,61,15,1,0,0,0,3,27,29,
        58
    ]

class PythonicParser ( Parser ):

    grammarFileName = "Pythonic.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'protocol('", "'):'", "'to'", "'from'", 
                     "'send'", "'sequence:'", "'shuffle:'", "'choice:'", 
                     "'close'" ]

    symbolicNames = [ "<INVALID>", "PROTOCOL", "SLUIT", "TO", "FROM", "SEND", 
                      "SEQUENCE", "SHUFFLE", "CHOICE", "CLOSE", "WORD", 
                      "WS", "NL", "INDENT", "DEDENT" ]

    RULE_protocol = 0
    RULE_expression = 1
    RULE_sequence = 2
    RULE_shuffle = 3
    RULE_choice = 4
    RULE_send = 5
    RULE_close = 6
    RULE_block = 7

    ruleNames =  [ "protocol", "expression", "sequence", "shuffle", "choice", 
                   "send", "close", "block" ]

    EOF = Token.EOF
    PROTOCOL=1
    SLUIT=2
    TO=3
    FROM=4
    SEND=5
    SEQUENCE=6
    SHUFFLE=7
    CHOICE=8
    CLOSE=9
    WORD=10
    WS=11
    NL=12
    INDENT=13
    DEDENT=14

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProtocolContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PROTOCOL(self):
            return self.getToken(PythonicParser.PROTOCOL, 0)

        def WORD(self):
            return self.getToken(PythonicParser.WORD, 0)

        def SLUIT(self):
            return self.getToken(PythonicParser.SLUIT, 0)

        def block(self):
            return self.getTypedRuleContext(PythonicParser.BlockContext,0)


        def EOF(self):
            return self.getToken(PythonicParser.EOF, 0)

        def getRuleIndex(self):
            return PythonicParser.RULE_protocol

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProtocol" ):
                listener.enterProtocol(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProtocol" ):
                listener.exitProtocol(self)




    def protocol(self):

        localctx = PythonicParser.ProtocolContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_protocol)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 16
            self.match(PythonicParser.PROTOCOL)
            self.state = 17
            self.match(PythonicParser.WORD)
            self.state = 18
            self.match(PythonicParser.SLUIT)
            self.state = 19
            self.block()
            self.state = 20
            self.match(PythonicParser.EOF)
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

        def send(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PythonicParser.SendContext)
            else:
                return self.getTypedRuleContext(PythonicParser.SendContext,i)


        def sequence(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PythonicParser.SequenceContext)
            else:
                return self.getTypedRuleContext(PythonicParser.SequenceContext,i)


        def shuffle(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PythonicParser.ShuffleContext)
            else:
                return self.getTypedRuleContext(PythonicParser.ShuffleContext,i)


        def choice(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PythonicParser.ChoiceContext)
            else:
                return self.getTypedRuleContext(PythonicParser.ChoiceContext,i)


        def close(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PythonicParser.CloseContext)
            else:
                return self.getTypedRuleContext(PythonicParser.CloseContext,i)


        def getRuleIndex(self):
            return PythonicParser.RULE_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpression" ):
                listener.enterExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpression" ):
                listener.exitExpression(self)




    def expression(self):

        localctx = PythonicParser.ExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 27 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 27
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [5]:
                        self.state = 22
                        self.send()
                        pass
                    elif token in [6]:
                        self.state = 23
                        self.sequence()
                        pass
                    elif token in [7]:
                        self.state = 24
                        self.shuffle()
                        pass
                    elif token in [8]:
                        self.state = 25
                        self.choice()
                        pass
                    elif token in [9]:
                        self.state = 26
                        self.close()
                        pass
                    else:
                        raise NoViableAltException(self)


                else:
                    raise NoViableAltException(self)
                self.state = 29 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,1,self._ctx)

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




    def sequence(self):

        localctx = PythonicParser.SequenceContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_sequence)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 31
            self.match(PythonicParser.SEQUENCE)
            self.state = 32
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




    def shuffle(self):

        localctx = PythonicParser.ShuffleContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_shuffle)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 34
            self.match(PythonicParser.SHUFFLE)
            self.state = 35
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




    def choice(self):

        localctx = PythonicParser.ChoiceContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_choice)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 37
            self.match(PythonicParser.CHOICE)
            self.state = 38
            self.block()
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

        def getRuleIndex(self):
            return PythonicParser.RULE_send

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSend" ):
                listener.enterSend(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSend" ):
                listener.exitSend(self)




    def send(self):

        localctx = PythonicParser.SendContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_send)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 40
            self.match(PythonicParser.SEND)
            self.state = 41
            self.match(PythonicParser.WORD)
            self.state = 42
            self.match(PythonicParser.FROM)
            self.state = 43
            self.match(PythonicParser.WORD)
            self.state = 44
            self.match(PythonicParser.TO)
            self.state = 45
            self.match(PythonicParser.WORD)
            self.state = 46
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




    def close(self):

        localctx = PythonicParser.CloseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_close)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 48
            self.match(PythonicParser.CLOSE)
            self.state = 49
            self.match(PythonicParser.WORD)
            self.state = 50
            self.match(PythonicParser.TO)
            self.state = 51
            self.match(PythonicParser.WORD)
            self.state = 52
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




    def block(self):

        localctx = PythonicParser.BlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_block)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 54
            self.match(PythonicParser.INDENT)
            self.state = 56 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 55
                self.expression()
                self.state = 58 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 992) != 0)):
                    break

            self.state = 60
            self.match(PythonicParser.DEDENT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





