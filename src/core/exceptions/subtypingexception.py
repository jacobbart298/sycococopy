from src.core.exceptions.sycococopyexception import SycococopyException

'''
SubtypingException is raised when the provided object is not an instance of the specified type.
'''
class SubtypingException(SycococopyException):
        
    def __init__(self, superType: type, subType: type):
        self.superType: str = superType.__name__
        self.subType: str = subType.__name__
        
    def __str__(self) -> str:
        return f"\nSUBTYPING VIOLATION\n'{self.subType}' is not a subclass of '{self.superType}'!\n"        
        