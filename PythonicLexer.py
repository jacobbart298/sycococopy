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
        4,0,12,103,6,-1,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,
        2,6,7,6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,1,0,1,0,1,0,
        1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,1,1,1,1,1,1,2,1,2,1,2,1,3,1,3,1,3,
        1,3,1,3,1,4,1,4,1,4,1,4,1,4,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,
        1,5,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,7,1,7,1,7,1,7,1,7,1,7,
        1,7,1,7,1,8,1,8,1,8,1,8,1,8,1,8,1,9,4,9,86,8,9,11,9,12,9,87,1,10,
        1,10,1,10,1,10,1,11,3,11,95,8,11,1,11,1,11,5,11,99,8,11,10,11,12,
        11,102,9,11,0,0,12,1,1,3,2,5,3,7,4,9,5,11,6,13,7,15,8,17,9,19,10,
        21,11,23,12,1,0,1,4,0,48,57,65,90,95,95,97,122,105,0,1,1,0,0,0,0,
        3,1,0,0,0,0,5,1,0,0,0,0,7,1,0,0,0,0,9,1,0,0,0,0,11,1,0,0,0,0,13,
        1,0,0,0,0,15,1,0,0,0,0,17,1,0,0,0,0,19,1,0,0,0,0,21,1,0,0,0,0,23,
        1,0,0,0,1,25,1,0,0,0,3,35,1,0,0,0,5,38,1,0,0,0,7,41,1,0,0,0,9,46,
        1,0,0,0,11,51,1,0,0,0,13,61,1,0,0,0,15,70,1,0,0,0,17,78,1,0,0,0,
        19,85,1,0,0,0,21,89,1,0,0,0,23,94,1,0,0,0,25,26,5,112,0,0,26,27,
        5,114,0,0,27,28,5,111,0,0,28,29,5,116,0,0,29,30,5,111,0,0,30,31,
        5,99,0,0,31,32,5,111,0,0,32,33,5,108,0,0,33,34,5,40,0,0,34,2,1,0,
        0,0,35,36,5,41,0,0,36,37,5,58,0,0,37,4,1,0,0,0,38,39,5,116,0,0,39,
        40,5,111,0,0,40,6,1,0,0,0,41,42,5,102,0,0,42,43,5,114,0,0,43,44,
        5,111,0,0,44,45,5,109,0,0,45,8,1,0,0,0,46,47,5,115,0,0,47,48,5,101,
        0,0,48,49,5,110,0,0,49,50,5,100,0,0,50,10,1,0,0,0,51,52,5,115,0,
        0,52,53,5,101,0,0,53,54,5,113,0,0,54,55,5,117,0,0,55,56,5,101,0,
        0,56,57,5,110,0,0,57,58,5,99,0,0,58,59,5,101,0,0,59,60,5,58,0,0,
        60,12,1,0,0,0,61,62,5,115,0,0,62,63,5,104,0,0,63,64,5,117,0,0,64,
        65,5,102,0,0,65,66,5,102,0,0,66,67,5,108,0,0,67,68,5,101,0,0,68,
        69,5,58,0,0,69,14,1,0,0,0,70,71,5,99,0,0,71,72,5,104,0,0,72,73,5,
        111,0,0,73,74,5,105,0,0,74,75,5,99,0,0,75,76,5,101,0,0,76,77,5,58,
        0,0,77,16,1,0,0,0,78,79,5,99,0,0,79,80,5,108,0,0,80,81,5,111,0,0,
        81,82,5,115,0,0,82,83,5,101,0,0,83,18,1,0,0,0,84,86,7,0,0,0,85,84,
        1,0,0,0,86,87,1,0,0,0,87,85,1,0,0,0,87,88,1,0,0,0,88,20,1,0,0,0,
        89,90,5,32,0,0,90,91,1,0,0,0,91,92,6,10,0,0,92,22,1,0,0,0,93,95,
        5,13,0,0,94,93,1,0,0,0,94,95,1,0,0,0,95,96,1,0,0,0,96,100,5,10,0,
        0,97,99,5,32,0,0,98,97,1,0,0,0,99,102,1,0,0,0,100,98,1,0,0,0,100,
        101,1,0,0,0,101,24,1,0,0,0,102,100,1,0,0,0,5,0,85,87,94,100,1,6,
        0,0
    ]

class PythonicLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    PROTOCOL = 1
    SLUIT = 2
    TO = 3
    FROM = 4
    SEND = 5
    SEQUENCE = 6
    SHUFFLE = 7
    CHOICE = 8
    CLOSE = 9
    WORD = 10
    WS = 11
    NL = 12

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'protocol('", "'):'", "'to'", "'from'", "'send'", "'sequence:'", 
            "'shuffle:'", "'choice:'", "'close'" ]

    symbolicNames = [ "<INVALID>",
            "PROTOCOL", "SLUIT", "TO", "FROM", "SEND", "SEQUENCE", "SHUFFLE", 
            "CHOICE", "CLOSE", "WORD", "WS", "NL" ]

    ruleNames = [ "PROTOCOL", "SLUIT", "TO", "FROM", "SEND", "SEQUENCE", 
                  "SHUFFLE", "CHOICE", "CLOSE", "WORD", "WS", "NL" ]

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



