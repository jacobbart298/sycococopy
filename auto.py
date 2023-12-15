import builtins

class Auto:
    
    def __init__(self, merk, kilometerstand):
        self.merk = merk
        self.kilometerstand = kilometerstand
        
class Opel(Auto):
    
    def __init__(self, kilometerstand):
        super().__init__("Opel", kilometerstand)

# print(dir(builtins))

def testen():
    pass

# type_obj = type(testen)
# print(type_obj)
# print(type_obj.__name__)

# auto = Auto("Tesla", 835)
# type_obj = type(auto)
# print(type_obj)
# auto2 = type_obj("Opel", 3483)
# print(type(auto2))


# trueVal = True
# trueType = type(trueVal)
# print(trueType)
# trueVal2 = trueType(False)
# print(trueVal2)


# intVal = -2
# intType = type(intVal)
# print(intType)
# intVal2 = intType("3")
# print(intVal2)
