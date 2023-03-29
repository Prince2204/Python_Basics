'''
import shutil
zippedFile="C:\\Users\\prinfnu\\Documents\\Python Scripts\\unzip_me_for_instructions.zip"
unzipfoldername="C:\\Users\\prinfnu\\Documents\\Python Scripts\\Instructions"
#unzipping the folder
shutil.unpack_archive(zippedFile,unzipfoldername,"zip")
'''

'''
#Reading the instructions.txt
instructions_file_path="C:\\Users\\prinfnu\\Documents\\Python Scripts\\Instructions\\extracted_content\\Instructions.txt"

instructions=open(instructions_file_path,'r')
#call read() or readlines() method
contents=instructions.read()       # getting the contents of file
print(contents)  
'''


