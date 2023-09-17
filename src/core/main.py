from antlr4 import *
from antlr4.tree.Trees import Trees
from antlr4.tree.Tree import TerminalNodeImpl
from PythonicLexer import PythonicLexer
from PythonicParser import PythonicParser
from FSMbuilder import FSMbuilder
from transition import Transition

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
    # dump(tree, ruleNames=parser.ruleNames)
    fsm_builder = FSMbuilder()
    fsm = fsm_builder.visitSpecification(tree)
    print(fsm)
    print(str(fsm.state))
    fsm.makeTransition(Transition("String", "A", "B"))
    fsm.makeTransition(Transition("int", "B", "A"))
    fsm.makeTransition(Transition("iets", "Teun", "Jacob"))

if __name__ == '__main__':
    import sys
    main(sys.argv)