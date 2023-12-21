import typing
from src.core.exceptions.sycococopyexception import SycococopyException

'''
The IllegalTypeException is raised when a type is used in the protocol that is not defined.
'''
class IllegalTypeException(SycococopyException):
        
    def __init__(self, illegalType: str):
        self.illegalType = illegalType
        
    def __str__(self) -> str:
        return f"TYPE NOT RECOGNISED!\nThe type {self.illegalType} was not recognised as a valid type!"        
        