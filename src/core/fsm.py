from typing import Any
from src.core.state import State
from src.core.transition import Transition

class FSM:

    def __init__(self):
        self.states = {State()}

    def checkTransition(self, transition):
        transitions = []
        for state in self.states:
            if state.containsTransition(transition):
                transitions.append(state.getTransitions(transition))
        return transitions

    def makeTransition(self, transition):
        newStates = set()
        for state in self.states:
            newStates.update(state.getNextStates(transition))
        self.states = newStates
        
    def getStates(self):
        return list(self.states)