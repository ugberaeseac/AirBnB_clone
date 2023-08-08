#!/usr/bin/python3
"""This module stores objects
"""

import json


class FileStorage:
    """This class serializes instances to a JSON file and
    deserializes JSON file to instances

    Private class attributes:
    __file_path: string - path to the JSON file
    __objects: dictionary - empty but will store all objects by <class name>.id

    """
    __file_path = file.json
    __objects = {}

    def all(self):
        """Public instance method of class FileStorage that returns
        the dictionary __objects"""
        return FileStorage.__objects
