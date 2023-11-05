from src.core.transition import Transition, PredicateTransition

class State:

    def __init__(self):
        self.transitionsToStates: dict[Transition, set(State)] = {}

    def addTransitionToState(self, transition, state):
        if transition in self.transitionsToStates: 
            self.transitionsToStates[transition].add(state)
        else:
            self.transitionsToStates[transition] = {state}
    
    def getNextStates(self, transition): 
        if self.containsTransition(transition):
            return self.transitionsToStates[transition]                
        return set()
    
    def containsTransition(self, checkTransition: Transition):
        for transition in self.transitionsToStates:
            if transition.isSimilar(checkTransition):
                return True
        return False
    
    def getTransitions(self, transition):
        transitions = []
        for state_transition in self.transitionsToStates:
            if state_transition.isSimilar(transition):
                transitions.append(state_transition)
        return transitions

    def __str__(self) -> str:
        if len(self.transitionsToStates) == 0:
            return "I'm a state that supports no transitions"
        else:
            strValue = "I am a state that supports the following transitions:\n"
            for transition in self.transitionsToStates:
                strValue += str(transition) + "\n"
            return strValue
