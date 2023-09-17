from typing import Any
from state import State
from transition import Transition

class FSM:

    def __init__(self):
        self.state = State()
        self.transitionHistory = []
        
    def makeTransition(self, transition):
        newState = self.state.getNextState(transition)
        # print(f"Making a transition {str(transition)} and newState equals: {str(newState)}")
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
    
    def __str__(self) -> str:
        print(self.state)
        key = list(self.state.transitionsToState.keys())[0]
        transition = self.state.transitionsToState[key]
        print(transition)
        self.makeTransition(transition)
        print(self.state)
