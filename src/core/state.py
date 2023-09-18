from transition import Transition

class State:

    def __init__(self):
        self.transitionsToState = {}

    def addTransitionToState(self, transition, state):
        self.transitionsToState[transition] = state

    def getNextState(self, transition): 
        if transition in self.transitionsToState:
            return self.transitionsToState[transition]
        return None
    
    def __str__(self) -> str:
        for transition in self.transitionsToState:
            return(f"I'm in a state that needs the transition: {str(transition)}")
