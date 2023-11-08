#!/usr/bin/python3
# By - Musonda Christopher
# A Python function that reads a text file (UTF8) and prints it to stdout.


"""this defines a text file-reading function."""
def read_file(filename=""):
    """Print the contents of a UTF8 text file to stdout."""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
