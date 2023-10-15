from typing import Any
from src.core.state import State
from src.core.transition import Transition

class FSM:

    def __init__(self):
        self.states = {State()}
        self.newStates = set()

    def updateStates(self):
        self.states.clear()
        self.states.update(self.newStates)
        self.newStates.clear()

    def checkTransition(self, transition):
        transitions = []
        for state in self.states:
            if state.containsTransition(transition):
                transitions.extend(state.getTransitions(transition))
        return transitions
        
    def makeTransition(self, transition):
        for state in self.states:
            self.newStates.update(state.getNextStates(transition))

    def getStates(self):
        return list(self.states)