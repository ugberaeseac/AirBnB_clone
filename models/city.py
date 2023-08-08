#!/usr/bin/python3

"""
Module: city
inherits from Parent class BaseModel
"""


from models.base_model import BaseModel


class City(BaseModel):
    """
    Derived class City inherits from BaseModel
    """
    state_id = ""
    name = ""
