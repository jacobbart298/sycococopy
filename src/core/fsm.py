from typing import Any
from src.core.state import State
from src.core.transition import Transition

class FSM:

    def __init__(self):
        self.state = State()
        self.transitionHistory = []
        self.uncheckedReceives = {}

    def removeFromUncheckedReceives(self, transition):
        self.uncheckedReceives[transition.getReceiver()].remove(transition)

    def checkTransition(self, transition):
        return (self.state.containsTransition(transition) 
                and self.uncheckedReceives[transition.getSender()] == []) #isEmpty doesn't exist, instead compare with empty list
    
    def checkReceive(self, transition):
        return transition in self.uncheckedReceives[transition.getReceiver()]

    def makeTransition(self, transition):
        self.transitionHistory.append(transition)
        newState = self.state.getNextState(transition)
        if newState is not None:
            self.uncheckedReceives[transition.getReceiver()].append(transition)
            self.state = newState
            print(f"I just made the following transition: {str(transition)}")
        else:
            print(f"ILLEGAL TRANSITION: {transition}")
            count = 0
            for transition in self.transitionHistory:
                print(f"{count}: {str(transition)}")
                count += 1
            return self.transitionHistory #For now returns the transitionHistory for an Illegal transition (so I can test), I think we need to raise an exception here?

    def initialiseUncheckedReceives(self, roles):
        for role in roles:
            self.uncheckedReceives[role] = []
        
    def getState(self):
        return self.state
    
    def __str__(self) -> str:
        print(self.state)
        key = list(self.state.transitionsToState.keys())[0]
        transition = self.state.transitionsToState[key]
        print(transition)
        self.makeTransition(transition)
        print(self.state)
