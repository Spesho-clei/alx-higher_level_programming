#!/usr/bin/python3
"""Defines Write_file module."""

def write_file(filename="", text=""):
    """
    Writes a string to a text file in UTF-8 format and returns the number of characters written.

    Args:
        filename (str, optional): The name of the file. Defaults to "".
        text (str, optional): The string to be written to the file. Defaults to "".

    Returns:
        int: The number of characters written.
    """
    with open(filename, 'w', encoding='utf-8') as file:
        num_chars_written = file.write(text)
        return num_chars_written
