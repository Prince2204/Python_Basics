# Handle the exception thrown by the code below by using try and except blocks.

try:
    for i in ['a','b','c']:
        print(i**2)
except TypeError:
    print("Power is applicable only on numbers. It seems you have not entered numbers")

# Handle the exception thrown by the code below by using try and except blocks. Then use a finally block to print 'All Done.'
try:
    x = 5
    y = 0
    z = x/y
except ZeroDivisionError:
    print("Denominator can't be zero")
except:
    print("Something worng happened")
finally:
    print("All Done.")


# Write a function that asks for an integer and prints the square of it. 
# Use a while loop with a try, except, else block to account for incorrect inputs.

def ask():
    while True:
        try:
            inp=int(input("Enter an Integer: "))
            print("Square of "+str(inp)+ " is: "+str(inp**2))
        except:
            print("Wrong Input!!!, Please enter an Integer")
        else:
            print("In else block")
            break   

ask()