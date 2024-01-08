from src.core.exceptions.sycococopyexception import SycococopyException

'''
The ComparatorNotImplementedException is raised when a comparison is used but the type does not implement its use.
'''
class ComparatorNotImplementedException(SycococopyException):
        
    def __init__(self, comparator: str, type: any):
        self.type = type
        self.comparator = comparator
        
    def __str__(self) -> str:
        return f"\nCOMPARATOR NOT IMPLEMENTED: \n{self.type.__name__} does not support {self.comparator} comparison\n"        
        