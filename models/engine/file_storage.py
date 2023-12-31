#!/usr/bin/python3
"""
Module: file_storage
This module serializes python objects into JSON objects
and deserialize them to python objects
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
    """
    This class serializes instances to a JSON file and
    deserializes JSON file to instances

    Private class attributes:
    __file_path: string - path to the JSON file
    __objects: dictionary - empty but will store all objects by <class name>.id

    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        Public instance method of class FileStorage that returns
        the dictionary __objects
        """
        return FileStorage.__objects

    def new(self, obj):
        """
        sets in __objects the obj with key <obj class name>.id
        """
        obj_class_name = obj.__class__.__name__
        FileStorage.__objects["{}.{}".format(obj_class_name, obj.id)] = obj

    def save(self):
        """
        serializes __objects to the JSON file
        """
        object_dict = FileStorage.__objects
        en_obj = {key: value.to_dict() for key, value in object_dict.items()}
        with open(FileStorage.__file_path, 'w', encoding='utf-8') as f:
            json.dump(en_obj, f)

    def reload(self):
        """
        deserializes the JSON file to __objects (
        only if the JSON file exists)
        """
        try:
            with open(FileStorage.__file_path, 'r', encoding='utf-8') as f:
                encoded_obj = json.load(f)

                class_names = {
                        "BaseModel": BaseModel,
                        "User": User,
                        "State": State,
                        "Place": Place,
                        "Amenity": Amenity,
                        "City": City,
                        "Review": Review
                }

                for item in encoded_obj.values():
                    obj_type = item.get("__class__")
                    if obj_type:
                        del item["__class__"]
                        class_type = class_names.get(obj_type)
                        if class_type:
                            self.new(class_type(**item))
                        else:
                            print(f"Unrecognized class type: {obj_type}")
        except FileNotFoundError:
            pass
