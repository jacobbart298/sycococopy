from src.core.exceptions.sycococopyexception import SycococopyException

'''
IllegalValueException is raised when the provided value cannot be parsed to the given type.
'''
class IllegalValueException(SycococopyException):
        
    def __init__(self, value: str, type: type):
        self.value: str = value
        self.type: str = type.__name__
        
    def __str__(self) -> str:
        return f"\nILLEGAL EXPRESSION: unable to construct an object of type '{self.type}' from expression '{self.value}'!\n"        
        