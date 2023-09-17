from transition import Transition

class State:

    def __init__(self):
        self.transitionsToState = {}

    def addTransitionToState(self, transition, state):
        self.transitionsToState[transition] = state

    def getNextState(self, transition): 
        for key in self.transitionsToState:
            if key == transition:
                return self.transitionsToState[key]
        return None
    
    def __str__(self) -> str:
        for transition in self.transitionsToState:
            return(f"I'm in a state that needs the transition: {str(transition)}")



