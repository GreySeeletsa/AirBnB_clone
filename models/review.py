#!/usr/bin/python3
"""This contains a review model"""
from models.base_model import BaseModel


class Review(BaseModel):
    """Implementing a review model"""
    place_id = ""
    user_id = ""
    text = ""
