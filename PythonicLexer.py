# Generated from ./Pythonic.g4 by ANTLR 4.13.1
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


from antlr_denter.DenterHelper import DenterHelper
from PythonicParser import PythonicParser


def serializedATN():
    return [
        4,0,13,112,6,-1,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,
        2,6,7,6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,1,
        0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,
        1,1,2,1,2,1,2,1,3,1,3,1,3,1,4,1,4,1,4,1,4,1,4,1,5,1,5,1,5,1,5,1,
        5,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,7,1,7,1,7,1,7,1,7,1,
        7,1,7,1,7,1,7,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,9,1,9,1,9,1,9,1,
        9,1,9,1,10,4,10,95,8,10,11,10,12,10,96,1,11,1,11,1,11,1,11,1,12,
        3,12,104,8,12,1,12,1,12,5,12,108,8,12,10,12,12,12,111,9,12,0,0,13,
        1,1,3,2,5,3,7,4,9,5,11,6,13,7,15,8,17,9,19,10,21,11,23,12,25,13,
        1,0,1,4,0,48,57,65,90,95,95,97,122,114,0,1,1,0,0,0,0,3,1,0,0,0,0,
        5,1,0,0,0,0,7,1,0,0,0,0,9,1,0,0,0,0,11,1,0,0,0,0,13,1,0,0,0,0,15,
        1,0,0,0,0,17,1,0,0,0,0,19,1,0,0,0,0,21,1,0,0,0,0,23,1,0,0,0,0,25,
        1,0,0,0,1,27,1,0,0,0,3,37,1,0,0,0,5,44,1,0,0,0,7,47,1,0,0,0,9,50,
        1,0,0,0,11,55,1,0,0,0,13,60,1,0,0,0,15,70,1,0,0,0,17,79,1,0,0,0,
        19,87,1,0,0,0,21,94,1,0,0,0,23,98,1,0,0,0,25,103,1,0,0,0,27,28,5,
        112,0,0,28,29,5,114,0,0,29,30,5,111,0,0,30,31,5,116,0,0,31,32,5,
        111,0,0,32,33,5,99,0,0,33,34,5,111,0,0,34,35,5,108,0,0,35,36,5,40,
        0,0,36,2,1,0,0,0,37,38,5,114,0,0,38,39,5,111,0,0,39,40,5,108,0,0,
        40,41,5,101,0,0,41,42,5,115,0,0,42,43,5,58,0,0,43,4,1,0,0,0,44,45,
        5,41,0,0,45,46,5,58,0,0,46,6,1,0,0,0,47,48,5,116,0,0,48,49,5,111,
        0,0,49,8,1,0,0,0,50,51,5,102,0,0,51,52,5,114,0,0,52,53,5,111,0,0,
        53,54,5,109,0,0,54,10,1,0,0,0,55,56,5,115,0,0,56,57,5,101,0,0,57,
        58,5,110,0,0,58,59,5,100,0,0,59,12,1,0,0,0,60,61,5,115,0,0,61,62,
        5,101,0,0,62,63,5,113,0,0,63,64,5,117,0,0,64,65,5,101,0,0,65,66,
        5,110,0,0,66,67,5,99,0,0,67,68,5,101,0,0,68,69,5,58,0,0,69,14,1,
        0,0,0,70,71,5,115,0,0,71,72,5,104,0,0,72,73,5,117,0,0,73,74,5,102,
        0,0,74,75,5,102,0,0,75,76,5,108,0,0,76,77,5,101,0,0,77,78,5,58,0,
        0,78,16,1,0,0,0,79,80,5,99,0,0,80,81,5,104,0,0,81,82,5,111,0,0,82,
        83,5,105,0,0,83,84,5,99,0,0,84,85,5,101,0,0,85,86,5,58,0,0,86,18,
        1,0,0,0,87,88,5,99,0,0,88,89,5,108,0,0,89,90,5,111,0,0,90,91,5,115,
        0,0,91,92,5,101,0,0,92,20,1,0,0,0,93,95,7,0,0,0,94,93,1,0,0,0,95,
        96,1,0,0,0,96,94,1,0,0,0,96,97,1,0,0,0,97,22,1,0,0,0,98,99,5,32,
        0,0,99,100,1,0,0,0,100,101,6,11,0,0,101,24,1,0,0,0,102,104,5,13,
        0,0,103,102,1,0,0,0,103,104,1,0,0,0,104,105,1,0,0,0,105,109,5,10,
        0,0,106,108,5,32,0,0,107,106,1,0,0,0,108,111,1,0,0,0,109,107,1,0,
        0,0,109,110,1,0,0,0,110,26,1,0,0,0,111,109,1,0,0,0,5,0,94,96,103,
        109,1,6,0,0
    ]

class PythonicLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    PROTOCOL = 1
    ROLES = 2
    CLOSEBRKT = 3
    TO = 4
    FROM = 5
    SEND = 6
    SEQUENCE = 7
    SHUFFLE = 8
    CHOICE = 9
    CLOSE = 10
    WORD = 11
    WS = 12
    NL = 13

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'protocol('", "'roles:'", "'):'", "'to'", "'from'", "'send'", 
            "'sequence:'", "'shuffle:'", "'choice:'", "'close'" ]

    symbolicNames = [ "<INVALID>",
            "PROTOCOL", "ROLES", "CLOSEBRKT", "TO", "FROM", "SEND", "SEQUENCE", 
            "SHUFFLE", "CHOICE", "CLOSE", "WORD", "WS", "NL" ]

    ruleNames = [ "PROTOCOL", "ROLES", "CLOSEBRKT", "TO", "FROM", "SEND", 
                  "SEQUENCE", "SHUFFLE", "CHOICE", "CLOSE", "WORD", "WS", 
                  "NL" ]

    grammarFileName = "Pythonic.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    class MyCoolDenter(DenterHelper):
        def __init__(self, lexer, nl_token, indent_token, dedent_token, ignore_eof):
            super().__init__(nl_token, indent_token, dedent_token, ignore_eof)
            self.lexer: PythonicLexer = lexer

        def pull_token(self):
            return super(PythonicLexer, self.lexer).nextToken()

    denter = None

    def nextToken(self):
        if not self.denter:
            self.denter = self.MyCoolDenter(self, self.NL, PythonicParser.INDENT, PythonicParser.DEDENT, False)
        return self.denter.next_token()



