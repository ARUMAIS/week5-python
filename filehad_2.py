"""
# ---------------------------
# File           : filehad_2.py
# Created        : 28-10-2021 19:16
# Author         : Aishwarya
# Version        : v1.0.0
# Licensing      : (c) 2021 Aishwarya,LYIT
#                  Available under GNU Public License (GPL)
# Description    
# ---------------------------
"""
def file_processing2(file_name):
    file_obj = open(file_name,"r+")
    for line in file_obj:
        print(line.rstrip()) #remove or strip the whitespace at the end of line when printing
    file_obj.write("\nThe stig,  L700084,M.eng mechanical engineering")
    file_obj.seek(0) #rewind the file to the beginning,satrt at position 0

    print("\nAfter new student was added:")
    all_file_contents = file_obj.read()
    print(all_file_contents)
    file_obj.close()


if __name__ == "__main__":
    file_processing2("sample.txt")