# Generated from ./Pythonic.g4 by ANTLR 4.13.1
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
        4,0,23,221,6,-1,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,
        2,6,7,6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,
        13,7,13,2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,
        19,2,20,7,20,2,21,7,21,2,22,7,22,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,
        1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,1,2,1,2,1,3,1,3,1,3,1,3,
        1,3,1,4,1,4,1,4,1,4,1,4,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,
        1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,7,1,7,1,7,1,7,1,7,1,7,1,7,
        1,7,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,9,1,9,1,9,1,9,1,9,1,10,1,10,1,
        10,1,11,1,11,1,12,1,12,1,13,1,13,1,14,1,14,1,14,1,14,1,14,1,14,1,
        14,1,14,1,14,3,14,135,8,14,1,15,1,15,1,15,3,15,140,8,15,1,16,3,16,
        143,8,16,1,16,1,16,5,16,147,8,16,10,16,12,16,150,9,16,1,16,3,16,
        153,8,16,1,17,1,17,1,17,1,17,5,17,159,8,17,10,17,12,17,162,9,17,
        1,17,1,17,1,18,3,18,167,8,18,1,18,4,18,170,8,18,11,18,12,18,171,
        1,18,1,18,4,18,176,8,18,11,18,12,18,177,1,18,3,18,181,8,18,1,18,
        1,18,1,18,4,18,186,8,18,11,18,12,18,187,3,18,190,8,18,1,19,1,19,
        1,19,1,19,1,19,1,19,1,19,1,19,1,19,3,19,201,8,19,1,20,4,20,204,8,
        20,11,20,12,20,205,1,21,1,21,1,21,1,21,1,22,3,22,213,8,22,1,22,1,
        22,5,22,217,8,22,10,22,12,22,220,9,22,1,160,0,23,1,1,3,2,5,3,7,4,
        9,5,11,6,13,7,15,8,17,9,19,10,21,11,23,12,25,13,27,14,29,15,31,16,
        33,17,35,18,37,19,39,20,41,21,43,22,45,23,1,0,6,1,0,45,45,1,0,49,
        57,1,0,48,57,1,0,48,48,2,0,60,60,62,62,4,0,48,57,65,90,95,95,97,
        122,241,0,1,1,0,0,0,0,3,1,0,0,0,0,5,1,0,0,0,0,7,1,0,0,0,0,9,1,0,
        0,0,0,11,1,0,0,0,0,13,1,0,0,0,0,15,1,0,0,0,0,17,1,0,0,0,0,19,1,0,
        0,0,0,21,1,0,0,0,0,23,1,0,0,0,0,25,1,0,0,0,0,27,1,0,0,0,0,29,1,0,
        0,0,0,31,1,0,0,0,0,33,1,0,0,0,0,35,1,0,0,0,0,37,1,0,0,0,0,39,1,0,
        0,0,0,41,1,0,0,0,0,43,1,0,0,0,0,45,1,0,0,0,1,47,1,0,0,0,3,57,1,0,
        0,0,5,64,1,0,0,0,7,67,1,0,0,0,9,72,1,0,0,0,11,77,1,0,0,0,13,87,1,
        0,0,0,15,96,1,0,0,0,17,104,1,0,0,0,19,111,1,0,0,0,21,116,1,0,0,0,
        23,119,1,0,0,0,25,121,1,0,0,0,27,123,1,0,0,0,29,134,1,0,0,0,31,139,
        1,0,0,0,33,152,1,0,0,0,35,154,1,0,0,0,37,189,1,0,0,0,39,200,1,0,
        0,0,41,203,1,0,0,0,43,207,1,0,0,0,45,212,1,0,0,0,47,48,5,112,0,0,
        48,49,5,114,0,0,49,50,5,111,0,0,50,51,5,116,0,0,51,52,5,111,0,0,
        52,53,5,99,0,0,53,54,5,111,0,0,54,55,5,108,0,0,55,56,5,58,0,0,56,
        2,1,0,0,0,57,58,5,114,0,0,58,59,5,111,0,0,59,60,5,108,0,0,60,61,
        5,101,0,0,61,62,5,115,0,0,62,63,5,58,0,0,63,4,1,0,0,0,64,65,5,116,
        0,0,65,66,5,111,0,0,66,6,1,0,0,0,67,68,5,102,0,0,68,69,5,114,0,0,
        69,70,5,111,0,0,70,71,5,109,0,0,71,8,1,0,0,0,72,73,5,115,0,0,73,
        74,5,101,0,0,74,75,5,110,0,0,75,76,5,100,0,0,76,10,1,0,0,0,77,78,
        5,115,0,0,78,79,5,101,0,0,79,80,5,113,0,0,80,81,5,117,0,0,81,82,
        5,101,0,0,82,83,5,110,0,0,83,84,5,99,0,0,84,85,5,101,0,0,85,86,5,
        58,0,0,86,12,1,0,0,0,87,88,5,115,0,0,88,89,5,104,0,0,89,90,5,117,
        0,0,90,91,5,102,0,0,91,92,5,102,0,0,92,93,5,108,0,0,93,94,5,101,
        0,0,94,95,5,58,0,0,95,14,1,0,0,0,96,97,5,99,0,0,97,98,5,104,0,0,
        98,99,5,111,0,0,99,100,5,105,0,0,100,101,5,99,0,0,101,102,5,101,
        0,0,102,103,5,58,0,0,103,16,1,0,0,0,104,105,5,114,0,0,105,106,5,
        101,0,0,106,107,5,112,0,0,107,108,5,101,0,0,108,109,5,97,0,0,109,
        110,5,116,0,0,110,18,1,0,0,0,111,112,5,108,0,0,112,113,5,111,0,0,
        113,114,5,111,0,0,114,115,5,112,0,0,115,20,1,0,0,0,116,117,3,41,
        20,0,117,118,5,58,0,0,118,22,1,0,0,0,119,120,5,40,0,0,120,24,1,0,
        0,0,121,122,5,41,0,0,122,26,1,0,0,0,123,124,5,44,0,0,124,28,1,0,
        0,0,125,126,5,84,0,0,126,127,5,114,0,0,127,128,5,117,0,0,128,135,
        5,101,0,0,129,130,5,70,0,0,130,131,5,97,0,0,131,132,5,108,0,0,132,
        133,5,115,0,0,133,135,5,101,0,0,134,125,1,0,0,0,134,129,1,0,0,0,
        135,30,1,0,0,0,136,140,3,35,17,0,137,140,3,33,16,0,138,140,3,37,
        18,0,139,136,1,0,0,0,139,137,1,0,0,0,139,138,1,0,0,0,140,32,1,0,
        0,0,141,143,7,0,0,0,142,141,1,0,0,0,142,143,1,0,0,0,143,144,1,0,
        0,0,144,148,7,1,0,0,145,147,7,2,0,0,146,145,1,0,0,0,147,150,1,0,
        0,0,148,146,1,0,0,0,148,149,1,0,0,0,149,153,1,0,0,0,150,148,1,0,
        0,0,151,153,7,3,0,0,152,142,1,0,0,0,152,151,1,0,0,0,153,34,1,0,0,
        0,154,160,5,34,0,0,155,156,5,92,0,0,156,159,5,34,0,0,157,159,9,0,
        0,0,158,155,1,0,0,0,158,157,1,0,0,0,159,162,1,0,0,0,160,161,1,0,
        0,0,160,158,1,0,0,0,161,163,1,0,0,0,162,160,1,0,0,0,163,164,5,34,
        0,0,164,36,1,0,0,0,165,167,7,0,0,0,166,165,1,0,0,0,166,167,1,0,0,
        0,167,169,1,0,0,0,168,170,7,1,0,0,169,168,1,0,0,0,170,171,1,0,0,
        0,171,169,1,0,0,0,171,172,1,0,0,0,172,173,1,0,0,0,173,175,5,46,0,
        0,174,176,7,2,0,0,175,174,1,0,0,0,176,177,1,0,0,0,177,175,1,0,0,
        0,177,178,1,0,0,0,178,190,1,0,0,0,179,181,7,0,0,0,180,179,1,0,0,
        0,180,181,1,0,0,0,181,182,1,0,0,0,182,183,7,3,0,0,183,185,5,46,0,
        0,184,186,7,2,0,0,185,184,1,0,0,0,186,187,1,0,0,0,187,185,1,0,0,
        0,187,188,1,0,0,0,188,190,1,0,0,0,189,166,1,0,0,0,189,180,1,0,0,
        0,190,38,1,0,0,0,191,201,7,4,0,0,192,193,5,60,0,0,193,201,5,61,0,
        0,194,195,5,62,0,0,195,201,5,61,0,0,196,197,5,33,0,0,197,201,5,61,
        0,0,198,199,5,61,0,0,199,201,5,61,0,0,200,191,1,0,0,0,200,192,1,
        0,0,0,200,194,1,0,0,0,200,196,1,0,0,0,200,198,1,0,0,0,201,40,1,0,
        0,0,202,204,7,5,0,0,203,202,1,0,0,0,204,205,1,0,0,0,205,203,1,0,
        0,0,205,206,1,0,0,0,206,42,1,0,0,0,207,208,5,32,0,0,208,209,1,0,
        0,0,209,210,6,21,0,0,210,44,1,0,0,0,211,213,5,13,0,0,212,211,1,0,
        0,0,212,213,1,0,0,0,213,214,1,0,0,0,214,218,5,10,0,0,215,217,5,9,
        0,0,216,215,1,0,0,0,217,220,1,0,0,0,218,216,1,0,0,0,218,219,1,0,
        0,0,219,46,1,0,0,0,220,218,1,0,0,0,19,0,134,139,142,148,152,158,
        160,166,171,177,180,187,189,200,203,205,212,218,1,6,0,0
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
    LOOPLABEL = 11
    OPENINGBRACKET = 12
    CLOSINGBRACKET = 13
    COMMA = 14
    BOOLEAN = 15
    PRIMITIVE = 16
    INTEGER = 17
    STRING = 18
    FLOAT = 19
    COMPARATOR = 20
    WORD = 21
    WS = 22
    NL = 23

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'protocol:'", "'roles:'", "'to'", "'from'", "'send'", "'sequence:'", 
            "'shuffle:'", "'choice:'", "'repeat'", "'loop'", "'('", "')'", 
            "','" ]

    symbolicNames = [ "<INVALID>",
            "PROTOCOL", "ROLES", "TO", "FROM", "SEND", "SEQUENCE", "SHUFFLE", 
            "CHOICE", "REPEAT", "LOOP", "LOOPLABEL", "OPENINGBRACKET", "CLOSINGBRACKET", 
            "COMMA", "BOOLEAN", "PRIMITIVE", "INTEGER", "STRING", "FLOAT", 
            "COMPARATOR", "WORD", "WS", "NL" ]

    ruleNames = [ "PROTOCOL", "ROLES", "TO", "FROM", "SEND", "SEQUENCE", 
                  "SHUFFLE", "CHOICE", "REPEAT", "LOOP", "LOOPLABEL", "OPENINGBRACKET", 
                  "CLOSINGBRACKET", "COMMA", "BOOLEAN", "PRIMITIVE", "INTEGER", 
                  "STRING", "FLOAT", "COMPARATOR", "WORD", "WS", "NL" ]

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



