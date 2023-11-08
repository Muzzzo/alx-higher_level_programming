#!/usr/bin/python3
# By - Musonda
# A Python function that returns the JSON representation of an object (string)
"""it defines a string-to-JSON function"""
import json


def to_json_string(my_obj):
    """return the JSON representation of a string object"""
    return json.dumps(my_obj)
