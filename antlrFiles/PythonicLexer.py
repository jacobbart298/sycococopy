# Generated from ./antlrFiles/Pythonic.g4 by ANTLR 4.13.1
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


from antlr_denter.DenterHelper import DenterHelper
from antlrFiles.PythonicParser import PythonicParser


def serializedATN():
    return [
        4,0,14,123,6,-1,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,
        2,6,7,6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,
        13,7,13,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,1,1,1,1,1,1,1,
        1,1,1,1,1,1,1,2,1,2,1,2,1,3,1,3,1,3,1,3,1,3,1,4,1,4,1,4,1,4,1,4,
        1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,6,1,6,1,6,1,6,1,6,1,6,
        1,6,1,6,1,6,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,8,1,8,1,8,1,8,1,8,
        1,8,1,8,1,9,1,9,1,9,1,9,1,9,1,10,1,10,1,10,1,10,1,10,1,10,1,11,4,
        11,106,8,11,11,11,12,11,107,1,12,1,12,1,12,1,12,1,13,3,13,115,8,
        13,1,13,1,13,5,13,119,8,13,10,13,12,13,122,9,13,0,0,14,1,1,3,2,5,
        3,7,4,9,5,11,6,13,7,15,8,17,9,19,10,21,11,23,12,25,13,27,14,1,0,
        1,4,0,48,57,65,90,95,95,97,122,125,0,1,1,0,0,0,0,3,1,0,0,0,0,5,1,
        0,0,0,0,7,1,0,0,0,0,9,1,0,0,0,0,11,1,0,0,0,0,13,1,0,0,0,0,15,1,0,
        0,0,0,17,1,0,0,0,0,19,1,0,0,0,0,21,1,0,0,0,0,23,1,0,0,0,0,25,1,0,
        0,0,0,27,1,0,0,0,1,29,1,0,0,0,3,39,1,0,0,0,5,46,1,0,0,0,7,49,1,0,
        0,0,9,54,1,0,0,0,11,59,1,0,0,0,13,69,1,0,0,0,15,78,1,0,0,0,17,86,
        1,0,0,0,19,93,1,0,0,0,21,98,1,0,0,0,23,105,1,0,0,0,25,109,1,0,0,
        0,27,114,1,0,0,0,29,30,5,112,0,0,30,31,5,114,0,0,31,32,5,111,0,0,
        32,33,5,116,0,0,33,34,5,111,0,0,34,35,5,99,0,0,35,36,5,111,0,0,36,
        37,5,108,0,0,37,38,5,58,0,0,38,2,1,0,0,0,39,40,5,114,0,0,40,41,5,
        111,0,0,41,42,5,108,0,0,42,43,5,101,0,0,43,44,5,115,0,0,44,45,5,
        58,0,0,45,4,1,0,0,0,46,47,5,116,0,0,47,48,5,111,0,0,48,6,1,0,0,0,
        49,50,5,102,0,0,50,51,5,114,0,0,51,52,5,111,0,0,52,53,5,109,0,0,
        53,8,1,0,0,0,54,55,5,115,0,0,55,56,5,101,0,0,56,57,5,110,0,0,57,
        58,5,100,0,0,58,10,1,0,0,0,59,60,5,115,0,0,60,61,5,101,0,0,61,62,
        5,113,0,0,62,63,5,117,0,0,63,64,5,101,0,0,64,65,5,110,0,0,65,66,
        5,99,0,0,66,67,5,101,0,0,67,68,5,58,0,0,68,12,1,0,0,0,69,70,5,115,
        0,0,70,71,5,104,0,0,71,72,5,117,0,0,72,73,5,102,0,0,73,74,5,102,
        0,0,74,75,5,108,0,0,75,76,5,101,0,0,76,77,5,58,0,0,77,14,1,0,0,0,
        78,79,5,99,0,0,79,80,5,104,0,0,80,81,5,111,0,0,81,82,5,105,0,0,82,
        83,5,99,0,0,83,84,5,101,0,0,84,85,5,58,0,0,85,16,1,0,0,0,86,87,5,
        114,0,0,87,88,5,101,0,0,88,89,5,112,0,0,89,90,5,101,0,0,90,91,5,
        97,0,0,91,92,5,116,0,0,92,18,1,0,0,0,93,94,5,108,0,0,94,95,5,111,
        0,0,95,96,5,111,0,0,96,97,5,112,0,0,97,20,1,0,0,0,98,99,5,99,0,0,
        99,100,5,108,0,0,100,101,5,111,0,0,101,102,5,115,0,0,102,103,5,101,
        0,0,103,22,1,0,0,0,104,106,7,0,0,0,105,104,1,0,0,0,106,107,1,0,0,
        0,107,105,1,0,0,0,107,108,1,0,0,0,108,24,1,0,0,0,109,110,5,32,0,
        0,110,111,1,0,0,0,111,112,6,12,0,0,112,26,1,0,0,0,113,115,5,13,0,
        0,114,113,1,0,0,0,114,115,1,0,0,0,115,116,1,0,0,0,116,120,5,10,0,
        0,117,119,5,32,0,0,118,117,1,0,0,0,119,122,1,0,0,0,120,118,1,0,0,
        0,120,121,1,0,0,0,121,28,1,0,0,0,122,120,1,0,0,0,5,0,105,107,114,
        120,1,6,0,0
    ]

class PythonicLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    PROTOCOL = 1
    ROLES = 2
    TO = 3
    FROM = 4
    SEND = 5
    SEQUENCE = 6
    SHUFFLE = 7
    CHOICE = 8
    REPEAT = 9
    LOOP = 10
    CLOSE = 11
    WORD = 12
    WS = 13
    NL = 14

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'protocol:'", "'roles:'", "'to'", "'from'", "'send'", "'sequence:'", 
            "'shuffle:'", "'choice:'", "'repeat'", "'loop'", "'close'" ]

    symbolicNames = [ "<INVALID>",
            "PROTOCOL", "ROLES", "TO", "FROM", "SEND", "SEQUENCE", "SHUFFLE", 
            "CHOICE", "REPEAT", "LOOP", "CLOSE", "WORD", "WS", "NL" ]

    ruleNames = [ "PROTOCOL", "ROLES", "TO", "FROM", "SEND", "SEQUENCE", 
                  "SHUFFLE", "CHOICE", "REPEAT", "LOOP", "CLOSE", "WORD", 
                  "WS", "NL" ]

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



