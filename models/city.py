#!/usr/bin/python3
"""City class"""
from models.base_model import BaseModel


class City(BaseModel):
    """Representing a city.

    Attributes:
        state_id (str): The state id.
        name (str): Name of city.
    """

    state_id = ""
    name = ""
