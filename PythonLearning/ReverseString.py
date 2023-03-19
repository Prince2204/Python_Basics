#write a program which uses a for loop to reverse a string. 
inp_str=input("Enter a string: ")
print("You have entered: ",inp_str) #hello
reversed_str=""
for i in range(len(inp_str)-1,-1,-1):
    reversed_str=reversed_str+inp_str[i]

print(reversed_str)

