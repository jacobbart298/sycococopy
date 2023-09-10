grammar Pythonic;

tokens { INDENT, DEDENT }

@lexer::header{
from antlr_denter.DenterHelper import DenterHelper
from PythonicParser import PythonicParser
}
@lexer::members {
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

}

/*
 *   Parser rules
 */

protocol            : PROTOCOL WORD SLUIT block EOF ;
expression          : (send | sequence | shuffle | choice | close)+ ;
sequence            : SEQUENCE block ;
shuffle             : SHUFFLE block ;
choice              : CHOICE block ;
send                : SEND WORD FROM WORD TO WORD NL ;
close               : CLOSE WORD TO WORD NL;
block               : INDENT expression+ DEDENT ;


/*
 *   Lexer rules
 */

PROTOCOL            : 'protocol(' ;
SLUIT               : '):' ;
TO                  : 'to';
FROM                : 'from';
SEND                : 'send';
SEQUENCE            : 'sequence:';
SHUFFLE             : 'shuffle:' ;  
CHOICE              : 'choice:' ;
CLOSE               : 'close' ;
WORD                : ([a-z] | [A-Z] | [0-9] | '_' )+ ;
WS                  : (' ') -> skip;
NL                  : ('\r'? '\n' ' '*); 

