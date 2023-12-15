import builtins
from inspect import isfunction
from random import random

class Auto:
    
    def __init__(self, merk, kilometerstand):
        self.merk = merk
        self.kilometerstand = kilometerstand
        
class Opel(Auto):
    
    def __init__(self, kilometerstand):
        super().__init__("Opel", kilometerstand)

def testfunctie():
    print("gelukt!")

# functie = testfunctie
# print(functie)
# print(type(functie))

# print(isfunction(testfunctie))
# print(isfunction(type(Auto("Tesla", 23434))))
# print(isfunction(type(3)))

# print(type(functie))
# type_obj = type(testfunctie)
# print(type_obj)
# print(isinstance(type_obj, type_obj))

# print(dir(builtins))
# print(type([1,2,3]))
# print(type(int))
# print(type(1))