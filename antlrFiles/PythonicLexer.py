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
        4,0,23,225,6,-1,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,
        2,6,7,6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,
        13,7,13,2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,
        19,2,20,7,20,2,21,7,21,2,22,7,22,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,
        1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,1,2,1,2,1,3,1,3,1,3,1,3,
        1,3,1,4,1,4,1,4,1,4,1,4,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,
        1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,7,1,7,1,7,1,7,1,7,1,7,1,7,
        1,7,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,9,1,9,1,9,1,9,1,9,1,10,1,10,1,
        10,1,10,1,10,1,10,1,11,1,11,1,11,1,12,1,12,1,13,1,13,1,14,1,14,1,
        14,1,14,1,14,1,14,1,14,1,14,1,14,3,14,139,8,14,1,15,1,15,1,15,3,
        15,144,8,15,1,16,3,16,147,8,16,1,16,1,16,5,16,151,8,16,10,16,12,
        16,154,9,16,1,16,3,16,157,8,16,1,17,1,17,1,17,1,17,5,17,163,8,17,
        10,17,12,17,166,9,17,1,17,1,17,1,18,3,18,171,8,18,1,18,4,18,174,
        8,18,11,18,12,18,175,1,18,1,18,4,18,180,8,18,11,18,12,18,181,1,18,
        3,18,185,8,18,1,18,1,18,1,18,4,18,190,8,18,11,18,12,18,191,3,18,
        194,8,18,1,19,1,19,1,19,1,19,1,19,1,19,1,19,1,19,1,19,3,19,205,8,
        19,1,20,4,20,208,8,20,11,20,12,20,209,1,21,1,21,1,21,1,21,1,22,3,
        22,217,8,22,1,22,1,22,5,22,221,8,22,10,22,12,22,224,9,22,1,164,0,
        23,1,1,3,2,5,3,7,4,9,5,11,6,13,7,15,8,17,9,19,10,21,11,23,12,25,
        13,27,14,29,15,31,16,33,17,35,18,37,19,39,20,41,21,43,22,45,23,1,
        0,6,1,0,45,45,1,0,49,57,1,0,48,57,1,0,48,48,2,0,60,60,62,62,4,0,
        48,57,65,90,95,95,97,122,245,0,1,1,0,0,0,0,3,1,0,0,0,0,5,1,0,0,0,
        0,7,1,0,0,0,0,9,1,0,0,0,0,11,1,0,0,0,0,13,1,0,0,0,0,15,1,0,0,0,0,
        17,1,0,0,0,0,19,1,0,0,0,0,21,1,0,0,0,0,23,1,0,0,0,0,25,1,0,0,0,0,
        27,1,0,0,0,0,29,1,0,0,0,0,31,1,0,0,0,0,33,1,0,0,0,0,35,1,0,0,0,0,
        37,1,0,0,0,0,39,1,0,0,0,0,41,1,0,0,0,0,43,1,0,0,0,0,45,1,0,0,0,1,
        47,1,0,0,0,3,57,1,0,0,0,5,64,1,0,0,0,7,67,1,0,0,0,9,72,1,0,0,0,11,
        77,1,0,0,0,13,87,1,0,0,0,15,96,1,0,0,0,17,104,1,0,0,0,19,111,1,0,
        0,0,21,116,1,0,0,0,23,122,1,0,0,0,25,125,1,0,0,0,27,127,1,0,0,0,
        29,138,1,0,0,0,31,143,1,0,0,0,33,156,1,0,0,0,35,158,1,0,0,0,37,193,
        1,0,0,0,39,204,1,0,0,0,41,207,1,0,0,0,43,211,1,0,0,0,45,216,1,0,
        0,0,47,48,5,112,0,0,48,49,5,114,0,0,49,50,5,111,0,0,50,51,5,116,
        0,0,51,52,5,111,0,0,52,53,5,99,0,0,53,54,5,111,0,0,54,55,5,108,0,
        0,55,56,5,58,0,0,56,2,1,0,0,0,57,58,5,114,0,0,58,59,5,111,0,0,59,
        60,5,108,0,0,60,61,5,101,0,0,61,62,5,115,0,0,62,63,5,58,0,0,63,4,
        1,0,0,0,64,65,5,116,0,0,65,66,5,111,0,0,66,6,1,0,0,0,67,68,5,102,
        0,0,68,69,5,114,0,0,69,70,5,111,0,0,70,71,5,109,0,0,71,8,1,0,0,0,
        72,73,5,115,0,0,73,74,5,101,0,0,74,75,5,110,0,0,75,76,5,100,0,0,
        76,10,1,0,0,0,77,78,5,115,0,0,78,79,5,101,0,0,79,80,5,113,0,0,80,
        81,5,117,0,0,81,82,5,101,0,0,82,83,5,110,0,0,83,84,5,99,0,0,84,85,
        5,101,0,0,85,86,5,58,0,0,86,12,1,0,0,0,87,88,5,115,0,0,88,89,5,104,
        0,0,89,90,5,117,0,0,90,91,5,102,0,0,91,92,5,102,0,0,92,93,5,108,
        0,0,93,94,5,101,0,0,94,95,5,58,0,0,95,14,1,0,0,0,96,97,5,99,0,0,
        97,98,5,104,0,0,98,99,5,111,0,0,99,100,5,105,0,0,100,101,5,99,0,
        0,101,102,5,101,0,0,102,103,5,58,0,0,103,16,1,0,0,0,104,105,5,114,
        0,0,105,106,5,101,0,0,106,107,5,112,0,0,107,108,5,101,0,0,108,109,
        5,97,0,0,109,110,5,116,0,0,110,18,1,0,0,0,111,112,5,108,0,0,112,
        113,5,111,0,0,113,114,5,111,0,0,114,115,5,112,0,0,115,20,1,0,0,0,
        116,117,5,99,0,0,117,118,5,108,0,0,118,119,5,111,0,0,119,120,5,115,
        0,0,120,121,5,101,0,0,121,22,1,0,0,0,122,123,3,41,20,0,123,124,5,
        58,0,0,124,24,1,0,0,0,125,126,5,40,0,0,126,26,1,0,0,0,127,128,5,
        41,0,0,128,28,1,0,0,0,129,130,5,84,0,0,130,131,5,114,0,0,131,132,
        5,117,0,0,132,139,5,101,0,0,133,134,5,70,0,0,134,135,5,97,0,0,135,
        136,5,108,0,0,136,137,5,115,0,0,137,139,5,101,0,0,138,129,1,0,0,
        0,138,133,1,0,0,0,139,30,1,0,0,0,140,144,3,35,17,0,141,144,3,33,
        16,0,142,144,3,37,18,0,143,140,1,0,0,0,143,141,1,0,0,0,143,142,1,
        0,0,0,144,32,1,0,0,0,145,147,7,0,0,0,146,145,1,0,0,0,146,147,1,0,
        0,0,147,148,1,0,0,0,148,152,7,1,0,0,149,151,7,2,0,0,150,149,1,0,
        0,0,151,154,1,0,0,0,152,150,1,0,0,0,152,153,1,0,0,0,153,157,1,0,
        0,0,154,152,1,0,0,0,155,157,7,3,0,0,156,146,1,0,0,0,156,155,1,0,
        0,0,157,34,1,0,0,0,158,164,5,34,0,0,159,160,5,92,0,0,160,163,5,34,
        0,0,161,163,9,0,0,0,162,159,1,0,0,0,162,161,1,0,0,0,163,166,1,0,
        0,0,164,165,1,0,0,0,164,162,1,0,0,0,165,167,1,0,0,0,166,164,1,0,
        0,0,167,168,5,34,0,0,168,36,1,0,0,0,169,171,7,0,0,0,170,169,1,0,
        0,0,170,171,1,0,0,0,171,173,1,0,0,0,172,174,7,1,0,0,173,172,1,0,
        0,0,174,175,1,0,0,0,175,173,1,0,0,0,175,176,1,0,0,0,176,177,1,0,
        0,0,177,179,5,46,0,0,178,180,7,2,0,0,179,178,1,0,0,0,180,181,1,0,
        0,0,181,179,1,0,0,0,181,182,1,0,0,0,182,194,1,0,0,0,183,185,7,0,
        0,0,184,183,1,0,0,0,184,185,1,0,0,0,185,186,1,0,0,0,186,187,7,3,
        0,0,187,189,5,46,0,0,188,190,7,2,0,0,189,188,1,0,0,0,190,191,1,0,
        0,0,191,189,1,0,0,0,191,192,1,0,0,0,192,194,1,0,0,0,193,170,1,0,
        0,0,193,184,1,0,0,0,194,38,1,0,0,0,195,205,7,4,0,0,196,197,5,60,
        0,0,197,205,5,61,0,0,198,199,5,62,0,0,199,205,5,61,0,0,200,201,5,
        33,0,0,201,205,5,61,0,0,202,203,5,61,0,0,203,205,5,61,0,0,204,195,
        1,0,0,0,204,196,1,0,0,0,204,198,1,0,0,0,204,200,1,0,0,0,204,202,
        1,0,0,0,205,40,1,0,0,0,206,208,7,5,0,0,207,206,1,0,0,0,208,209,1,
        0,0,0,209,207,1,0,0,0,209,210,1,0,0,0,210,42,1,0,0,0,211,212,5,32,
        0,0,212,213,1,0,0,0,213,214,6,21,0,0,214,44,1,0,0,0,215,217,5,13,
        0,0,216,215,1,0,0,0,216,217,1,0,0,0,217,218,1,0,0,0,218,222,5,10,
        0,0,219,221,5,32,0,0,220,219,1,0,0,0,221,224,1,0,0,0,222,220,1,0,
        0,0,222,223,1,0,0,0,223,46,1,0,0,0,224,222,1,0,0,0,19,0,138,143,
        146,152,156,162,164,170,175,181,184,191,193,204,207,209,216,222,
        1,6,0,0
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
    LOOPLABEL = 12
    OPENINGBRACKET = 13
    CLOSINGBRACKET = 14
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
            "'shuffle:'", "'choice:'", "'repeat'", "'loop'", "'close'", 
            "'('", "')'" ]

    symbolicNames = [ "<INVALID>",
            "PROTOCOL", "ROLES", "TO", "FROM", "SEND", "SEQUENCE", "SHUFFLE", 
            "CHOICE", "REPEAT", "LOOP", "CLOSE", "LOOPLABEL", "OPENINGBRACKET", 
            "CLOSINGBRACKET", "BOOLEAN", "PRIMITIVE", "INTEGER", "STRING", 
            "FLOAT", "COMPARATOR", "WORD", "WS", "NL" ]

    ruleNames = [ "PROTOCOL", "ROLES", "TO", "FROM", "SEND", "SEQUENCE", 
                  "SHUFFLE", "CHOICE", "REPEAT", "LOOP", "CLOSE", "LOOPLABEL", 
                  "OPENINGBRACKET", "CLOSINGBRACKET", "BOOLEAN", "PRIMITIVE", 
                  "INTEGER", "STRING", "FLOAT", "COMPARATOR", "WORD", "WS", 
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



