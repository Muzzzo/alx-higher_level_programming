#!/usr/bin/python3
# By - Musonda Christopher
# A Python class on BaseGeometry (based on 6-base_geometry.py)
"""class defines a base geometry BaseGeometry"""


class BaseGeometry:
    """reprsent a base geometry"""

    def area(self):
        """is not yet implemented."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate a parameter as an integer.

        Arguments:
            name (str): The name of the parameter.
            value (int): The parameter to validate.
        Raises 2 excepxns:
            TypeError: If value is not an integer.
            ValueError: If value is <= 0.
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
