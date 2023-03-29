
import os,re,shutil

zippedFile="C:\\Users\\prinfnu\\Documents\\Python Scripts\\unzip_me_for_instructions.zip"
unzipfoldername="C:\\Users\\prinfnu\\Documents\\Python Scripts\\Instructions"
#unzipping the folder
shutil.unpack_archive(zippedFile,unzipfoldername,"zip")

#Reading the instructions.txt
instructions_file_path="C:\\Users\\prinfnu\\Documents\\Python Scripts\\Instructions\\extracted_content\\Instructions.txt"

instructions=open(instructions_file_path,'r')
#call read() or readlines() method
contents=instructions.read()       # getting the contents of file
print(contents)  

working_directory="C:\\Users\\prinfnu\\Documents\\Python Scripts\\Instructions\\extracted_content"
print(os.listdir(working_directory))

#function to check if file contains phone no in proper format 
def check_phn_no_in_file(file):
    pattern=r'\d{3}-\d{3}-\d{4}'
    #open file and read the content
    myfile=open(file,'r')
    contents=myfile.read()       # getting the contents of file
    # use regex to find the pattern
    if re.search(pattern,contents):
        # return list of phn numbers matched
        print("Match Found:")
        return re.search(pattern,contents)
    else:
        return ""

# initialising empty list to contain the list of matched phone numbers
results = []

# Using OS module to walk through the directory
for folder, subfolders,files in os.walk(working_directory):
     for f in files:
        full_path = folder+'\\'+f     
        print("Checking file {}".format(f))
        results.append(check_phn_no_in_file(full_path)) 

#printing the matched phone number
for r in results:
    if r != '':
        print(r.group())
    



