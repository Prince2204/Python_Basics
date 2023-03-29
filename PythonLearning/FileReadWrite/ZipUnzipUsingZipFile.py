#Zipping Files:
import zipfile

file1="C:\\Users\\prinfnu\\Documents\\TestFiles\\myfile.txt"
file2="C:\\Users\\prinfnu\\Documents\\TestFiles\\myfile1.txt"

zipFileName="C:\\Users\\prinfnu\\Documents\\TestFiles\\zipfile_test.zip"

zipFileObj=zipfile.ZipFile(zipFileName,'w')

zipFileObj.write(file1,compress_type=zipfile.ZIP_DEFLATED)
zipFileObj.write(file2,compress_type=zipfile.ZIP_DEFLATED)

zipFileObj.close()

#Unzipping the file

zipObj=zipfile.ZipFile("C:\\Users\\prinfnu\\Documents\\TestFiles\\zipfile_test.zip","r")

zipObj.extractall("C:\\Users\\prinfnu\\Documents\\TestFiles\\extracted_content")
