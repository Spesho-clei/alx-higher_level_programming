#!/usr/bin/python3
"""Defines a class MyInt that inherits from int."""

class MyInt(int):
    """
    This is the MyInt class, inheriting from int.

    MyInt has inverted == and != operators.
    """

    def __eq__(self, other):
        """
        Override the == operator to return the opposite result.

        Args:
            other (int): The value to compare with.

        Returns:
            bool: True if self is not equal to other, False otherwise.
        """
        return super().__ne__(other)

    def __ne__(self, other):
        """
        Override the != operator to return the opposite result.

        Args:
            other (int): The value to compare with.

        Returns:
            bool: True if self is equal to other, False otherwise.
        """
        return super().__eq__(other)
