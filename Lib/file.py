"""
My python library for file read/write usage.
"""
import os
import warnings


def checkFile(path):
    if os.path.isfile(path):  # If path is file
        return True  # return True
    else:  # else
        msg = "File does not exist! Maybe wrong path?"  # create warning message
        warnings.warn(msg)  # Show warning in console (this will point to log file in future update)
        return False  # return False


def read_TXT(path: str):
    """
    This function checks if the file exists and if exists return the file to a string.
    :param path: path to the file
    :return: a string with the contain of the file
    """
    data = ''  # Create an empty data string
    if checkFile(path):  # Check if file exists
        with open(path, "r") as myFile:  # Open the file if exists
            data = myFile.readlines()  # Read the file
    return data  # return data string


def write_TXT(path: str, text: str):
    """
    This function create a file and write in it the text.
    :param path: path to the file
    :param text: text to write in file
    :return: Nothing
    """
    with open(path, 'w') as f:
        f.write(text)
    f.close()
