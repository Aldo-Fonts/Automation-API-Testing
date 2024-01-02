###############################################################################################################
# script:       error.py
# description:  This script has the fail messages in the platform
# version:      1.1
# creation:     December 9, 2023
# update:       January 2, 2024
###############################################################################################################
# Library/ies
from tkinter.messagebox import *

# Function(s)
def popup_showerror(error):
    showerror("Error", message(error))

def message(error_number):
    error_list = {
        "0" : "Fail! The program does not work correct :(",
        "1" : "The file does not contain an collection name",
        "2" : "The file does not contain an environment name",
        "3" : "The collection file does not containt the necessary information",
        "4" : "The collection was not saved on the path 'src/collection'",
        "5" : "The new collection can not be saved on the path 'src/collection'",
        "6" : "The folder is empty",
        "7" : "The path 'src/collection' is empty",
        "8" : "The given APIs does not can be added to the new collection",
        "9" : "Invalid request option"
    }
    return error_list[error_number]
