from typing import Any
from src.core.state import State
from src.core.transition import Transition, PredicateTransition

class FSM:

    def __init__(self):
        self.states = {State()}
        
    def makeTransition(self, transition, item = None):
        newStates = set()
        for state in self.states:
            for stateTransition in state.getTransitions():
                if stateTransition.satisfies(transition, item):
                    newStates.update(state.getNextStates(stateTransition))
        self.states = newStates
        return len(self.states) != 0
        
    def getStates(self):
        return list(self.states)