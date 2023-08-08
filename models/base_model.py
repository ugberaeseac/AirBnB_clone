#!/usr/bin/python3

"""
Module: base_python
contains parent class BaseModel
contains public instance attributes and methods
"""


from datetime import datetime
import uuid


class BaseModel:
    """
    Parent class for the AirBnB clone project
    """
    def __init__(self):
        """
        Initialize public instance attributes
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

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

    def to_dict(self):
        """
        Returns a dictionary containing all keys/values
        of __dict__ of the instance
        """
        a_dict = {}
        a_dict = self.__dict__
        a_dict["__class___"] = self.__class__.__name_

        for key, value in a_dict.items():
            if isinstance(value, datetime):
                a_dict["key"] = value.isoformat()
            else:
                a_dict["key"] = value

        return (a_dict)     _
