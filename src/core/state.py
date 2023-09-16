from transition import Transition

class State:

    def __init__(self):
        self.transitionsToState = {}

    def addTransitionToState(self, transition, state):
        self.transitionsToState[transition] = state

    def getNextState(self, transition: Transition): 
        for key in self.transitionsToState:
            if key == transition:
                return self.transitionsToState[key]
        return None



