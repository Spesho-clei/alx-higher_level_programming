#!/usr/bin/python3
"""Defines a module appends a string."""

def append_write(filename="", text=""):
    """
    Appends a string to the end of a text file in UTF-8 format and returns the number of characters added.

    Args:
        filename (str, optional): The name of the file. Defaults to "".
        text (str, optional): The string to be appended to the file. Defaults to "".

    Returns:
        int: The number of characters added.
    """
    with open(filename, 'a', encoding='utf-8') as file:
        num_chars_added = file.write(text)
        return num_chars_added
