

list1=[1, 2.34, True, "Prince", [10,11,12]]
list2=list("Hello")

print("e" in list2)
print("o" not in list2)

list1=[[0, 2], [4, 6], [8, 10], [12, 14]]
print(list1[0])
print(list1[3][1])

list2=["chair", "table", "desk", "lamp", "bed"]
print(list2[-5])
print("Most people own at least "+str(list1[0][1])+" "+list2[-5]+".")

list3=[0.98, 8.76, 6.54, 4.32]
print(list3[1:])
print(list3[1:3])
print(list3[:2])


arctic_animals=["penguin", "elephant", "polar bear", "walrus", "tiger", "reindeer"]
print(arctic_animals)
#del method: uses index to delete the item from list:
del arctic_animals[4]
print(arctic_animals)
#remove method uses actual value to remove the item from list:
arctic_animals.remove("elephant")
print(arctic_animals)
#append method to add "arctic fox" to list
arctic_animals.append("arctic fox")
print(arctic_animals)
#insert method to insert element at a certain position in list:
arctic_animals.insert(2,"snowy owl")
print(arctic_animals)
#sort method to arrnge the items in list
arctic_animals.sort()
print(arctic_animals)
#index method to get the index of a element in list:
print(arctic_animals.index("reindeer"))
#pop method to pop(remove last element) from list:
last_element=arctic_animals.pop()
print(last_element)
print(arctic_animals)

