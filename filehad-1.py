"""
# ---------------------------
# File           : filehad-1.py
# Created        : 19-10-2021 11:16
# Author         : Aishwarya
# Version        : v1.0.0
# Licensing      : (c) 2021 Aishwarya,LYIT
#                  Available under GNU Public License (GPL)
# Description    
# ---------------------------
"""


def file_processing(file_name):
    """
     Open a file with a list of students and print their details.
     Parameters:
     file_name name of file with students name, lnumber and course details
     Returns:
     none
     """
    lines = open(file_name).readlines()
    lines.sort() #this method can be used to sort a file
    for line in lines:
        student,l_num,course= line.split(",")

        print("student Name:\t{0} "
               "\nLNumber : \t{1} "
                "\nCourse :\t{2}"
              .format(student,l_num,course))


if __name__ == "__main__":
    file_processing("sample.txt")
