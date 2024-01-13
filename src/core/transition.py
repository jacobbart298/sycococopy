from __future__ import annotations
import builtins
from src.core.exceptions.comparatornotimplementedexception import ComparatorNotImplementedException

'''
The transition module offers the Transition and PredicateTransition classes that represent a transition between two
states in a Finite State Machine. A transition contains a message type, sender and receiver. A PredicateTransition
also contains a comparator and a value to check against to allow value checking in a transition.
'''
class Transition:

    def __init__(self, type: type, sender: str, receiver: str):
        self.type = type
        self.sender = sender
        self.receiver = receiver

    def getSender(self) -> str:
        return self.sender
    
    def getReceiver(self) -> str:
        return self.receiver
    
    def getType(self) -> any:
        return self.type
    
    # Determines whether this Transition satisfies the given Transition.
    # That is to say, it checks whether this Transition's type, sender 
    # and receiver are equal to those of the given Transition.
    def satisfies(self, other: Transition, value: any) -> bool:
        if hasattr(builtins, type(value).__name__):
            typeValid = self.type == other.type
        else:
            typeValid = isinstance(value, self.type)
        return typeValid and self.sender == other.sender and self.receiver == other.receiver
    
    # Checks if the given object is a Transition equal to this Transition. 
    def __eq__(self, other: any) -> bool:
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
    
    # Determines whether this PredicateTransition satisfies the given Transition, value combination. 
    # That is to say, it checks whether this PredicateTransition's type, sender and receiver are 
    # equal to those of the given Transition and whether this PredicateTransition's value satisfies
    # the given value using this PredicateTransition's comparator.
    def satisfies(self, other: Transition, value: any) -> bool:
        if not super().satisfies(other, value):
            return False        
        match self.comparator:
            case '<':
                verdict = value.__lt__(self.value)
            case '<=':
                verdict = value.__le__(self.value)
            case '>':
                verdict = value.__gt__(self.value)
            case '>=':
                verdict = value.__ge__(self.value)
            case '==':
                verdict = value.__eq__(self.value)
            case '!=':
                verdict = value.__ne__(self.value)
        if verdict == NotImplemented:
            raise ComparatorNotImplementedException(self.comparator, type(value))
        else:
            return verdict

    # Checks if the given object is a PredicateTransition equal to this PredicateTransition. 
    def __eq__(self, other: any) -> bool:
        return type(self) == type(other) and self.type == other.type and self.sender == other.sender and self.receiver == other.receiver and self.comparator == other.comparator and self.value == other.value

    def __hash__(self) -> int:
        return hash(self.type) + hash(self.sender) + hash(self.receiver) + hash(self.comparator) + hash(self.value)
    
    def __str__(self) -> str:
        return "send " + str(self.type) + "(" + str(self.comparator) + str(self.value) + ") from " + str(self.sender) + " to " + str(self.receiver)
