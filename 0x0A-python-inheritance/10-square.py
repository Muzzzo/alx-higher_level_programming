#!/usr/bin/python3
# By - Musonda Christopher
# A Python class Square that inherits from Rectangle (9-rectangle.py)
"""Defines a Rectangle subclass Square."""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """class that represents a square."""

    def __init__(self, size):
        """initializes a new square.

        Arguments:
            size (int): The size of the new square.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
