from __future__ import annotations
from src.core.transition import Transition

'''
The State class represents a state in a Finite State Machine.
A state contains a dictionary that maps transitions to new states.
'''
class State:

    def __init__(self):
        self.transitionsToStates: dict[Transition, set[State]] = {}

    # Adds a Transition, State pair to this State.
    def addTransitionToState(self, transition: Transition, state: State) -> None:
        if transition in self.transitionsToStates: 
            self.transitionsToStates[transition].add(state)
        else:
            self.transitionsToStates[transition] = {state}
    
    # Returns the set of States that are reachable from this State with the given Transition.
    # If this State does not feature the given Transition, an empty set is returned.
    def getNextStates(self, transition: Transition) -> set[State]: 
        if transition in self.transitionsToStates:
           return self.transitionsToStates[transition]
        return set()
    
    # Returns a set of possible Transitions in this State.
    def getTransitions(self) -> set[Transition]:
        return set(self.transitionsToStates.keys())

    # Returns True if the state is a final state, False otherwise
    def isFinalState(self) -> bool:
        return len(self.transitionsToStates) == 0