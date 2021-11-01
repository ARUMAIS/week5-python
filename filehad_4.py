"""
# ---------------------------
# File           : filehad_4.py
# Created        : 28-10-2021 19:42
# Author         : Aishwarya
# Version        : v1.0.0
# Licensing      : (c) 2021 Aishwarya,LYIT
#                  Available under GNU Public License (GPL)
# Description    
# ---------------------------
"""

import os
def walk_file_processing():
 """
 zip file demo
 :return:
 """
 for folder_name, sub_folders, file_names in os.walk("c:\\Users\\Aishu\\PycharmProjects"):
     print("Folder: ".format(folder_name))
    for sub_folder in sub_folders:
        print("Folder Name: {0} is a sub-folder in {1}".format(folder_name,sub_folder))
    for file_name in file_names:
        print("{0} is a file inside {1}".format(file_name, folder_name))
  print("\n")

if __name__=="__main__":
    walk_file_processing()
    