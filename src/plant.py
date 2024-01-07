class Plant():
    
    def __eq__(self, other) -> bool:
        return type(self) == type(other)
    
    def __hash__(self) -> int:
        return hash(type(self))
    
    def __str__(self) -> str:
        return self.__class__.__name__
    
class Sansevieria(Plant):
    pass

class Aralia(Plant):
    pass