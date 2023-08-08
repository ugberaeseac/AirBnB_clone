#!/usr/bin/python3

"""
Module: review
inherits from Parent class BaseModel
"""


from models.base_model import BaseModel


class Review(BaseModel):
    """
    Derived class Review inherits from BaseModel
    """
    place_id = ""
    user_id = ""
    text = ""
