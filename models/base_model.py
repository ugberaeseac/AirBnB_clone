#!/usr/bin/python3

"""
Module: base_python
contains parent class BaseModel
contains public instance attributes and methods
"""


import models
from datetime import datetime
import uuid


class BaseModel:
    """
    Parent class for the AirBnB clone project
    """
    def __init__(self, *args, **kwargs):
        """
        Initialize public instance attributesi


        """
        if kwargs:
            for key, value in kwargs.items():
                if key == "__class__":
                    pass
                elif key == "created_at":
                    self.created_at = datetime.strptime(kwargs["created_at"],
                                                        "%Y-%m-%dT%H:%M:%S.%f")
                elif key == "updated_at":
                    self.updated_at = datetime.strptime(kwargs["updated_at"],
                                                        "%Y-%m-%dT%H:%M:%S.%f")
                else:
                    setattr(self, key, value)

        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

            models.storage.new(self)

    def __str__(self):
        """
        Return string representation of the Base class
        """
        return ("[{}] ({}) {}".
                format(self.__class__.__name__, self.id, self.__dict__))

    def save(self):
        """
        Updates the public instance attribute updated_at
        with the current datetime
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        Returns a dictionary containing all keys/values
        of __dict__ of the instance
        """
        a_dict = {}

        for key, value in self.__dict__.items():
            if isinstance(value, datetime):
                a_dict[key] = value.isoformat()
            else:
                a_dict[key] = value
        a_dict["__class__"] = self.__class__.__name__

        return (a_dict)
