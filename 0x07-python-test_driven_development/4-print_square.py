#!/usr/bin/python3
# By - Musonda Christopher
# A Python function that prints a square with the character #.
"""
This is the "4-print_square" module.
The 4-print_square  module supplies one function, print_square(size).
"""
def print_square(size):
    """prints a square with "#"'s that has a length of size """
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if size > 0:
        print(("#" * size + "\n") * size, end="")
