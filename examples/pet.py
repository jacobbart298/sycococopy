import inspect

class Pet():

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def makeSound(self):
        pass

    def __eq__(self, other) -> bool:
        return type(self) == type(other) and self.age == other.age and self.name == other.name
    
    def __hash__(self) -> int:
        return hash(type(self)) + hash(self.age) + hash(self.name)
        
    def __str__(self) -> str:
        return f"{type(self)}({self.age}, {self.name})"
    
class Cat(Pet):
    
    def makeSound(self):
        print("Miauw!")

class Dog(Pet):

    def __init__(self, name: str, age: int, height: float):
        super().__init__(name, age)
        self.height = height

    def __gt__(self, other):
        return self.height > other.height
    
    def __lt__(self, other):
        return self.height < other.height
    
    def __ge__(self, other):
        return self.height >= other.height
        
    def __le__(self, other):
        return self.height <= other.height
    
    def __eq__(self, other):
        return type(self) == type(other) and self.age == other.age and self.name == other.name and self.height == other.height
    
    def __hash__(self) -> int:
        return hash(self.age) + hash(self.name) + hash(self.height)
            
    def makeSound(self):
        print("Woef!")

def implements_method(class_obj, method_name):
    current_class = class_obj
    while current_class:
        if hasattr(current_class, method_name): # '__eq__'
            method = getattr(current_class, method_name)
            if callable(method):
                method_signature = inspect.signature(method)
                if method_signature.parameters.get('self') == inspect.Parameter('self', inspect.Parameter.POSITIONAL_OR_KEYWORD):
                    return True
        current_class = current_class.__bases__[0] if current_class.__bases__ else None
    return False