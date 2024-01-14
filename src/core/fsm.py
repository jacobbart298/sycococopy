from src.core.state import State
from src.core.transition import Transition, Lambda

'''
The FSM class holds a set of State objects that reflect the current possible states of the FSM.
'''

class FSM:

    def __init__(self):
        self.states: set(State) = {State()}
        
    def makeTransition(self, transition: Transition, item: any) -> bool:
        newStates: set[State] = set()
        while(len(self.states) != 0):
            state: State = self.states.pop()
            for stateTransition in state.getTransitions():
                if stateTransition == Lambda():
                    self.states.update(state.getNextStates(Lambda()))
                elif stateTransition.satisfies(transition, item):
                    newStates.update(state.getNextStates(stateTransition))
        self.states = newStates
        return len(self.states) != 0
        
    def getStates(self) -> list[State]:
        return list(self.states)
    
    # Checks if at least one of the current states has no transitions and is hence in an end state
    def isInFinalState(self) -> bool:        
        for state in self.states:
            if not state.getTransitions():
                return True
        return False