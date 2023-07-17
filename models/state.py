#!/usr/bin/python3
"""State class."""
from models.base_model import BaseModel


class State(BaseModel):
    """Representing a state.

    Attributes:
        name (str): name of state.
    """

    name = ""
