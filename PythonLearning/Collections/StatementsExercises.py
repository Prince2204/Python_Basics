#Use for, .split(), and if to create a Statement that will print out words that start with 's':
st = 'Print only the words that start with s in this sentence'
print(st)
words_list=st.split(" ")


print("Printing all the words from above sentence that start's with 's'")

for words in words_list:
    if words.startswith("s"):
        print(words)

#Use range() to print all the even numbers from 0 to 10.
x=list(range(0,11,2))
for num in x:
    print(num)

#Use a List Comprehension to create a list of all numbers between 1 and 50 that are divisible by 3.
div_by_3=(x for x in range(1,51) if x%3==0)
for num in div_by_3:
    print(num)

#Go through the string below and if the length of a word is even print "even!"

st = 'Print every word in this sentence that has an even number of letters'
st_list=st.split(" ")
for word in st_list:
    if len(word)%2==0:
        print("word is: "+word+" and it's length is : even")

#Write a program that prints the integers from 1 to 100. But for multiples of three print "Fizz" instead of the number, 
#and for the multiples of five print "Buzz". For numbers which are multiples of both three and five print "FizzBuzz".

for num in range(1,101):
    if num%3==0 and num%5==0:
        print("FizzBuzz")
    elif num%3==0:
        print("Fizz")
    elif num%5==0:
        print("Buzz")
    else:
        print(num)

#Use List Comprehension to create a list of the first letters of every word in the string below:

st1 = 'Create a list of the first letters of every word in this string'
st1_list=st1.split(" ")
first_letter_list=(word[0] for word in st1_list)
for letter in first_letter_list:
    print(letter)
