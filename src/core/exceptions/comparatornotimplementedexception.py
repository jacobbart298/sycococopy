from src.core.exceptions.sycococopyexception import SycococopyException

'''
ComparatorNotImplementedException is raised when a comparator is used with an object that does not implement it.
'''
class ComparatorNotImplementedException(SycococopyException):
        
    def __init__(self, comparator: str, type: type):
        self.type: str = type.__name__
        self.comparator: str = comparator
        
    def __str__(self) -> str:
        match self.comparator:
            case '<':
                method = "__lt__"
            case '<=':
                method = "__le__"
            case '>':
                method = "__gt__"
            case '>=':
                method = "__ge__"
            case '==':
                method = "__eq__"
            case '!=':
                method = "__ne__"
        return f"\nCOMPARATOR NOT IMPLEMENTED: class '{self.type}' does not implement method '{method}'!\n"  
        