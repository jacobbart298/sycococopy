import inspect 

class Auto:
    
    def __init__(self, merk, kilometerstand):
        self.merk = merk
        self.kilometerstand = kilometerstand
        
    # def __eq__(self, other: any) -> bool:
    #     return type(self) == type(other) and self.merk == other.merk and self.kilometerstand == other.kilometerstand
    
    def __hash__(self) -> int:
        return hash(self.merk) + hash(self.kilometerstand)
    
    def __str__(self):
        return f"{self.merk},{self.kilometerstand}"
    
    # def __gt__(self, other):
    #     return self.kilometerstand > other.kilometerstand
    
    # def __lt__(self, other):
    #     return other.__gt__(self)
        
class Opel(Auto):
    
    def __init__(self, kilometerstand):
        super().__init__("Opel", kilometerstand)

def implements_method(class_obj, method_name):
    current_class = class_obj
    while current_class:
        if hasattr(current_class, method_name):
            method = getattr(current_class, method_name)
            if callable(method):
                method_signature = inspect.signature(method)
                if method_signature.parameters.get('self') == inspect.Parameter('self', inspect.Parameter.POSITIONAL_OR_KEYWORD):
                    return True
        current_class = current_class.__bases__[0] if current_class.__bases__ else None
    return False