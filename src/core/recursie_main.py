from antlr4 import *
from antlr4.tree.Trees import Trees
from antlr4.tree.Tree import TerminalNodeImpl
from antlrFiles.PythonicLexer import PythonicLexer
from antlrFiles.PythonicParser import PythonicParser
from src.core.FSMbuilder import FSMbuilder
from src.core.transition import Transition
from src.core.monitor import Monitor

#IMPORTANT: test file is now alloperationsgrammar.txt

def dump(node, depth=0, ruleNames=None):
    depthStr = '. ' * depth
    if isinstance(node, TerminalNodeImpl):
        print(f'{depthStr}{node.symbol}')
    else:
        print(f'{depthStr}{Trees.getNodeText(node, ruleNames)}')
        for child in node.children:
            dump(child, depth + 1, ruleNames)

def main(argv):
    monitor = Monitor(argv[1])

    


if __name__ == '__main__':
    import sys
    main(sys.argv)