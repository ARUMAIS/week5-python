"""
# ---------------------------
# File           : filehad_5.py
# Created        : 29-10-2021 11:19
# Author         : Aishwarya
# Version        : v1.0.0
# Licensing      : (c) 2021 Aishwarya,LYIT
#                  Available under GNU Public License (GPL)
# Description    
# ---------------------------
"""
""" zip demo """
import zipfile, os

def zip_file_processing():
    """
    Zip File Demo

    :return:
    """
    # before running this example create a folder called c://zipDemo
    # add two files, one called sample2.txt the other called rubbish.txt
    os.chdir(os.path.normpath("C://zipdemo"))
    newZip = zipfile.ZipFile('myNew.zip', 'a')  # create a zip file. can be r,w,a
    new2= open.('sample2.txt','a')

    print("{}".format(newZip.printdir()))

    # newZip.write("RubbishFile.txt")  # add a second file

    print("\nFiles in the zip are: {}\n".format("c://zipDemo//extracthere"))
    newZip.extractall("c://zipDemo//extracthere")
    newZip.close()

if __name__ == "__main__":
    zip_file_processing()
