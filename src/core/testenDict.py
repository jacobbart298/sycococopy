from transition import Transition

dictionary = {}
transition = Transition("int", "Jacob", "Teun")
dictionary[1] = [transition]
print(f"Na toevoegen: {dictionary}")


transition2 = Transition("int", "Jacob", "Teun")
print(f"zit erin: {transition2 in dictionary[1]}")
dictionary[1].remove(transition2)
print(f"Na verwijderen: {dictionary}")