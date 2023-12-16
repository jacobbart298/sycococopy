# Generated from Pythonic.g4 by ANTLR 4.13.1
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
        4,0,25,252,6,-1,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,
        2,6,7,6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,
        13,7,13,2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,
        19,2,20,7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,1,0,1,0,1,0,
        1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,1,2,
        1,2,1,3,1,3,1,3,1,3,1,3,1,4,1,4,1,4,1,4,1,4,1,5,1,5,1,5,1,5,1,5,
        1,5,1,5,1,5,1,5,1,5,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,7,1,7,
        1,7,1,7,1,7,1,7,1,7,1,7,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,9,1,9,1,9,
        1,9,1,9,1,10,1,10,1,10,1,10,1,10,1,10,1,11,1,11,1,11,1,12,1,12,1,
        13,1,13,1,14,1,14,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,3,
        15,145,8,15,1,16,1,16,1,16,3,16,150,8,16,1,17,3,17,153,8,17,1,17,
        1,17,5,17,157,8,17,10,17,12,17,160,9,17,1,17,3,17,163,8,17,1,18,
        1,18,1,18,1,18,5,18,169,8,18,10,18,12,18,172,9,18,1,18,1,18,1,19,
        3,19,177,8,19,1,19,4,19,180,8,19,11,19,12,19,181,1,19,1,19,4,19,
        186,8,19,11,19,12,19,187,1,19,3,19,191,8,19,1,19,1,19,1,19,4,19,
        196,8,19,11,19,12,19,197,3,19,200,8,19,1,20,1,20,1,20,1,20,1,20,
        1,20,1,20,1,20,1,20,3,20,211,8,20,1,21,4,21,214,8,21,11,21,12,21,
        215,1,22,1,22,1,22,1,22,3,22,222,8,22,1,22,1,22,1,22,3,22,227,8,
        22,5,22,229,8,22,10,22,12,22,232,9,22,1,22,3,22,235,8,22,1,22,1,
        22,1,23,1,23,1,23,1,23,1,24,3,24,244,8,24,1,24,1,24,5,24,248,8,24,
        10,24,12,24,251,9,24,1,170,0,25,1,1,3,2,5,3,7,4,9,5,11,6,13,7,15,
        8,17,9,19,10,21,11,23,12,25,13,27,14,29,15,31,16,33,17,35,18,37,
        19,39,20,41,21,43,22,45,23,47,24,49,25,1,0,6,1,0,45,45,1,0,49,57,
        1,0,48,57,1,0,48,48,2,0,60,60,62,62,4,0,48,57,65,90,95,95,97,122,
        276,0,1,1,0,0,0,0,3,1,0,0,0,0,5,1,0,0,0,0,7,1,0,0,0,0,9,1,0,0,0,
        0,11,1,0,0,0,0,13,1,0,0,0,0,15,1,0,0,0,0,17,1,0,0,0,0,19,1,0,0,0,
        0,21,1,0,0,0,0,23,1,0,0,0,0,25,1,0,0,0,0,27,1,0,0,0,0,29,1,0,0,0,
        0,31,1,0,0,0,0,33,1,0,0,0,0,35,1,0,0,0,0,37,1,0,0,0,0,39,1,0,0,0,
        0,41,1,0,0,0,0,43,1,0,0,0,0,45,1,0,0,0,0,47,1,0,0,0,0,49,1,0,0,0,
        1,51,1,0,0,0,3,61,1,0,0,0,5,68,1,0,0,0,7,71,1,0,0,0,9,76,1,0,0,0,
        11,81,1,0,0,0,13,91,1,0,0,0,15,100,1,0,0,0,17,108,1,0,0,0,19,115,
        1,0,0,0,21,120,1,0,0,0,23,126,1,0,0,0,25,129,1,0,0,0,27,131,1,0,
        0,0,29,133,1,0,0,0,31,144,1,0,0,0,33,149,1,0,0,0,35,162,1,0,0,0,
        37,164,1,0,0,0,39,199,1,0,0,0,41,210,1,0,0,0,43,213,1,0,0,0,45,217,
        1,0,0,0,47,238,1,0,0,0,49,243,1,0,0,0,51,52,5,112,0,0,52,53,5,114,
        0,0,53,54,5,111,0,0,54,55,5,116,0,0,55,56,5,111,0,0,56,57,5,99,0,
        0,57,58,5,111,0,0,58,59,5,108,0,0,59,60,5,58,0,0,60,2,1,0,0,0,61,
        62,5,114,0,0,62,63,5,111,0,0,63,64,5,108,0,0,64,65,5,101,0,0,65,
        66,5,115,0,0,66,67,5,58,0,0,67,4,1,0,0,0,68,69,5,116,0,0,69,70,5,
        111,0,0,70,6,1,0,0,0,71,72,5,102,0,0,72,73,5,114,0,0,73,74,5,111,
        0,0,74,75,5,109,0,0,75,8,1,0,0,0,76,77,5,115,0,0,77,78,5,101,0,0,
        78,79,5,110,0,0,79,80,5,100,0,0,80,10,1,0,0,0,81,82,5,115,0,0,82,
        83,5,101,0,0,83,84,5,113,0,0,84,85,5,117,0,0,85,86,5,101,0,0,86,
        87,5,110,0,0,87,88,5,99,0,0,88,89,5,101,0,0,89,90,5,58,0,0,90,12,
        1,0,0,0,91,92,5,115,0,0,92,93,5,104,0,0,93,94,5,117,0,0,94,95,5,
        102,0,0,95,96,5,102,0,0,96,97,5,108,0,0,97,98,5,101,0,0,98,99,5,
        58,0,0,99,14,1,0,0,0,100,101,5,99,0,0,101,102,5,104,0,0,102,103,
        5,111,0,0,103,104,5,105,0,0,104,105,5,99,0,0,105,106,5,101,0,0,106,
        107,5,58,0,0,107,16,1,0,0,0,108,109,5,114,0,0,109,110,5,101,0,0,
        110,111,5,112,0,0,111,112,5,101,0,0,112,113,5,97,0,0,113,114,5,116,
        0,0,114,18,1,0,0,0,115,116,5,108,0,0,116,117,5,111,0,0,117,118,5,
        111,0,0,118,119,5,112,0,0,119,20,1,0,0,0,120,121,5,99,0,0,121,122,
        5,108,0,0,122,123,5,111,0,0,123,124,5,115,0,0,124,125,5,101,0,0,
        125,22,1,0,0,0,126,127,3,43,21,0,127,128,5,58,0,0,128,24,1,0,0,0,
        129,130,5,40,0,0,130,26,1,0,0,0,131,132,5,41,0,0,132,28,1,0,0,0,
        133,134,5,44,0,0,134,30,1,0,0,0,135,136,5,84,0,0,136,137,5,114,0,
        0,137,138,5,117,0,0,138,145,5,101,0,0,139,140,5,70,0,0,140,141,5,
        97,0,0,141,142,5,108,0,0,142,143,5,115,0,0,143,145,5,101,0,0,144,
        135,1,0,0,0,144,139,1,0,0,0,145,32,1,0,0,0,146,150,3,37,18,0,147,
        150,3,35,17,0,148,150,3,39,19,0,149,146,1,0,0,0,149,147,1,0,0,0,
        149,148,1,0,0,0,150,34,1,0,0,0,151,153,7,0,0,0,152,151,1,0,0,0,152,
        153,1,0,0,0,153,154,1,0,0,0,154,158,7,1,0,0,155,157,7,2,0,0,156,
        155,1,0,0,0,157,160,1,0,0,0,158,156,1,0,0,0,158,159,1,0,0,0,159,
        163,1,0,0,0,160,158,1,0,0,0,161,163,7,3,0,0,162,152,1,0,0,0,162,
        161,1,0,0,0,163,36,1,0,0,0,164,170,5,34,0,0,165,166,5,92,0,0,166,
        169,5,34,0,0,167,169,9,0,0,0,168,165,1,0,0,0,168,167,1,0,0,0,169,
        172,1,0,0,0,170,171,1,0,0,0,170,168,1,0,0,0,171,173,1,0,0,0,172,
        170,1,0,0,0,173,174,5,34,0,0,174,38,1,0,0,0,175,177,7,0,0,0,176,
        175,1,0,0,0,176,177,1,0,0,0,177,179,1,0,0,0,178,180,7,1,0,0,179,
        178,1,0,0,0,180,181,1,0,0,0,181,179,1,0,0,0,181,182,1,0,0,0,182,
        183,1,0,0,0,183,185,5,46,0,0,184,186,7,2,0,0,185,184,1,0,0,0,186,
        187,1,0,0,0,187,185,1,0,0,0,187,188,1,0,0,0,188,200,1,0,0,0,189,
        191,7,0,0,0,190,189,1,0,0,0,190,191,1,0,0,0,191,192,1,0,0,0,192,
        193,7,3,0,0,193,195,5,46,0,0,194,196,7,2,0,0,195,194,1,0,0,0,196,
        197,1,0,0,0,197,195,1,0,0,0,197,198,1,0,0,0,198,200,1,0,0,0,199,
        176,1,0,0,0,199,190,1,0,0,0,200,40,1,0,0,0,201,211,7,4,0,0,202,203,
        5,60,0,0,203,211,5,61,0,0,204,205,5,62,0,0,205,211,5,61,0,0,206,
        207,5,33,0,0,207,211,5,61,0,0,208,209,5,61,0,0,209,211,5,61,0,0,
        210,201,1,0,0,0,210,202,1,0,0,0,210,204,1,0,0,0,210,206,1,0,0,0,
        210,208,1,0,0,0,211,42,1,0,0,0,212,214,7,5,0,0,213,212,1,0,0,0,214,
        215,1,0,0,0,215,213,1,0,0,0,215,216,1,0,0,0,216,44,1,0,0,0,217,218,
        3,43,21,0,218,234,3,25,12,0,219,222,3,33,16,0,220,222,3,31,15,0,
        221,219,1,0,0,0,221,220,1,0,0,0,222,230,1,0,0,0,223,226,3,29,14,
        0,224,227,3,33,16,0,225,227,3,31,15,0,226,224,1,0,0,0,226,225,1,
        0,0,0,227,229,1,0,0,0,228,223,1,0,0,0,229,232,1,0,0,0,230,228,1,
        0,0,0,230,231,1,0,0,0,231,235,1,0,0,0,232,230,1,0,0,0,233,235,1,
        0,0,0,234,221,1,0,0,0,234,233,1,0,0,0,235,236,1,0,0,0,236,237,3,
        27,13,0,237,46,1,0,0,0,238,239,5,32,0,0,239,240,1,0,0,0,240,241,
        6,23,0,0,241,48,1,0,0,0,242,244,5,13,0,0,243,242,1,0,0,0,243,244,
        1,0,0,0,244,245,1,0,0,0,245,249,5,10,0,0,246,248,5,32,0,0,247,246,
        1,0,0,0,248,251,1,0,0,0,249,247,1,0,0,0,249,250,1,0,0,0,250,50,1,
        0,0,0,251,249,1,0,0,0,23,0,144,149,152,158,162,168,170,176,181,187,
        190,197,199,210,213,215,221,226,230,234,243,249,1,6,0,0
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
    COMMA = 15
    BOOLEAN = 16
    PRIMITIVE = 17
    INTEGER = 18
    STRING = 19
    FLOAT = 20
    COMPARATOR = 21
    WORD = 22
    CONSTRUCTORSTRING = 23
    WS = 24
    NL = 25

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'protocol:'", "'roles:'", "'to'", "'from'", "'send'", "'sequence:'", 
            "'shuffle:'", "'choice:'", "'repeat'", "'loop'", "'close'", 
            "'('", "')'", "','" ]

    symbolicNames = [ "<INVALID>",
            "PROTOCOL", "ROLES", "TO", "FROM", "SEND", "SEQUENCE", "SHUFFLE", 
            "CHOICE", "REPEAT", "LOOP", "CLOSE", "LOOPLABEL", "OPENINGBRACKET", 
            "CLOSINGBRACKET", "COMMA", "BOOLEAN", "PRIMITIVE", "INTEGER", 
            "STRING", "FLOAT", "COMPARATOR", "WORD", "CONSTRUCTORSTRING", 
            "WS", "NL" ]

    ruleNames = [ "PROTOCOL", "ROLES", "TO", "FROM", "SEND", "SEQUENCE", 
                  "SHUFFLE", "CHOICE", "REPEAT", "LOOP", "CLOSE", "LOOPLABEL", 
                  "OPENINGBRACKET", "CLOSINGBRACKET", "COMMA", "BOOLEAN", 
                  "PRIMITIVE", "INTEGER", "STRING", "FLOAT", "COMPARATOR", 
                  "WORD", "CONSTRUCTORSTRING", "WS", "NL" ]

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



