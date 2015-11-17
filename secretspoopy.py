import random
import copy
names = []
names2 = []
def clash(names, names2):
    for i in range(len(names)):
        while names[i] == names2[i]:
            random.shuffle(names2)
            clash(names, names2)      
name = input("Add a person to the Secret Santa (type end to end): ")
while name != "end":
    names.append(name)
    print(names)
    names2 = copy.copy(names)
    print(names2)
    name = input("Add a person to the Secret Santa (type end to end): ")
if name == "end":
    for i in range(len(names)):
        clash(names, names2)
        print( names[i] + " will give a present to " + names2[i] )
