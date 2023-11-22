from __future__ import annotations
import typing

'''
The transition module offers the Transition and PredicateTransition classes that represent a transition between two
states in a Finite State Machine. A transition contains a message type, sender and receiver. A PredicateTransition
also contains a comparator and a value to check against to allow value checking in a transition.
'''
class Transition:

    def __init__(self, type: any, sender: str, receiver: str):
        self.type = type
        self.sender = sender
        self.receiver = receiver

    def getSender(self) -> str:
        return self.sender
    
    def getReceiver(self) -> str:
        return self.receiver
    
    def getType(self) -> any:
        return self.type
    
    def satisfies(self, other: Transition, _: any) -> bool:
        return self.type == other.type and self.sender == other.sender and self.receiver == other.receiver
    
    def __eq__(self, other: any) -> bool:
        if not isinstance(other, Transition):
            return False
        return type(self) == type(other) and self.type == other.type and self.sender == other.sender and self.receiver == other.receiver 

    def __hash__(self) -> int:
        return hash(self.type) + hash(self.sender) + hash(self.receiver)
    
    def __str__(self) -> str:
        return "send " + str(self.type) + " from " + str(self.sender) + " to " + str(self.receiver) 
    
'''
PredicateTransition is a specialisation of Transition: it is a transition that also features a comparator and value, 
which combine to a predicate that can be used to check if a value that is contained in a message is allowed or not.
'''
class PredicateTransition(Transition):

    def __init__(self, type: any, sender: str, receiver: str, comparator: str =None, value: any =None):
        super().__init__(type, sender, receiver)
        self.comparator = comparator
        self.value = value
    
    def satisfies(self, other: Transition, value: any) -> bool:
        if not super().satisfies(other, value):
            return False        
        isValueValid: bool = False
        match self.comparator:
            case '<':
                isValueValid = value < self.value
            case '<=':
                isValueValid = value <= self.value
            case '>':
                isValueValid = value > self.value
            case '>=':
                isValueValid = value >= self.value
            case '!=':
                isValueValid = value != self.value
            case '==':
                isValueValid = value == self.value
        return isValueValid

    def __eq__(self, other: any) -> bool:
        if not isinstance(other, PredicateTransition):
            return False
        return type(self) == type(other) and self.type == other.type and self.sender == other.sender and self.receiver == other.receiver and self.comparator == other.comparator and self.value == other.value

    def __hash__(self) -> int:
        return hash(self.type) + hash(self.sender) + hash(self.receiver) + hash(self.comparator) + hash(self.value)
    
    def __str__(self) -> str:
        return "send " + str(self.type) + "(" + str(self.comparator) + str(self.value) + ") from " + str(self.sender) + " to " + str(self.receiver)
