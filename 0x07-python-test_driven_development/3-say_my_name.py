#!/usr/bin/python3
def say_my_name(first_name, last_name=""):
    """Print a formatted name.

    Args:
        first_name (str): The first name to print.
        last_name (str): The last name to print.
    Raises:
        TypeError: If either of first_name or last_name are not strings.
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    formatted_name = "My name is {} {}".format(first_name, last_name) if last_name else "My name is {}".format(first_name)
    print(formatted_name)
