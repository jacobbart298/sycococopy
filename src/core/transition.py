from __future__ import annotations #required to reference Transition class in typing from within the class itself
import typing

'''
The transition module offers the Transition and PredicateTransition classes that represent a transition between two.
states in a Finite State Machine. A transition contains a message type, sender and receiver. A PredicateTransition
in addition contains a comparator and value to check against to allow value checking in a transition.
'''
class Transition:

    def __init__(self, type: any, sender: str, receiver: str):
        self.type = type
        self.sender = sender
        self.receiver = receiver

    # Function that checks if the type, sender and receiver in a (Predicate)Transition are the same
    # It is used in the State class to verify if a transition to another state is possible
    # This is required, because the equality can't be used, as these also check for equality of transition-type
    def isSimilar(self: Transition, other: Transition) -> bool:
        return self.type == other.type and self.sender == other.sender and self.receiver == other.receiver

    def getSender(self) -> str:
        return self.sender
    
    def getReceiver(self) -> str:
        return self.receiver
    
    def getType(self) -> any:
        return self.type
    
    # Function used to check against a predicate in a PredicateTransition. Always returns True for regular Transition
    def isValid(self, value: any) -> bool:
        return True

    # Equality comparator, be aware that it also requires the type of transition (Transition / PredicateTransition) to be
    # identical. This is required to allow both a Transition and PredicateTransition to be available in a state's 
    # dictionary of transitions
    def __eq__(self, other: Transition) -> bool:
        return type(self) == type(other) and self.type == other.type and self.sender == other.sender and self.receiver == other.receiver 

    def __hash__(self):
        return hash(self.type) + hash(self.sender) + hash(self.receiver)
    
    def __str__(self) -> str:
        return "send " + str(self.type) + " from " + str(self.sender) + " to " + str(self.receiver) 
    
'''
Class that inherits from transition class, but includes a comparator and value, which combine to a predicate that
can be used to check if a value that's contained in a message is allowed or not
'''
class PredicateTransition(Transition):

    def __init__(self, type: any, sender: str, receiver: str, operator: str = None, value: any = None):
        super().__init__(type, sender, receiver)
        self.operator = operator
        self.value = value

    def __str__(self) -> str:
        return "send " + str(self.type) + "(" + str(self.operator) + str(self.value) + ") from " + str(self.sender) + " to " + str(self.receiver)

    # def getComparator(self) -> str:
    #     return self.operator
    
    # def getValue(self) -> any:
    #     return self.value

    # Function that checks if the given value is allowed by the predicate in the PredicateTransition or not
    def isValid(self, value: any) -> bool:
        match self.operator:
            case '<':
                return value < self.value
            case '<=':
                return value <= self.value
            case '>':
                return value > self.value
            case '>=':
                return value >= self.value
            case '!=':
                return value != self.value
            case '==':
                return value == self.value

    # Equality comparator, be aware that it also requires the type of transition (Transition / PredicateTransition) to be
    # identical. This is required to allow both a Transition and PredicateTransition to be available in a state's 
    # dictionary of transitions
    def __eq__(self, other: Transition) -> bool:
        return type(self) == type(other) and self.type == other.type and self.sender == other.sender and self.receiver == other.receiver and self.operator == other.comparator and self.value == other.value

    def __hash__(self):
        return hash(self.type) + hash(self.sender) + hash(self.receiver) + hash(self.operator) + hash(self.value)
    
    