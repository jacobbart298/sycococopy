from __future__ import annotations
from src.core.transition import Transition
import typing

'''
The state module offers the State class that represents a state in a Finite State Machine.
A state contains a dictionary that maps transitions to states.
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
    
    # Returns a list of possible Transitions in this State.
    def getTransitions(self) -> list[Transition]:
        return list(self.transitionsToStates.keys())

    def __str__(self) -> str:
        if len(self.transitionsToStates) == 0:
            return "I'm a state that supports no transitions"
        else:
            strValue = "I am a state that supports the following transitions:\n"
            for transition in self.transitionsToStates:
                strValue += str(transition) + "\n"
            return strValue
