class Pet():

    def __init__(self, age: int, name: str):
        self.age = age
        self.name = name

    def __eq__(self, other) -> bool:
        return type(self) == type(other) and self.age == other.age and self.name == other.name
    
    def __hash__(self) -> int:
        return hash(self.age) + hash(self.name)
        
    def __str__(self) -> str:
        return f"{self.age}, {self.name}"
    
class Cat(Pet):
    pass

class Dog(Pet):
    pass