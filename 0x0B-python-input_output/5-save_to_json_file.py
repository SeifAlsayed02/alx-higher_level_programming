#!/usr/bin/python3
"""
=============================
Module with the method save_to_json_file
=============================
"""


import json


def save_to_json_file(my_obj, filename):
    """
    function that writes an Object to a text file,
    using a JSON representation
    """

    with open(filename, "w") as file:
        file.write(json.dumps(my_obj))
