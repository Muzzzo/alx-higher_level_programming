#!/usr/bin/python3

"""
File: 101-add_attribute.py
Desc: Contains a single function defination
Author: Muzzo
Date Created: Sept 27, 2023
"""


def add_attribute(obj, att, value):
    """
    This function adds a new attribute to an object if  possible
    """
    if hasattr(obj, "__dict__"):
        setattr(obj, att, value)
    else:
        raise TypeError("can't add new attribute")
