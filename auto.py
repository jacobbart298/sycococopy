class Auto:
    
    def __init__(self, merk, kilometerstand):
        self.merk = merk
        self.kilometerstand = kilometerstand
        
    def __eq__(self, other: any) -> bool:
        return type(self) == type(other) and self.merk == other.merk and self.kilometerstand == other.kilometerstand
    
    def __hash__(self) -> int:
        return hash(self.merk) + hash(self.kilometerstand)
        
class Opel(Auto):
    
    def __init__(self, kilometerstand):
        super().__init__("Opel", kilometerstand)