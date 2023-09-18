from antlr4 import *
from antlr4.tree.Trees import Trees
from antlr4.tree.Tree import TerminalNodeImpl
from PythonicLexer import PythonicLexer
from PythonicParser import PythonicParser
from FSMbuilder import FSMbuilder
from transition import Transition

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
    input = FileStream(argv[1])
    lexer = PythonicLexer(input)
    stream = CommonTokenStream(lexer)
    parser = PythonicParser(stream)
    tree = parser.specification() 
    # dump(tree, ruleNames=parser.ruleNames)
    fsm_builder = FSMbuilder()
    fsm = fsm_builder.visitSpecification(tree)

    # perform one walkthrough
    state0a = fsm.getState()
    fsm.makeTransition(Transition("str", "buyer1", "seller"))
    state1a = fsm.getState()
    fsm.makeTransition(Transition("int", "seller", "buyer2"))
    state2a = fsm.getState()
    fsm.makeTransition(Transition("int", "seller", "buyer1"))
    state3a = fsm.getState()
    fsm.makeTransition(Transition("bool", "seller", "buyer1"))
    state4a = fsm.getState()
    fsm.makeTransition(Transition("str", "buyer1", "seller"))
    state5a = fsm.getState()
    fsm.makeTransition(Transition("str", "buyer1", "buyer2"))
    state6a = fsm.getState()

    # reset FSM
    fsm.state = state0a
    fsm.transitionHistory = []
    print("FSM reset")

    # perform another walkthrough
    state0b = fsm.getState()
    fsm.makeTransition(Transition("str", "buyer1", "seller"))
    state1b = fsm.getState()
    fsm.makeTransition(Transition("int", "seller", "buyer1"))
    state2b = fsm.getState()
    fsm.makeTransition(Transition("int", "seller", "buyer2"))
    state3b = fsm.getState()
    fsm.makeTransition(Transition("str", "buyer1", "buyer2"))
    state4b = fsm.getState()
    fsm.makeTransition(Transition("bool", "buyer2", "buyer1"))
    state5b = fsm.getState()
    fsm.makeTransition(Transition("str", "buyer1", "buyer2"))
    state6b = fsm.getState()

    if (state0a == state0b
        and state1a == state1b 
        and state2a != state2b
        and state3a == state3b 
        and state4a != state4b
        and state5a == state5b
        and state6a == state6b):
        print("SUCCESS")
    else:
        print("FAILURE")

if __name__ == '__main__':
    import sys
    main(sys.argv)