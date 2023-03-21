
#File write
# mode 'w' overwrite the content of file if exists, if file doesn't exist it creates and write the data
with open('C:\\Users\\prinfnu\\Documents\\TestFiles\\myfile_write.txt','w') as my_text_file:
    my_text_file.write("Welcome to python learning!!!\n")
    my_text_file.write("I hope you are getting the lessons!!!")
  

with open('C:\\Users\\prinfnu\\Documents\\TestFiles\\myfile_write.txt','r') as my_text_file:
    contents=my_text_file.read()
    print(contents)


# mode 'a' will append the content of file if exists, if file doesn't exist it creates and write the data
with open('C:\\Users\\prinfnu\\Documents\\TestFiles\\myfile.txt','a') as my_text_file:
    my_text_file.write("Welcome to python learning!!!\n")
    my_text_file.write("I hope you are getting the lessons!!!")
  

with open('C:\\Users\\prinfnu\\Documents\\TestFiles\\myfile.txt','r') as my_text_file:
    contents=my_text_file.read()
    print(contents)

