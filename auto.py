class Auto:
    
    def __init__(self, merk, kilometerstand):
        self.merk = merk
        self.kilometerstand = kilometerstand
        
    def __eq__(self, other: any) -> bool:
        return type(self) == type(other) and self.merk == other.merk and self.kilometerstand == other.kilometerstand
    
    def __hash__(self) -> int:
        return hash(self.merk) + hash(self.kilometerstand)
    
    def __str__(self):
        return f"{self.merk},{self.kilometerstand}"
    
    def __gt__(self, other):
        return self.kilometerstand > other.kilometerstand
    
    def __lt__(self, other):
        return self.__gt__(other, self)
        
class Opel(Auto):
    
    def __init__(self, kilometerstand):
        super().__init__("Opel", kilometerstand)