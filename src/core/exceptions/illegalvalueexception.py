from src.core.exceptions.sycococopyexception import SycococopyException

'''
IllegalValueException is raised when a type that is used in the protocol has
not been defined.
'''
class IllegalValueException(SycococopyException):
        
    def __init__(self, illegalValue: str, requiredType: str):
        self.illegalValue = illegalValue
        self.requiredType = requiredType
        
    def __str__(self) -> str:
        return f"\nILLEGAL VALUE PROVIDED: unable to construct an object with type '{self.requiredType}' from value '{self.illegalValue}'!\n"        
        