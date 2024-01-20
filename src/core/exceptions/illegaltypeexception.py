from src.core.exceptions.sycococopyexception import SycococopyException

'''
IllegalTypeException is raised when the given type cannot not recognised.
'''
class IllegalTypeException(SycococopyException):
        
    def __init__(self, type: type):
        self.type: str = type
        
    def __str__(self) -> str:
        return f"\nILLEGAL TYPE: failed to recognise type '{self.type}'!\n"
        