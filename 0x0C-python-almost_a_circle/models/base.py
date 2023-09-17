#!/usr/bin/python3
"""Defines Base class"""
import json
import csv

class Base:
    """Base class body.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize Id in a constructor
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Get the JSON string representation of a list of dictionaries.

        Args:
            list_dictionaries (list): A list of dictionaries.

        Returns:
            str: The JSON string representation.
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)
    @staticmethod
    def from_json_string(json_string):
        """
        Get the list of dictionaries from a JSON string representation.

        Args:
            json_string (str): The JSON string representation.

        Returns:
            list: A list of dictionaries.
        """
        if json_string is None or json_string == "":
            return []
        else:
            return json.loads(json_string)
    @classmethod
    def create(cls, **dictionary):
        """
        Create an instance with attributes set based on the provided dictionary.

        Args:
            **dictionary: A dictionary of attributes.

        Returns:
            Base: An instance of the class with attributes set.
        """
        if cls.__name__ == "Rectangle":
            dummy_instance = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy_instance = cls(1)
        else:
            return None

        dummy_instance.update(**dictionary)
        return dummy_instance
    @classmethod
    def save_to_file_csv(cls, list_objs):
        """
        Serialize a list of instances to a CSV file.

        Args:
            list_objs (list): A list of instances.
        """
        filename = "{}.csv".format(cls.__name__)
        with open(filename, mode='w', newline='') as file:
            writer = csv.writer(file)
            for obj in list_objs:
                if cls.__name__ == "Rectangle":
                    writer.writerow([obj.id, obj.width, obj.height, obj.x, obj.y])
                elif cls.__name__ == "Square":
                    writer.writerow([obj.id, obj.size, obj.x, obj.y])

    @classmethod
    def load_from_file_csv(cls):
        """
        Deserialize a list of instances from a CSV file.

        Returns:
            list: A list of instances.
        """
        filename = "{}.csv".format(cls.__name__)
        try:
            with open(filename, mode='r') as file:
                reader = csv.reader(file)
                instances = []
                for row in reader:
                    if cls.__name__ == "Rectangle":
                        obj = cls(int(row[1]), int(row[2]), int(row[3]), int(row[4]), int(row[0]))
                    elif cls.__name__ == "Square":
                        obj = cls(int(row[1]), int(row[2]), int(row[3]), int(row[0]))
                    instances.append(obj)
                return instances
        except FileNotFoundError:
            return []
    @classmethod
    def load_from_file(cls):
        """
        Load a list of instances from a file.

        Returns:
            list: A list of instances.
        """
        filename = "{}.json".format(cls.__name__)
        try:
            with open(filename, mode='r', encoding='utf-8') as file:
                json_string = file.read()
                list_dicts = cls.from_json_string(json_string)
                return [cls.create(**dict_item) for dict_item in list_dicts]
        except FileNotFoundError:
            return []
    @classmethod
    def save_to_file(cls, list_objs):
        """
        Write the JSON string representation of list_objs to a file.

        Args:
            list_objs (list): A list of instances.

        Note:
            The filename will be "<Class name>.json" (e.g., "Rectangle.json").
        """
        if list_objs is None:
            list_objs = []
        filename = "{}.json".format(cls.__name__)
        with open(filename, mode='w', encoding='utf-8') as file:
            json_string = cls.to_json_string([obj.to_dictionary() for obj in list_objs])
            file.write(json_string)
