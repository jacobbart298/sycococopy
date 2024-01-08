from src.core.exceptions.sycococopyexception import SycococopyException

'''
ComparatorNotImplementedException is raised when a comparator is used with an object that does not implement it.
'''
class ComparatorNotImplementedException(SycococopyException):
        
    def __init__(self, comparator: str, type: any):
        self.type = type
        self.comparator = comparator
        
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
                method = "__eq__"
        return f"\nCOMPARATOR NOT IMPLEMENTED: class {self.type.__name__} does not implement method {method}!\n"  
        