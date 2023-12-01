import importlib
import json

with open('modules.json') as modules:
    classNameToModulePath = json.load(modules)
    
modulePath = classNameToModulePath["Auto"]
my_module = importlib.import_module(modulePath)
autoClass = getattr(my_module, "Auto")
opel = autoClass("Opel", 21333)
gelijk = isinstance(opel, autoClass)
print(f"is instance = {gelijk}")