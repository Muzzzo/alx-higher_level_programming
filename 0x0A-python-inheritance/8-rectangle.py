#!/usr/bin/python3
# By - Musonda Christopher
# A Python class on BaseGeometry (based on 7-base_geometry.py)
"""class defines a Rectangle that inherits from BaseGeometry."""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """it represents a rectangle using BaseGeometry."""

    def __init__(self, width, height):
        """Intialization a new Rectangle.

        Arguments:
            width (int): The width of the new Rectangle.
            height (int): The height of the new Rectangle.
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
