#For this programming challenge, write a function in a .py file 
#which takes 1 string as an argument, finds out the number of words in that string, 
#then returns that number.

str_1 = "James Bond is 007."
str_2 = "When the moon hits your eye like a big pizza pie, that's amore!"
str_3 = "Anyway, like I was sayin', shrimp is the fruit of the sea. You can barbecue it, boil it, broil it, bake it, \
saute it. Dey's uh, shrimp-kabobs, shrimp creole, shrimp gumbo. Pan fried, deep fried, stir-fried. There's pineapple \
shrimp, lemon shrimp, coconut shrimp, pepper shrimp, shrimp soup, shrimp stew, shrimp salad, shrimp and potatoes, \
shrimp burger, shrimp sandwich. That- that's about it."

#Approach 1
print(len(str_1.split(" ")))
print(len(str_2.split(" ")))
print(len(str_3.split(" ")))

#Approach 2
def word_counter(words):
    spaces_and_letters = ""
    word_count = 1
    for i in words:
        if i.isalnum() or i.isspace() or i == "-" or i == "'":
            spaces_and_letters += i
    for j in spaces_and_letters:
        if j == " ":
            word_count += 1
    return word_count
 
 
print(word_counter(str_1))
print(word_counter(str_2))
print(word_counter(str_3))