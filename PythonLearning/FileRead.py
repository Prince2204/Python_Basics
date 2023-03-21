
#File read
# Open  a file
myfile=open('C:\\Users\\prinfnu\\Documents\\TestFiles\\myfile.txt','r')
#call read() or readlines() method
contents=myfile.read()       # getting the contents of file
print(contents)              #printing the contents

print(myfile.readable())     # checking if file is readable

#Another Option to traverse the file
myfile.seek(0)               #moving back the file pointer to begining
count = 0
# Strips the newline character
for line in myfile:
    count += 1
    print("Line{}: {}".format(count, line.strip()))

#closing the file
myfile.close()
print("closed the file")



