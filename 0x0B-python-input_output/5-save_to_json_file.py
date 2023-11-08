#!/usr/bin/python3
# By -Muzzo
"""defines a JSON file-writing function."""
import json


def save_to_json_file(my_obj, filename):
    """the 'w' writes an object to a text file using JSON rep"""
    with open(filename, "w") as f:
        json.dump(my_obj, f)
