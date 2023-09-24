from typing import Any
from src.core.state import State
from src.core.transition import Transition

class FSM:

    def __init__(self):
        self.state = State()

    def checkTransition(self, transition):
        return self.state.containsTransition(transition)

    def makeTransition(self, transition):
        newState = self.state.getNextState(transition)        
        self.state = newState
        print(f"I just made the following transition: {str(transition)}")
        
    def getState(self):
        return self.state