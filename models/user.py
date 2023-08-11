#!/usr/bin/python3
"""Implementing a user's model"""
from models.base_model import BaseModel


class User(BaseModel):
    """
    Inheriting from a BaseModel class and then add the user's functionalities
    Args:
        email (str): Email of a user
        password (str): Password of a user
        first_name (str): First name of a user
        last_name (str): Last name of a user
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
