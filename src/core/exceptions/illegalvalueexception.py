import typing
from src.core.exceptions.sycococopyexception import SycococopyException

'''
The IllegalTypeException is raised when a type is used in the protocol that is not defined.
'''
class IllegalValueException(SycococopyException):
        
    def __init__(self, illegalValue: str, requiredType: str):
        self.illegalValue = illegalValue
        self.requiredType = requiredType
        
    def __str__(self) -> str:
        return f"\nILLEGAL VALUE PROVIDED:\nUnable to construct object with type '{self.requiredType}' from value '{self.illegalValue}'!\n"        
        