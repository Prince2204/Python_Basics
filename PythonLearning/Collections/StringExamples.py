var_str="Just Do It!"
# accessing by index
print(var_str[10])
# slicing
print("sliced string is: ",var_str[5:7])
print("sliced string is: ",var_str[8:])
print("sliced string is: ",var_str[:4])
#Slicing and concatenation
print("Don't" +" "+var_str[5:])
#type function
print(type(var_str))
print(type(2))
# str function: to convert to string
boolean_var=True
print("type is: ",type(boolean_var))
print("new type is: ",type(str(boolean_var)))
# escape sequence
print("\"Hello, I\'m Prince, it\'s nice to meet you!\"")
# Exercise
"""Using your knowledge of escape sequences, create a single print() statement 
with single string inside of it that displays this when the program is run:
 *******
  *****
   ***
    *
"""
print("\t*******\n\t *****\n\t  ***\n\t   *")


#String methds:

mixed_case="A Song of Ice and Fire"
print("Check if mixed_case is all upper : ",mixed_case.isupper())
print("Check if mixed_case is all lower : ",mixed_case.islower())
print("Changing all letters in mixed_case to upper : ",mixed_case.upper())
print("Changing all letters in mixed_case to lower : ",mixed_case.lower())
print("Check if mixed_case is title case : ",mixed_case.istitle())
title_case=mixed_case.title()
print("title case conversion of mixed case is: ",title_case)
print("Check if mixed case starts with \'A\': ",mixed_case.startswith("A"))
print("Check if mixed case ends with \'Fire\': ",mixed_case.endswith("Fire"))
words=mixed_case.split()
print(words)
joined_words="".join(words)
print("joined words: ",joined_words)
print("check if all are alphabets in joined words: ",joined_words.isalpha())


the_string="North Dakota"
print(the_string.rjust(17))
print(the_string.ljust(17,"*"))
center_plus=the_string.center(16,"+")
print(center_plus)
print(the_string.lstrip("North"))
print(center_plus.rstrip("+"))
print(center_plus.strip("+"))
print(the_string.replace("North","South"))

#Format method in string:
name=input("Applican't name: ")
major=input("Major in degree: ")
exp=input("Total Experience: ")

print(name+ " has done major in "+major+" and has "+exp+ " years of experience")
#using format:
print("{} has done major in {} and has {} years of experience".format(name,major,exp))



