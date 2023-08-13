#!/usr/bin/python3
"""city"""
from models.base_model import BaseModel


class City(BaseModel):
    """class City
           attribute:
               state_id: state id
               name: name of state
    """

    name = ""
    state_id = ""
