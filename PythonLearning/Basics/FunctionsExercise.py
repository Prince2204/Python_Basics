#Define a function called myfunc that takes in a string, and returns a matching string where every even letter is uppercase, and every odd letter is lowercase.
def myfunc(str_var):
    index=0
    return_var=[]
    ret_str=""
    for letter in str_var:
        if index%2==0:
            ret_str=ret_str+letter.upper()
        else:
            ret_str=ret_str+letter
        index+=1
    
    return ret_str

upr_str=myfunc("apple")
print(upr_str)

#Write a function that returns the lesser of two given numbers if both numbers are even, but returns the greater if one or both numbers are odd
def lesser_of_two_evens_or_odd_num(a,b):
    if a%2==0 and b%2==0:
        print("both the numbers are even hence returning the lesser among them")
        if a>b:
            return b
        else:
            return a
    else:
         print("one of the number is odd hence returning the greter among them")
         if a>b:
            return a
         else:
            return b
        
result1=lesser_of_two_evens_or_odd_num(2,4)
print(result1)
result2=lesser_of_two_evens_or_odd_num(2,5)
print(result2)

#Write a function takes a two-word string and returns True if both words begin with same letter
def check_strings(text):
    while len(text.split())!=2:
        print("Please enter 2 word string ")

    print("word is : ",text)
    if text.split()[0][0]==text.split()[1][0]:
        print(" Both words starts from same letter ")
        return True
    else:
        return False

check_strings('Levelheaded Llama') 
check_strings('Crazy Kangaroo') 

#MAKES TWENTY: Given two integers, return True if the sum of the integers is 20 or if one of the integers is 20.
# If not, return False
def makes_twenty(a,b):
    if a==20 or b==20 or a+b==20:
        return True
    else:
        return False

        
print(makes_twenty(20,10))
print(makes_twenty(12,8))
print(makes_twenty(2,3))

#Write a function that capitalizes the first and fourth letters of a name

def caps_func(name):
    if len(name)>=4:
        if len(name)==4:
            return name[0].upper()+name[1:3]+name[3].upper()
        else:
            return name[0].upper()+name[1:3]+name[3].upper()+name[4:]
    else:
        print("Please enter a name which is atleast 4 characters long ")
        return name

print(caps_func('macdonald'))
print(caps_func('mac'))
print(caps_func('macd'))

#Given a sentence, return a sentence with the words reversed

def reverse_words(sentence):
    word_list=sentence.split(" ")
    word_list.reverse()
    return(" ".join(word_list))


print(reverse_words("how are you"))

#Given an integer n, return True if n is within 10 of either 100 or 200
def almost_there(num):
    if abs(100-num)<=10 or abs(200-num)<=10:
        return True
    else:
        return False

print(almost_there(90))
print(almost_there(104))
print(almost_there(209))
print(almost_there(150))

#Given a list of ints, return True if the array contains a 3 next to a 3 somewhere.

def has_33(list_of_int):
    index=0
    while index < len(list_of_int)-1:
        if (list_of_int[index]==3 and list_of_int[index+1]==3):
            return True

        index+=1
    return False

print(has_33([1, 3, 3]))
print(has_33([1, 3, 1, 3]))
print(has_33([3, 1, 3])) 

#Given a string, return a string where for every character in the original there are three characters
def triplicate_chars(inp):
    result=""
    for letter in inp:
        result=result+(letter*3)

    return result

print(triplicate_chars('Hello')) 
print(triplicate_chars('Mississippi'))

#Given three integers between 1 and 11, if their sum is less than or equal to 21, return their sum. 
#If their sum exceeds 21 and there's an eleven, reduce the total sum by 10. 
#Finally, if the sum (even after adjustment) exceeds 21, return 'BUST'
def blackjack(a,b,c):
    #assuming the user input of 3 numbers are between 1 to 11
    if a+b+c <=21:
        return a+b+c
    elif a+b+c > 21 and (a==11 or b==11 or c==11):
        return a+b+c-10
    else:
        return "BUST"


print(blackjack(5,6,7))
print(blackjack(9,9,9))
print(blackjack(9,9,11))

#Return the sum of the numbers in the array, except ignore sections of numbers starting with a 6 
#and extending to the next 9 (every 6 will be followed by at least one 9). Return 0 for no numbers.

def summer_69(inp):
    if 6 in inp and 9 in inp:
        indx_of_6=inp.index(6)
        indx_of_9=inp.index(9) 
        list_new=inp[:indx_of_6]+inp[indx_of_9+1:]
        return sum(list_new)
    else:
        return sum(inp)

print(summer_69([1, 3, 5]))
print(summer_69([4, 5, 6, 7, 8, 9]))
print(summer_69([2, 1, 6, 9, 11]))

#COUNT PRIMES: Write a function that returns the number of prime numbers that exist up to and including a given number
#By convention, 0 and 1 are not prime.
def count_primes(num):
    prime_count=0
    if num==0 or num==1:
        print("0 and 1 are not prime numbers")
        return prime_count
    else:
        list_of_nums=[*range(2,num+1)]
        for x in list_of_nums:
            if check_prime(x):
                prime_count+=1

        return prime_count

        
#This functions check if num is prime or not
def check_prime(num):
    for i in range(2,num):
        if (num%i==0):
            #factor is found not a prime number
            return False

    return True

print(check_prime(16))

print(count_primes(100))


