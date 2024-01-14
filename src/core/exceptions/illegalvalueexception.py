from src.core.exceptions.sycococopyexception import SycococopyException

'''
IllegalValueException is raised when the provided value cannot be parsed to the given type.
'''
class IllegalValueException(SycococopyException):
        
    def __init__(self, illegalValue: str, requiredType: str):
        self.illegalValue = illegalValue
        self.requiredType = requiredType
        
    def __str__(self) -> str:
        return f"\nILLEGAL VALUE PROVIDED: unable to construct an object with type '{self.requiredType}' from value '{self.illegalValue}'!\n"        
        