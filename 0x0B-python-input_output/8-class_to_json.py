#!/usr/bin/python3
# Done by - Musonda Christopher.Jr
""" funxn defines a Python class-to-JSON function."""


def class_to_json(obj):
    """return the dictionary representaxn of a simple data structure"""
    return obj.__dict__
