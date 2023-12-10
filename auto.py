class Auto:
    
    def __init__(self, merk, kilometerstand):
        self.merk = merk
        self.kilometerstand = kilometerstand
        
class Opel(Auto):
    
    def __init__(self, kilometerstand):
        super().__init__("Opel", kilometerstand)


auto = Auto("Mercedes", 12422)
opel = Opel(746384)
# print(isinstance(opel, Auto))

stringtype = type(int)
print(stringtype)

# Note that this approach assumes that the type string you're trying to convert is a built-in type,
# and it relies on the name of the type being the same as the string representation of the type.
def convert_to_type(type_str):
    try:
        type_object = getattr(__builtins__, type_str)
        if type(type_object) is type:
            print("type found")
            return type_object
        else:
            print("type not found")
            return None
    except AttributeError:
        print("attribute error")
        return None

str = convert_to_type("onzin")


print(type(list))
print(type(dict))
print(type(bool))
print(type(""))
print(type(sum))
