grammar Pythonic;

tokens { INDENT, DEDENT }

@lexer::header{
from antlr_denter.DenterHelper import DenterHelper
from MyCoolParser import MyCoolParser
}
@lexer::members {
class MyCoolDenter(DenterHelper):
    def __init__(self, lexer, nl_token, indent_token, dedent_token, ignore_eof):
        super().__init__(nl_token, indent_token, dedent_token, ignore_eof)
        self.lexer: MyCoolLexer = lexer

    def pull_token(self):
        return super(MyCoolLexer, self.lexer).nextToken()

denter = None

def nextToken(self):
    if not self.denter:
        self.denter = self.MyCoolDenter(self, self.NL, MyCoolParser.INDENT, MyCoolParser.DEDENT, ***Should Ignore EOF***)
    return self.denter.next_token()

}

/*
 *   Parser rules
 */

protocol            : (atomicOperator | compoundOperator) EOF ;
atomicOperator      : (send) ;
compoundOperator    : sequence | shuffle | choice ;
sequence            : SEQUENCE (compoundOperator | atomicOperator)+ ;
shuffle             : SHUFFLE (compoundOperator | atomicOperator)+ ;
choice              : CHOICE (compoundOperator | atomicOperator)+ ;
send                : SEND WS WORD WS FROM WS WORD WS TO WS WORD NEWLINE ;

/*
 *   Lexer rules
 */

TO                  : 'to';
FROM                : 'from';
SEND                : 'send';
SEQUENCE            : 'sequence:' NEWLINE;
SHUFFLE             : 'shuffle:' NEWLINE;  
CHOICE              : 'choice:' NEWLINE;
WORD                : ([a-z] | [A-Z] | '_')+ ;
WS                  : (' ' | '\t') ;
NEWLINE             : ('\r'? '\n' | '\r')+ ;
NL                  : ('\r'? '\n' ' '*); 

