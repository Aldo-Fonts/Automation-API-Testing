###############################################################################################################
# script:       fileFinder.py
# description:  This script open a file finder to read any file from the system
# version:      1.0
# creation:     December 9, 2023
# update:       December 14, 2023
###############################################################################################################
# Library/ies
from tkinter import filedialog
from tkinter import *
import os

# Function(s)
# openFile. It open the finder to upload any json file
def search():
    # It starts in /Documents
    document_path = os.path.expanduser('~') + "/Documents"
    # Open the file finder in /Documents, the window has the title 'Select a file' and only allows json files
    openFile = filedialog.askopenfilename(initialdir = document_path, title = "Select a file", filetypes = (("JSON files", ".json"),))
    # Return the path of the given file 
    return openFile