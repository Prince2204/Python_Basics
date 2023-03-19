
state_code={"BH":"Bihar","JH":"Jharkhand","KA":"Karnataka","UP":"Uttar Pradesh","DL":"Delhi"}

print(state_code["KA"])

print("TN" in state_code)

print("TN" not in state_code)

dict1={"Queen": "Bohemian Rhapsody", "Bee Gees": "Stayin' Alive", "U2": "One", 
       "The Beatles": "Hey Jude", "Bob Dylan": "Like A Rolling Stone"}

print("Length of dictionary: ",len(dict1))
#get the keys from dict an print it
print("Keys of dictionary dict1 are : ")
for key in dict1.keys():
    print(key)

#get the values from dict an print it
print("Values of dictionary dict1 are : ")
for value in dict1.values():
    print(value)

#get the items from dict an print it
print("Items of dictionary dict1 are : ")
for item in dict1.items():
    print(item)
#using get to retrieve the value for a key in dict
print(dict1.get("Promise of the Real","Key is not present in dict1"))
print(dict1.get("Bob Dylan","Key is not present in dict1"))


#USing fromkeys method to create a disctionary
# it takes 2 arguement. 1st arguement is a Iterable List or String that will be treated S KEYS OF DICTIONARY.
# Second Optional arguement is value and it will be same for all the keys in the dictionary.
dict_ex={}.fromkeys("bcdfghjklmnpqrstvwxyz", "consonant")
#printing each item of dictionary using for loop on dictionary's items method
for item in dict_ex.items():
    print(item)

fast_food_items = {"McDonald's": "Big Mac", "Burger King": "Whopper", "Chick-fil-A": "Original Chicken Sandwich"}
#getting the value for key "McDonald's"
print(fast_food_items["McDonald's"])
#Using popitem() to remove last item of dictionary
fast_food_items.popitem()
print(fast_food_items)
print(fast_food_items)


internet_celebrities = {"DrDisrespect": "YouTube", "ZLaner": "Facebook", "Ninja": "Mixer"}
print("Internet celebrity Dictionary: \n",internet_celebrities)
another_one = {"shroud": "Twitch"}
#add contents of dict another_one to dict internet_celebrities
internet_celebrities.update(another_one)
print("Internet celebrity Dictionary after update:\n ",internet_celebrities)
#using copy method to create a copy of dictionary
dict_copy=internet_celebrities.copy()
print("dict copy: \n",dict_copy )
#clearing the dictionary using clear()
internet_celebrities.clear()
print("internet_celebrities dict after clear: \n",internet_celebrities )
print("dict copy after clearing internet celebrity dict: \n",dict_copy )

#setdefault method: It checks if a key exists in dict, if exists it does nothing, if not exists
# it add the key and value to the dictionary
dict_copy.setdefault("India","Prince")
print(dict_copy)
dict_copy.setdefault("India","Prince Fnu")

#dict method: It is used to create a dictionary
empty_dict=dict()
print("empty_dict is : ",empty_dict)

create_dict=dict(yellow="Y", red="R")
print(create_dict)