#Count no of characters in a string:
inp_string=input("Enter a string: ")
char_count=0

for letter in inp_string:
    char_count += 1

print("You have entered: ",inp_string)
print("No of characters in string are: ",char_count)
