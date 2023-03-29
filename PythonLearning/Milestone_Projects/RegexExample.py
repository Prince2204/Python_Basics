import re

text="My no is 9988-989-9898 "
pattern=r'\d{3}-\d{3}-\d{4}'

phone=re.search(pattern,text)
all_nums=re.findall(pattern,text)

#phone=re.search(r'\d\d\d-\d\d\d-\d\d\d\d',text)
#all_nums=re.findall(r'\d\d\d-\d\d\d-\d\d\d\d',text)
#phone1=re.search(r'\d{3}-\d{3}-\d{4}',text)

print(phone)
print(phone.group())

print(all_nums)

def check_phn_no_in_file(file,pattern):
    #open file and read the content
    myfile=open(file,'r')
    contents=myfile.read()       # getting the contents of file
    # use regex to find the pattern
    if re.search(pattern,contents):
        # return list of phn numbers matched
        return re.search(pattern,contents)
    else:
        return " "
