from __future__ import annotations #required to reference State class in typing from within the class itself
from src.core.transition import Transition, PredicateTransition
import typing

'''
The state module offers the State class that represents a state in a Finite State Machine.
A state contains a dictionary that maps transitions to other possible states (which allows for
non determinism in the FSM).
'''

class State:

    def __init__(self):
        # transitionsToStates is a dictionary that maps a transition to a set (no duplicates) of states that 
        # are reachable via the transition
        self.transitionsToStates: dict[Transition, set(State)] = {}

    # Function (used for construction of the fsm) that adds a new state to the mapping from the transition
    def addTransitionToState(self, transition: Transition, state: type[State]) -> None:
        if transition in self.transitionsToStates: 
            self.transitionsToStates[transition].add(state)
        else:
            self.transitionsToStates[transition] = {state}

    # Function that returns the set of states that are reachable from the transition in this State
    # return an empty set if the transition is not available from the State
    def getNextStates(self, transition: Transition) -> set(type[State]): 
        if self.containsTransition(transition):
            return self.transitionsToStates[transition]                
        return set()
    
    # Function that checks if a transition is present in the keys of the transitionsToStates attribute
    def containsTransition(self, checkTransition: Transition) -> bool:
        for transition in self.transitionsToStates:
            if transition.isSimilar(checkTransition):
                return True
        return False
    
    # Function that returns a list of transitions and predicatetransitions if they are present in the
    # transitionsToStates attribute
    def getTransitions(self, transition: Transition) -> list(Transition):
        transitions = []
        for state_transition in self.transitionsToStates:
            if state_transition.isSimilar(transition):
                transitions.append(state_transition)
        return transitions

    # Function used for troubleshooting, which identifies the state when printed
    def __str__(self) -> str:
        if len(self.transitionsToStates) == 0:
            return "I'm a state that supports no transitions"
        else:
            strValue = "I am a state that supports the following transitions:\n"
            for transition in self.transitionsToStates:
                strValue += str(transition) + "\n"
            return strValue
