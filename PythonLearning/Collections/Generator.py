
#1 Create a generator that generates the squares of numbers up to some number N.
def gensquares(N):
    for num in range(N):
        yield num**2

print("printing squares of numbers from 1 to 10: ")
for x in gensquares(10):
    print(x)

#2 Create a generator that yields "n" random numbers between a low and high number (that are inputs).
#Note: Use the random library. For example:
import random

def rand_num(low,high,n):
    for num in range(n):
        yield random.randint(low,high)
    
print("\n printing 5 random numbers between low= 1 and high = 10")
for num in rand_num(1,10,5):
    print(num)

#3 Use the iter() function to convert the string below into an iterator:

s = 'hello'
print("\n Printing letter using iter()")
for letter in iter(s):
    print(letter)


#4 Print first 10 numbers of fibonacci series

def fibonacci_generator():
    n1=0
    n2=1
    while True:
        yield n1
        n1, n2 = n2, n1 + n2

sequence= fibonacci_generator()
n=0
print("\n printing first 10 numbers of fibonacci series using generators")
while n<10:
    print(next(sequence))
    n+=1

#5 define a generator comprehension for all the even numbers in 0-99:
even_gen = (i for i in range(100) if i%2 == 0)
print("\nChecking type of generator comprehension",type(even_gen))
print("\nPrinting even numbers between 0-99: ")
for num in even_gen:
    print(num)