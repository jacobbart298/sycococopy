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




    # # perform one walkthrough
    # state0a = monitor.fsm.getState()
    # monitor.verifySend(Transition("str", "buyer1", "seller"))
    # monitor.verifyReceive(Transition("str", "buyer1", "seller"))
    # state1a = monitor.fsm.getState()
    # monitor.verifySend(Transition("int", "seller", "buyer2"))
    # state2a = monitor.fsm.getState()
    # monitor.verifySend(Transition("int", "seller", "buyer1"))
    # state3a = monitor.fsm.getState()
    # monitor.verifySend(Transition("bool", "seller", "buyer1"))
    # state4a = monitor.fsm.getState()
    # monitor.verifyReceive(Transition("int", "seller", "buyer1"))
    # monitor.verifyReceive(Transition("bool", "seller", "buyer1"))
    # monitor.verifySend(Transition("str", "buyer1", "seller"))
    # state5a = monitor.fsm.getState()
    # monitor.verifySend(Transition("str", "buyer1", "buyer2"))
    # state6a = monitor.fsm.getState()

    # # reset FSM
    # monitor.fsm.state = state0a

    # monitor.transitionHistory = []
    # print("FSM reset")

    # # perform another walkthrough
    # state0b = monitor.fsm.getState()
    # monitor.verifySend(Transition("str", "buyer1", "seller"))
    # state1b = monitor.fsm.getState()
    # monitor.verifySend(Transition("int", "seller", "buyer1"))
    # state2b = monitor.fsm.getState()
    # monitor.verifySend(Transition("int", "seller", "buyer2"))
    # state3b = monitor.fsm.getState()
    # monitor.verifySend(Transition("str", "buyer1", "buyer2"))
    # state4b = monitor.fsm.getState()
    # monitor.verifySend(Transition("bool", "buyer2", "buyer1"))
    # state5b = monitor.fsm.getState()
    # monitor.verifySend(Transition("str", "buyer1", "buyer2"))
    # state6b = monitor.fsm.getState()

    # if (state0a == state0b
    #     and state1a == state1b 
    #     and state2a != state2b
    #     and state3a == state3b 
    #     and state4a != state4b
    #     and state5a == state5b
    #     and state6a == state6b):
    #     print("SUCCESS")
    # else:
    #     print("FAILURE")

if __name__ == '__main__':
    import sys
    main(sys.argv)