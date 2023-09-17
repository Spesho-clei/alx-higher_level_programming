#!/usr/bin/python3
"""Define Square class implement Rectangle
"""

from models.rectangle import Rectangle

class Square(Rectangle):
    """A class representing a square, which is a special case of a rectangle with equal sides."""

    def __init__(self, size, x=0, y=0, id=None):
        """
        Initialize a Square instance.

        Args:
            size (int): The size (side length) of the square.
            x (int, optional): The x-coordinate of the square's position. Defaults to 0.
            y (int, optional): The y-coordinate of the square's position. Defaults to 0.
            id (int, optional): The unique identifier for the square. Defaults to None.
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """int: The size (side length) of the square."""
        return self.width

    @size.setter
    def size(self, value):
        """
        Set the size (side length) of the square.

        Args:
            value (int): The size value to set.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than or equal to 0.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """
        Update the attributes of the square using either positional arguments or keyword arguments.

        Args:
            *args: Positional arguments (id, size, x, y).
            **kwargs: Keyword arguments for attributes.

        Note:
            If positional arguments (*args) are provided, they take precedence over keyword arguments (**kwargs).
        """
        if args:
            arg_names = ['id', 'size', 'x', 'y']
            for i, arg in enumerate(args):
                setattr(self, arg_names[i], arg)
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def __str__(self):
        """
        Get a string representation of the square.

        Returns:
            str: A string containing information about the square.
        """
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y, self.width)
    def to_dictionary(self):
        """
        Get the dictionary representation of the square.

        Returns:
            dict: A dictionary containing information about the square.
        """
        return {
            'id': self.id,
            'size': self.width,  # Since size and width are the same in a square
            'x': self.x,
            'y': self.y
        }
