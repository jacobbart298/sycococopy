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
        4,1,15,91,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,1,0,1,0,1,0,4,0,28,
        8,0,11,0,12,0,29,1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,2,1,2,1,2,1,2,1,2,
        1,2,4,2,45,8,2,11,2,12,2,46,1,3,1,3,1,3,1,4,1,4,1,4,1,5,1,5,1,5,
        1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,7,1,7,1,7,1,7,1,7,1,7,1,8,1,8,
        4,8,74,8,8,11,8,12,8,75,1,8,1,8,1,9,1,9,1,9,1,10,1,10,1,10,1,11,
        4,11,87,8,11,11,11,12,11,88,1,11,0,0,12,0,2,4,6,8,10,12,14,16,18,
        20,22,0,0,89,0,27,1,0,0,0,2,33,1,0,0,0,4,44,1,0,0,0,6,48,1,0,0,0,
        8,51,1,0,0,0,10,54,1,0,0,0,12,57,1,0,0,0,14,65,1,0,0,0,16,71,1,0,
        0,0,18,79,1,0,0,0,20,82,1,0,0,0,22,86,1,0,0,0,24,28,3,2,1,0,25,28,
        3,20,10,0,26,28,3,22,11,0,27,24,1,0,0,0,27,25,1,0,0,0,27,26,1,0,
        0,0,28,29,1,0,0,0,29,27,1,0,0,0,29,30,1,0,0,0,30,31,1,0,0,0,31,32,
        5,0,0,1,32,1,1,0,0,0,33,34,5,1,0,0,34,35,5,11,0,0,35,36,5,3,0,0,
        36,37,3,16,8,0,37,3,1,0,0,0,38,45,3,12,6,0,39,45,3,6,3,0,40,45,3,
        8,4,0,41,45,3,10,5,0,42,45,3,14,7,0,43,45,3,18,9,0,44,38,1,0,0,0,
        44,39,1,0,0,0,44,40,1,0,0,0,44,41,1,0,0,0,44,42,1,0,0,0,44,43,1,
        0,0,0,45,46,1,0,0,0,46,44,1,0,0,0,46,47,1,0,0,0,47,5,1,0,0,0,48,
        49,5,7,0,0,49,50,3,16,8,0,50,7,1,0,0,0,51,52,5,8,0,0,52,53,3,16,
        8,0,53,9,1,0,0,0,54,55,5,9,0,0,55,56,3,16,8,0,56,11,1,0,0,0,57,58,
        5,6,0,0,58,59,5,11,0,0,59,60,5,5,0,0,60,61,5,11,0,0,61,62,5,4,0,
        0,62,63,5,11,0,0,63,64,5,13,0,0,64,13,1,0,0,0,65,66,5,10,0,0,66,
        67,5,11,0,0,67,68,5,4,0,0,68,69,5,11,0,0,69,70,5,13,0,0,70,15,1,
        0,0,0,71,73,5,14,0,0,72,74,3,4,2,0,73,72,1,0,0,0,74,75,1,0,0,0,75,
        73,1,0,0,0,75,76,1,0,0,0,76,77,1,0,0,0,77,78,5,15,0,0,78,17,1,0,
        0,0,79,80,5,11,0,0,80,81,5,13,0,0,81,19,1,0,0,0,82,83,5,2,0,0,83,
        84,3,16,8,0,84,21,1,0,0,0,85,87,5,13,0,0,86,85,1,0,0,0,87,88,1,0,
        0,0,88,86,1,0,0,0,88,89,1,0,0,0,89,23,1,0,0,0,6,27,29,44,46,75,88
    ]

class PythonicParser ( Parser ):

    grammarFileName = "Pythonic.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'protocol('", "'roles:'", "'):'", "'to'", 
                     "'from'", "'send'", "'sequence:'", "'shuffle:'", "'choice:'", 
                     "'close'" ]

    symbolicNames = [ "<INVALID>", "PROTOCOL", "ROLES", "CLOSEBRKT", "TO", 
                      "FROM", "SEND", "SEQUENCE", "SHUFFLE", "CHOICE", "CLOSE", 
                      "WORD", "WS", "NL", "INDENT", "DEDENT" ]

    RULE_specification = 0
    RULE_protocol = 1
    RULE_expression = 2
    RULE_sequence = 3
    RULE_shuffle = 4
    RULE_choice = 5
    RULE_send = 6
    RULE_close = 7
    RULE_block = 8
    RULE_role = 9
    RULE_roles = 10
    RULE_emptyspace = 11

    ruleNames =  [ "specification", "protocol", "expression", "sequence", 
                   "shuffle", "choice", "send", "close", "block", "role", 
                   "roles", "emptyspace" ]

    EOF = Token.EOF
    PROTOCOL=1
    ROLES=2
    CLOSEBRKT=3
    TO=4
    FROM=5
    SEND=6
    SEQUENCE=7
    SHUFFLE=8
    CHOICE=9
    CLOSE=10
    WORD=11
    WS=12
    NL=13
    INDENT=14
    DEDENT=15

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

        def EOF(self):
            return self.getToken(PythonicParser.EOF, 0)

        def protocol(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PythonicParser.ProtocolContext)
            else:
                return self.getTypedRuleContext(PythonicParser.ProtocolContext,i)


        def roles(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PythonicParser.RolesContext)
            else:
                return self.getTypedRuleContext(PythonicParser.RolesContext,i)


        def emptyspace(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PythonicParser.EmptyspaceContext)
            else:
                return self.getTypedRuleContext(PythonicParser.EmptyspaceContext,i)


        def getRuleIndex(self):
            return PythonicParser.RULE_specification

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSpecification" ):
                listener.enterSpecification(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSpecification" ):
                listener.exitSpecification(self)




    def specification(self):

        localctx = PythonicParser.SpecificationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_specification)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 27 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 27
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [1]:
                    self.state = 24
                    self.protocol()
                    pass
                elif token in [2]:
                    self.state = 25
                    self.roles()
                    pass
                elif token in [13]:
                    self.state = 26
                    self.emptyspace()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 29 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 8198) != 0)):
                    break

            self.state = 31
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

        def WORD(self):
            return self.getToken(PythonicParser.WORD, 0)

        def CLOSEBRKT(self):
            return self.getToken(PythonicParser.CLOSEBRKT, 0)

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




    def protocol(self):

        localctx = PythonicParser.ProtocolContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_protocol)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 33
            self.match(PythonicParser.PROTOCOL)
            self.state = 34
            self.match(PythonicParser.WORD)
            self.state = 35
            self.match(PythonicParser.CLOSEBRKT)
            self.state = 36
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


        def role(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PythonicParser.RoleContext)
            else:
                return self.getTypedRuleContext(PythonicParser.RoleContext,i)


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
        self.enterRule(localctx, 4, self.RULE_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 44 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 44
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [6]:
                        self.state = 38
                        self.send()
                        pass
                    elif token in [7]:
                        self.state = 39
                        self.sequence()
                        pass
                    elif token in [8]:
                        self.state = 40
                        self.shuffle()
                        pass
                    elif token in [9]:
                        self.state = 41
                        self.choice()
                        pass
                    elif token in [10]:
                        self.state = 42
                        self.close()
                        pass
                    elif token in [11]:
                        self.state = 43
                        self.role()
                        pass
                    else:
                        raise NoViableAltException(self)


                else:
                    raise NoViableAltException(self)
                self.state = 46 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,3,self._ctx)

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
        self.enterRule(localctx, 6, self.RULE_sequence)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 48
            self.match(PythonicParser.SEQUENCE)
            self.state = 49
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
        self.enterRule(localctx, 8, self.RULE_shuffle)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 51
            self.match(PythonicParser.SHUFFLE)
            self.state = 52
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
        self.enterRule(localctx, 10, self.RULE_choice)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 54
            self.match(PythonicParser.CHOICE)
            self.state = 55
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
        self.enterRule(localctx, 12, self.RULE_send)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 57
            self.match(PythonicParser.SEND)
            self.state = 58
            self.match(PythonicParser.WORD)
            self.state = 59
            self.match(PythonicParser.FROM)
            self.state = 60
            self.match(PythonicParser.WORD)
            self.state = 61
            self.match(PythonicParser.TO)
            self.state = 62
            self.match(PythonicParser.WORD)
            self.state = 63
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
        self.enterRule(localctx, 14, self.RULE_close)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 65
            self.match(PythonicParser.CLOSE)
            self.state = 66
            self.match(PythonicParser.WORD)
            self.state = 67
            self.match(PythonicParser.TO)
            self.state = 68
            self.match(PythonicParser.WORD)
            self.state = 69
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
        self.enterRule(localctx, 16, self.RULE_block)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 71
            self.match(PythonicParser.INDENT)
            self.state = 73 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 72
                self.expression()
                self.state = 75 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 4032) != 0)):
                    break

            self.state = 77
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




    def role(self):

        localctx = PythonicParser.RoleContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_role)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 79
            self.match(PythonicParser.WORD)
            self.state = 80
            self.match(PythonicParser.NL)
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

        def block(self):
            return self.getTypedRuleContext(PythonicParser.BlockContext,0)


        def getRuleIndex(self):
            return PythonicParser.RULE_roles

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRoles" ):
                listener.enterRoles(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRoles" ):
                listener.exitRoles(self)




    def roles(self):

        localctx = PythonicParser.RolesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_roles)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 82
            self.match(PythonicParser.ROLES)
            self.state = 83
            self.block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class EmptyspaceContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NL(self, i:int=None):
            if i is None:
                return self.getTokens(PythonicParser.NL)
            else:
                return self.getToken(PythonicParser.NL, i)

        def getRuleIndex(self):
            return PythonicParser.RULE_emptyspace

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEmptyspace" ):
                listener.enterEmptyspace(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEmptyspace" ):
                listener.exitEmptyspace(self)




    def emptyspace(self):

        localctx = PythonicParser.EmptyspaceContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_emptyspace)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 86 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 85
                    self.match(PythonicParser.NL)

                else:
                    raise NoViableAltException(self)
                self.state = 88 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,5,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





