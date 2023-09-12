#!/usr/bin/python3

""" from_json_string module """
import json

def from_json_string(my_str):
    """
    Returns an object represented by a JSON string.

    Args:
        my_str (str): The JSON formatted string.

    Returns:
        object: The Python data structure represented by the JSON string.
    """
    return json.loads(my_str)
