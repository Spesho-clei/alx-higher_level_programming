#!/usr/bin/python3
"""Defines a class and inherited class-checking function."""

def is_kind_of_class(obj, a_class):
    """
    Check if the object is an instance of, or inherited from, the specified class.

    Args:
        obj: The object to be checked.
        a_class: The class to compare against.

    Returns:
        True if obj is an instance of a_class or inherited from a_class, otherwise False.
    """
    return isinstance(obj, a_class)
