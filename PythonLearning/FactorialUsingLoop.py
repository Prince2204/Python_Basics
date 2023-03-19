#Factorial 

def factorial(inp):
    #print("inside factorial")
    result=1
    while inp >0 :  
        #print("inside while loop")
        result=result*inp
        inp=inp-1
    return result

inp_num=int(input("Enter no to get facorial: "))

print("Factorial of "+str(inp_num)+ " is: "+ str(factorial(inp_num)))




