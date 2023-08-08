#!/usr/bin/python3

"""
Module: user
inherits from Parent class BaseModel
"""


from models.base_model import BaseModel


class User(BaseModel):
    """
    Derived class User inherits from BaseModel
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
