#!/usr/bin/python3
""" class-to-JSON module."""

def class_to_json(obj):
    """
    Returns a dictionary description with simple data structures for JSON serialization.

    Args:
        obj: An instance of a class.

    Returns:
        dict: A dictionary description of the object.
    """
    result = {}
    for key, value in obj.__dict__.items():
        if isinstance(value, (list, dict, str, int, bool)):
            result[key] = value
    return result
