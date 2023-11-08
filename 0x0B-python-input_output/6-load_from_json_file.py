#!/usr/bin/python3
# by - Toggy
"""defines a JSON file-reading function"""
import json


def load_from_json_file(filename):
    """the 'f' creates a Python object from a JSON file"""
    with open(filename) as f:
        return json.load(f)
