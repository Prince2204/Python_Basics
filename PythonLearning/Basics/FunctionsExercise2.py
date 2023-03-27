
#Write a function that computes the volume of a sphere given its radius.

def vol(rad):
    return 4/3*3.14*rad**3

print("Volume of sphere with radius 4 is :",str(round(vol(4),2)))
 
#Write a function that checks whether a number is in a given range (inclusive of high and low)
def check_in_range(num,low,high):
    if num>=low and num <=high:
        return "{} is in range given low={}, high={}".format(num,low,high)
    else:
        return "{} is not in range given low={}, high={}".format(num,low,high)
    
print(check_in_range(3,1,5))
print(check_in_range(13,1,5))

#Write a Python function that accepts a string and calculates the number of upper case letters and lower case letters.
#Sample String : 'Hello Mr. Rogers, how are you this fine Tuesday?'
#Expected Output : 
#No. of Upper case characters : 4
#No. of Lower case Characters : 33

def check_upper_lower(str):
    upperCount=0
    lowerCount=0
    for letter in str:
        if letter.isupper():
            upperCount+=1
        elif letter.islower():
            lowerCount+=1
        else:
            pass
            
    return (upperCount,lowerCount)

result=check_upper_lower("Hey How Are You")
result1=check_upper_lower("Hello Mr. Rogers, how are you this fine Tuesday?")

print("The string 'Hey How are you' contains {} upper and {} lower case letters.".format(result[0],result[1]))
print("The string 'Hello Mr. Rogers, how are you this fine Tuesday?' contains {} upper and {} lower case letters.".format(result1[0],result1[1]))

#Write a Python function that takes a list and returns a new list with unique elements of the first list.

#Sample List : [1,1,1,1,2,2,3,3,3,3,4,5]
#Unique List : [1, 2, 3, 4, 5]

def keep_unique(item_list):
    unique_elements=set(item_list)
    return list(unique_elements)

print(keep_unique([1,1,1,1,2,2,3,3,3,3,4,5]))

#Write a Python function to multiply all the numbers in a list.
def multiply_list(inp):
    res=1
    for n in inp:
        res=res*n
        
    return res

print("Multiplying all the elements of list [1, 2, 3, -4] and result is: ",str(multiply_list([1, 2, 3, -4])))

#Write a Python function that checks whether a word or phrase is palindrome or not.
#Note: A palindrome is word, phrase, or sequence that reads the same backward as forward, 
#e.g., madam,kayak,racecar, or a phrase "nurses run". 
#Hint: You may want to check out the .replace() method in a string to help out with dealing with spaces. 

def palindrome(inp):
    #check if there is any spaces?
    inp=inp.replace(" ","")
    reverse=inp[::-1]
    if inp==reverse:
        return True
    else:
        return False
    
print(palindrome('helleh'))
print(palindrome('run fast'))
print(palindrome('nurses run'))

#Write a Python function to check whether a string is pangram or not. (Assume the string passed in does not have any punctuation)
#Note : Pangrams are words or sentences containing every letter of the alphabet at least once.
#For example : "The quick brown fox jumps over the lazy dog"
import string

def check_pangram(inp):
    #replace spaces
    alphabet=string.ascii_lowercase
    #print(alphabet)
    inp=inp.replace(" ","").lower()
    print("input is: ",inp)
    sorted_unique_string="".join(sorted(list(set(inp))))
    print("sorted_unique_string is: ",sorted_unique_string)
    if alphabet in sorted_unique_string:
        return True
    else:
        return False
    
print(check_pangram("The quick brown fox jumps over the lazy dog!!"))
print(check_pangram("Hello!! I am done with the functions in python"))





