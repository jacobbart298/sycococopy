from src.core.exceptions.sycococopyexception import SycococopyException

'''
IllegalTypeException is raised when the given type cannot not recognised.
'''
class IllegalTypeException(SycococopyException):
        
    def __init__(self, illegalType: str):
        self.illegalType = illegalType
        
    def __str__(self) -> str:
        return f"\nILLEGAL TYPE PROVIDED: failed to recognise type {self.illegalType}!\n"
        