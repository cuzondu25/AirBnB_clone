#!/usr/bin/python3
"""Amenity class"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """ Amenity inheritting from BaseModel
    Attributes:
        name (str): The name of the amenity.
    """

    name = ""
