#Zipping and Unzipping using shutil library
import shutil

dir_to_zip="C:\\Users\\prinfnu\\Documents\\TestFiles\\extracted_content"
outfilename="C:\\Users\\prinfnu\\Documents\\ZippedTestFile"
#zip the folder
shutil.make_archive(outfilename,"zip",dir_to_zip)
#unzip the folder zipped above
zippedfilename="C:\\Users\\prinfnu\\Documents\\ZippedTestFile.zip"
unzipfoldername="C:\\Users\\prinfnu\\Documents\\UnZippedTestFile"
#unzipping the folder
shutil.unpack_archive(zippedfilename,unzipfoldername,"zip")
