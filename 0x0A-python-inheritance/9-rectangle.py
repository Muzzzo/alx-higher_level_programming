#!/usr/bin/python3
# By - Musonda Christopher
# A Python class Rectangle that inherits from BaseGeometry (7-base_geometry.py)
"""it defines a class Rectangle that inherits from BaseGeometry."""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """it represents a rectangle"""

    def __init__(self, width, height):
        """Intialize a new Rectangle.

        Arguments:
            width (int): The width of the new Rectangle.
            height (int): The height of the new Rectangle.
        """
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height

    def area(self):
        """returns area of the rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """returns print() and str() """
        string = "[" + str(self.__class__.__name__) + "] "
        string += str(self.__width) + "/" + str(self.__height)
        return string
