#while Loop
inp=int(input("Enter a positive integer: "))
print("You have entered: ",inp)
user_inp=inp
sum=0
#sum of numbers
while inp>=1:
    sum=sum+inp
    inp-=1

print("Sum of numbers from "+str(user_inp)+ " to 1 is: " + str(sum))

#For loop

words="hello world"

for letter in words:
    print(letter)


    


