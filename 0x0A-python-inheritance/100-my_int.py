#!/usr/bin/python3
"""
A class MyInt which/that inherits from int
"""


class MyInt(int):
    """A class MyInt which inherits from the class int"""

    def __eq__(self, other):
        """ this overrides equals, hence inverting it"""
        return int(self) != int(other)

    def __ne__(self, other):
        """ _ne_ which overrides not-equals, inverting it"""
        return int(self) == int(other)
