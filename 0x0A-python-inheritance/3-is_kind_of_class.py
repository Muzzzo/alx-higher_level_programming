#!/usr/bin/python3
# By - Musonda Christopher
# A Python class function that returns True.
"""define a class and inherited class-checking function"""


def is_kind_of_class(obj, a_class):
    """check if an object is an instance or inherited instance of a class.

    Arguments:
        object (any): The object to check.
        a_class (type): The class to match the type of obj to.
    Returns:
        If the object is an instance or inherited instance of a_class - True.
        Otherwise - False.
    """
    if isinstance(obj, a_class):
        return True
    return False
