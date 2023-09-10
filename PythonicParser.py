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
        4,1,15,74,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,1,0,1,0,1,0,1,0,1,0,1,0,1,1,1,1,1,1,1,
        1,1,1,1,1,4,1,33,8,1,11,1,12,1,34,1,2,1,2,1,2,1,3,1,3,1,3,1,4,1,
        4,1,4,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,6,1,6,1,6,1,6,1,6,1,6,1,
        7,1,7,4,7,62,8,7,11,7,12,7,63,1,7,1,7,1,8,1,8,1,9,1,9,1,9,1,9,1,
        9,0,0,10,0,2,4,6,8,10,12,14,16,18,0,0,70,0,20,1,0,0,0,2,32,1,0,0,
        0,4,36,1,0,0,0,6,39,1,0,0,0,8,42,1,0,0,0,10,45,1,0,0,0,12,53,1,0,
        0,0,14,59,1,0,0,0,16,67,1,0,0,0,18,69,1,0,0,0,20,21,5,1,0,0,21,22,
        5,11,0,0,22,23,5,3,0,0,23,24,3,14,7,0,24,25,3,18,9,0,25,1,1,0,0,
        0,26,33,3,10,5,0,27,33,3,4,2,0,28,33,3,6,3,0,29,33,3,8,4,0,30,33,
        3,12,6,0,31,33,3,16,8,0,32,26,1,0,0,0,32,27,1,0,0,0,32,28,1,0,0,
        0,32,29,1,0,0,0,32,30,1,0,0,0,32,31,1,0,0,0,33,34,1,0,0,0,34,32,
        1,0,0,0,34,35,1,0,0,0,35,3,1,0,0,0,36,37,5,7,0,0,37,38,3,14,7,0,
        38,5,1,0,0,0,39,40,5,8,0,0,40,41,3,14,7,0,41,7,1,0,0,0,42,43,5,9,
        0,0,43,44,3,14,7,0,44,9,1,0,0,0,45,46,5,6,0,0,46,47,5,11,0,0,47,
        48,5,5,0,0,48,49,5,11,0,0,49,50,5,4,0,0,50,51,5,11,0,0,51,52,5,13,
        0,0,52,11,1,0,0,0,53,54,5,10,0,0,54,55,5,11,0,0,55,56,5,4,0,0,56,
        57,5,11,0,0,57,58,5,13,0,0,58,13,1,0,0,0,59,61,5,14,0,0,60,62,3,
        2,1,0,61,60,1,0,0,0,62,63,1,0,0,0,63,61,1,0,0,0,63,64,1,0,0,0,64,
        65,1,0,0,0,65,66,5,15,0,0,66,15,1,0,0,0,67,68,5,11,0,0,68,17,1,0,
        0,0,69,70,5,2,0,0,70,71,3,14,7,0,71,72,5,0,0,1,72,19,1,0,0,0,3,32,
        34,63
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

    RULE_protocol = 0
    RULE_expression = 1
    RULE_sequence = 2
    RULE_shuffle = 3
    RULE_choice = 4
    RULE_send = 5
    RULE_close = 6
    RULE_block = 7
    RULE_role = 8
    RULE_roles = 9

    ruleNames =  [ "protocol", "expression", "sequence", "shuffle", "choice", 
                   "send", "close", "block", "role", "roles" ]

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


        def roles(self):
            return self.getTypedRuleContext(PythonicParser.RolesContext,0)


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
            self.state = 20
            self.match(PythonicParser.PROTOCOL)
            self.state = 21
            self.match(PythonicParser.WORD)
            self.state = 22
            self.match(PythonicParser.CLOSEBRKT)
            self.state = 23
            self.block()
            self.state = 24
            self.roles()
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
        self.enterRule(localctx, 2, self.RULE_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 32 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 32
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [6]:
                        self.state = 26
                        self.send()
                        pass
                    elif token in [7]:
                        self.state = 27
                        self.sequence()
                        pass
                    elif token in [8]:
                        self.state = 28
                        self.shuffle()
                        pass
                    elif token in [9]:
                        self.state = 29
                        self.choice()
                        pass
                    elif token in [10]:
                        self.state = 30
                        self.close()
                        pass
                    elif token in [11]:
                        self.state = 31
                        self.role()
                        pass
                    else:
                        raise NoViableAltException(self)


                else:
                    raise NoViableAltException(self)
                self.state = 34 
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
            self.state = 36
            self.match(PythonicParser.SEQUENCE)
            self.state = 37
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
            self.state = 39
            self.match(PythonicParser.SHUFFLE)
            self.state = 40
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
            self.state = 42
            self.match(PythonicParser.CHOICE)
            self.state = 43
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
            self.state = 45
            self.match(PythonicParser.SEND)
            self.state = 46
            self.match(PythonicParser.WORD)
            self.state = 47
            self.match(PythonicParser.FROM)
            self.state = 48
            self.match(PythonicParser.WORD)
            self.state = 49
            self.match(PythonicParser.TO)
            self.state = 50
            self.match(PythonicParser.WORD)
            self.state = 51
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
            self.state = 53
            self.match(PythonicParser.CLOSE)
            self.state = 54
            self.match(PythonicParser.WORD)
            self.state = 55
            self.match(PythonicParser.TO)
            self.state = 56
            self.match(PythonicParser.WORD)
            self.state = 57
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
            self.state = 59
            self.match(PythonicParser.INDENT)
            self.state = 61 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 60
                self.expression()
                self.state = 63 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 4032) != 0)):
                    break

            self.state = 65
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
        self.enterRule(localctx, 16, self.RULE_role)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 67
            self.match(PythonicParser.WORD)
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


        def EOF(self):
            return self.getToken(PythonicParser.EOF, 0)

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
        self.enterRule(localctx, 18, self.RULE_roles)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 69
            self.match(PythonicParser.ROLES)
            self.state = 70
            self.block()
            self.state = 71
            self.match(PythonicParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





