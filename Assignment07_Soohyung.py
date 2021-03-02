#----------------------------------------------------------#
# Title: Assignment 07
# Description: Working with pickling and exception handling
# ChangeLog: (Who, When, What)
# Soohyung Lee, 03/01/2021, Created script
#----------------------------------------------------------#

import pickle  # This imports code from another code file!

# --------------------- Data ------------------------#
strFileName = 'StudentData.dat'
lstStudent = []

#-------------------- Processing --------------------#
def save_data_to_file(file_name, list_of_data):
    file = open(file_name, "ab")
    pickle.dump(list_of_data, file)
    file.close()

def read_data_from_file(file_name):
    file = open(file_name, "rb")
    list_of_data = pickle.load(file)
    file.close()
    return list_of_data

#-------------------- Presentation -------------------#
try:
    print("Enter your 6-digit student ID number")
    intID = int(input("Student ID: "))
except ValueError:
    print("I am sorry but that's not a number!")
else:
    if intID < 100000 or intID > 999999:
        print("Please enter 6-digit valid student ID")
        input("\nPress any key to exit and try again")
    else:
        strName = str(input("Enter your Name: "))
        strMajor = str(input("Enter your major: "))
        lstStudent = [intID, strName, strMajor]

        save_data_to_file(strFileName, lstStudent)

        print(read_data_from_file(strFileName))




