import typing
from src.core.exceptions.sycococopyexception import SycococopyException

'''
The ComparatorNotImplementedException is raised when a type is used in the protocol that is not defined.
'''
class ComparatorNotImplementedException(SycococopyException):
        
    def __init__(self, comparator: str):
        self.comparator = comparator
        
    def __str__(self) -> str:
        return f"TYPE NOT RECOGNISED!\nThe type {self.illegalType} was not recognised as a valid type!"        
        