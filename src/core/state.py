from src.core.transition import Transition

class State:

    def __init__(self):
        self.transitionsToStates = {}

    def addTransitionToState(self, transition, state):
        self.transitionsToStates[transition] = state

    def getNextState(self, transition): 
        if self.containsTransition(transition):
            return self.transitionsToStates[transition]
        return None
    
    def containsTransition(self, transition):
        return transition in self.transitionsToStates

    def __str__(self) -> str:
        if len(self.transitionsToStates) == 0:
            return "I'm a state without transitions"
        strValue = ""
        for transition in self.transitionsToStates:
            strValue += "I'm in a state that needs the transition:" + str(transition) + "\n"
        return strValue
