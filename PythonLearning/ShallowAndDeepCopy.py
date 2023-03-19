#Shallow and Deep copy in Python
# importing copy module
import copy

# initializing list 1
li1 = [1, 2, [3, 5], 4]
print("li1 ID: ", id(li1), "Value: ", li1)
# using copy for shallow copy
li2 = copy.copy(li1)
print("li2 ID: ", id(li2), "Value: ", li2)
# using deepcopy for deepcopy
li3 = copy.deepcopy(li1)
print("li3 ID: ", id(li3), "Value: ", li3)
#If object created using deep copy changes the original object will not change
li3[2][0]=6
print("list 3 after changes: ", li3)
print("list 1 after changes in list 1: ", li1)

#If object created using shallow copy changes the original object will also reflect change
li2[2][0]=16
print("list 2 after changes: ", li2)
print("list 1 after changes in list 2: ", li2)