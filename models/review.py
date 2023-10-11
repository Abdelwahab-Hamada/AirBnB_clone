#!/usr/bin/python3
"""Review"""
from models.base_model import BaseModel


class Review(BaseModel):
    """Review props"""
    place_id = ""
    user_id = ""
    text = ""
