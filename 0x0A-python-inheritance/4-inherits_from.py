#!/usr/bin/python3
# By - Musonda Christopher
# A Python function that returns True,directly or indirectly.
"""define an inherited class-checking function"""


def inherits_from(obj, a_class):
    """checks if an object is an inherited instance of a class.

    Arguments:
        objects (any): The object to check.
        a_class (type): The class to match the type of obj to.
    Returns:
        If objects is an inherited instance of a_class - True.
        Otherwise - False.
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
