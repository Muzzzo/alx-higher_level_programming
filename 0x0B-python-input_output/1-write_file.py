#!/usr/bin/python3
# By - Musonda
# A Python function that writes a string to a text file (UTF8).
"""define a file-writing function"""


def write_file(filename="", text=""):
    """Write a string to a UTF8 text file.

    Argumnets:
        filename (str): The name of the file to write.
        text (str): The text to write to the file.
    Rtns:
        The number of characters written.
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
