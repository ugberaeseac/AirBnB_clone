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

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        obj_class_name = obj.__class__.__name__
        FileStorage.__objects["{}.{}".format(obj_class_name, obj.id)] = obj

    def save(self):
        """serializes __objects to the JSON file"""
        objects_dict = FileStorage.__objects
        serialized_objects = {}

        for obj_key in objects_dict:
            obj_instance = objects_dict[obj_key]
            serialized_objects[obj_key] = obj_instance.to_dict()

        with open(FileStorage.__objects, 'w') as f:
            json.dump(serialized_objects, f)

        
