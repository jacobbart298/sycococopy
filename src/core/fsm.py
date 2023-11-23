import typing
from src.core.state import State
from src.core.transition import Transition

'''
The FSM module is the starting point for the monitor to check whether a transition adheres to the
given protocol. 

The FSM class holds a set (no duplicates allowed) of possible states to support non-determinism (the
FSM is one of the possible states)
'''

class FSM:

    # On initialisation the FSM starts with a single State and an empty set on newStates
    def __init__(self):
        self.states: set(State) = {State()}
        self.newStates: set(State) = set()

    # Function that replaces states with newStates and empties the newStates set
    def updateStates(self) -> None:
        self.states.clear()
        self.states.update(self.newStates)
        self.newStates.clear()

    # Function that checks if a given Transition is available in the current states and
    # returns the list of possible transitions (Transition or PredicateTransition) 
    # VRAAG: KUNNEN WE HIER NIET BETER EEN SET MAKEN ZODAT DUPLICATES VERWIJDERD WORDEN?
    def checkTransition(self, transition: Transition) -> list[Transition]:
        transitions: list(Transition) = []
        for state in self.states:
            if state.containsTransition(transition):
                transitions.extend(state.getTransitions(transition))
        return transitions

    # Function that takes the current states and loads the next possible states for a given Transition
    # to the newStates set    
    def makeTransition(self, transition: Transition) -> None:
        for state in self.states:
            self.newStates.update(state.getNextStates(transition))

    # Function that returns the current states set as an iterable list  
    def getStates(self) -> list[State]:
        return list(self.states)