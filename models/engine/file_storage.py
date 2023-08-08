#!/usr/bin/python3
"""This module stores objects
"""

import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


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
    
    def reload(self):
        """deserializes the JSON file to __objects (only if the JSON file exists"""
        with open(FileStorage.__file_path) as f:
            serialized_objects =i json.loads(f)
            for item in serialized_objects.values():
                type = item["__class__"]
                del item["__class__"]

