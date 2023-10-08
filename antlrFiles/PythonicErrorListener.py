import sys
from antlr4 import *
from antlr4.error.ErrorListener import *
from pprint import pprint

from antlrFiles.PythonicLexer import PythonicLexer
from antlrFiles.PythonicParser import PythonicParser
from antlrFiles.pythonicSyntaxErrorException import PythonicSyntaxErrorException


class PythonicErrorListener(ErrorListener) :
    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        stack = recognizer.getRuleInvocationStack()
        stack.reverse()
        raise PythonicSyntaxErrorException(stack)
        # print("WHOOPS!")
        # print("rule stack: ", str(stack))
        # print("line", line, ":", column, "at", offendingSymbol, ":", msg)