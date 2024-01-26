from src.core.state import State
from src.core.transition import Transition, EpsilonTransition

'''
The FSM class holds a set of State objects that reflect the states that the FSM
is currently in. An FSM is able to perform transitions and determine whether or
not it is in a final state.
'''

class FSM:

    def __init__(self):
        self.states: set(State) = {State()}
  
    # Performs all transitions that satisfy the given transition and item,
    # updating its set of states accordingly. In case no transitions are 
    # satisfactory, this method returns False; otherwise, it returns True.
    def makeTransition(self, transition: Transition, item: any) -> bool:
        newStates: set[State] = set()
        visitedStates: set[State] = set()
        while(len(self.states) != 0):
            state: State = self.states.pop()
            if not state in visitedStates:
                for stateTransition in state.getTransitions():
                    if isinstance(stateTransition, EpsilonTransition):
                        self.states.update(state.getNextStates(EpsilonTransition()))
                    elif stateTransition.satisfies(transition, item):
                        newStates.update(state.getNextStates(stateTransition))
                visitedStates.add(state)
        self.states = newStates
        return len(self.states) != 0
            
    # Checks if any of the FSM's current states has no transitions. If so, the 
    # FSM is in a final state and this method returns True; otherwise, False.
    def isInFinalState(self) -> bool:        
        for state in self.states:
            if state.isFinalState():
                return True
        return False

    # Returns the collection of states that the FSM is currently in as a list.
    def getStates(self) -> list[State]:
        return list(self.states)