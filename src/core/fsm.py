import typing
from src.core.state import State
from src.core.transition import Transition

'''
The FSM module is the starting point for the monitor to check whether a transition adheres to the
given protocol. 

An FSM object is responsible for managing a set of State objects.
'''

class FSM:

    def __init__(self):
        self.states: set(State) = {State()}
        
    def makeTransition(self, transition: Transition, item: any) -> bool:
        newStates = set()
        for state in self.states:
            for stateTransition in state.getTransitions():
                if stateTransition.satisfies(transition, item):
                    newStates.update(state.getNextStates(stateTransition))
        self.states = newStates
        return len(self.states) != 0
        
    def getStates(self) -> list[State]:
        return list(self.states)
    
    # Checks if at least one of the current states has no transitions and is hence in an end state
    def inFinalState(self) -> bool:        
        for state in self.states:
            if not state.getTransitions():
                return True
        return False