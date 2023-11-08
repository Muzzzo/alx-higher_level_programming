#!/usr/bin/python3
# By - Musonda Christopher
"""defines a JSON-to-object function"""
import json


def from_json_string(my_str):
    """returns the Python object representaxn of a JSON string"""
    return json.loads(my_str)
