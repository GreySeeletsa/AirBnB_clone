#!/usr/bin/python3
"""Instantiate city class"""
from models.base_model import BaseModel


class City(BaseModel):
    """City class with state_id and name attributes"""

    state_id = ""
    name = ""
