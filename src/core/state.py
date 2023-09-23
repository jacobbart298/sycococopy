from transition import Transition

class State:

    def __init__(self):
        self.transitionsToState = {}

    def addTransitionToState(self, transition, state):
        self.transitionsToState[transition] = state

    def getNextState(self, transition): 
        if self.containsTransition(transition):
            return self.transitionsToState[transition]
        return None
    
    def containsTransition(self, transition):
        return transition in self.transitionsToState

    def __str__(self) -> str:
        for transition in self.transitionsToState:
            return(f"I'm in a state that needs the transition: {str(transition)}")
