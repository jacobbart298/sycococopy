from typing import Any
from state import State
from transition import Transition

class FSM:

    def __init__(self):
        self.state = State()
        self.transitionHistory = []
        self.uncheckedReceives = {}

    def checkTransition(self, transition):
        newState = self.state.getNextState(transition)
        if newState is not None:
            return True
        else:
            return False
        
    def makeTransition(self, transition):
        newState = self.state.getNextState(transition)
        if newState is not None:
            self.uncheckedReceives[transition.getReceiver()].append(transition)
            self.state = newState
            self.transitionHistory.append(transition)
            print(f"I just made the following transition: {str(transition)}")
        else:
            print(f"ILLEGAL TRANSITION: {transition}")
            count = 0
            for transition in self.transitionHistory:
                print(f"{count}: {str(transition)}")
                count += 1

    def initialiseUncheckedReceives(self, roles):
        for role in roles:
            self.uncheckedReceives[role] = []
        
    def getState(self):
        return self.state
    
    def __str__(self) -> str:
        print(self.state)
        key = list(self.state.transitionsToState.keys())[0]
        transition = self.state.transitionsToState[key]
        print(transition)
        self.makeTransition(transition)
        print(self.state)
