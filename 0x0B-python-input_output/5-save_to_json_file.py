#!/usr/bin/python3

"""Define save_to_json_file module """
import json

def save_to_json_file(my_obj, filename):
    """
    Writes an object to a text file using a JSON representation.

    Args:
        my_obj: The Python object to be saved to the file.
        filename (str): The name of the file to write to.

    Returns:
        None
    """
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(my_obj, file)
