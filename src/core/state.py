from src.core.transition import Transition, PredicateTransition

class State:

    def __init__(self):
        self.transitionsToStates: dict[Transition, set(State)] = {}

    def addTransitionToState(self, transition, state):
        if transition in self.transitionsToStates: 
            self.transitionsToStates[transition].add(state)
        else:
            self.transitionsToStates[transition] = {state}
    
    def getNextStates(self, transition, item): 
        nextStates = set()
        for transitionToStates in self.transitionsToStates:
            if transitionToStates.satisfies(transition) and transitionToStates.isValid(item):
                nextStates.update(self.transitionsToStates[transitionToStates])
        return nextStates
    
    def containsTransition(self, transition):
        return transition in self.transitionsToStates
    
    def getTransitions(self):
        return self.transitionsToStates.keys()

    def __str__(self) -> str:
        if len(self.transitionsToStates) == 0:
            return "I'm a state that supports no transitions"
        else:
            strValue = "I am a state that supports the following transitions:\n"
            for transition in self.transitionsToStates:
                strValue += str(transition) + "\n"
            return strValue
