from src.core.transition import Transition

class State:

    def __init__(self):
        self.transitionsToStates = {}

    def addTransitionToState(self, transition, state):
        if self.containsTransition(transition):
            self.transitionsToStates[transition].append(state)
        else:
            self.transitionsToStates[transition] = [state]
    
    def getNextStates(self, transition): 
        if self.containsTransition(transition):
            return self.transitionsToStates[transition]
        return []
    
    def containsTransition(self, transition):
        return transition in self.transitionsToStates

    def __str__(self) -> str:
        if len(self.transitionsToStates) == 0:
            return "I'm a state that supports no transitions"
        else:
            strValue = "I am a state that supports the following transitions:\n"
            for transition in self.transitionsToStates:
                strValue += str(transition) + "\n"
            return strValue
