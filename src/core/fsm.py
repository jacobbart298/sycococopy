from typing import Any
from state import State
from transition import Transition

class FSM:

    def __init__(self):
        self.state = State()
        self.transitionHistory = []
        
    def makeTransition(self, transition):
        newState = self.state.getNextState(transition)
        self.transitionHistory.append(transition)
        if newState is not None:
            self.state = newState
            print(f"I just made the following transition: {str(transition)}")
        else:
            print(f"ILLEGAL TRANSITION: {transition}")
            count = 0
            for transition in self.transitionHistory:
                print(f"{count}: {str(transition)}")
                count += 1
        
    def getState(self):
        return self.state
