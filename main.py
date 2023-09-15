from antlr4 import *
from antlr4.tree.Trees import Trees
from antlr4.tree.Tree import TerminalNodeImpl
from PythonicLexer import PythonicLexer
from PythonicParser import PythonicParser

def dump(node, depth=0, ruleNames=None):
    depthStr = '. ' * depth
    if isinstance(node, TerminalNodeImpl):
        print(f'{depthStr}{node.symbol}')
    else:
        print(f'{depthStr}{Trees.getNodeText(node, ruleNames)}')
        for child in node.children:
            dump(child, depth + 1, ruleNames)

def main(argv):
    input = FileStream(argv[1])
    lexer = PythonicLexer(input)
    stream = CommonTokenStream(lexer)
    parser = PythonicParser(stream)
    tree = parser.specification()
    print (Trees.toStringTree(tree)) 
    dump(tree, ruleNames=parser.ruleNames)

if __name__ == '__main__':
    import sys
    main(sys.argv)