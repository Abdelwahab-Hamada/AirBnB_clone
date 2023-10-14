#!/usr/bin/python3
"""Base Model"""
from uuid import uuid4
from datetime import datetime
import models


class BaseModel:
    """BaseModel props"""
    def __init__(self, *args, **kwargs):
        """Intialize"""
        self.id = str(uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()
        if kwargs:
            datetime_form = "%Y-%m-%dT%H:%M:%S.%f"
            for k, v in kwargs.items():  # k:key, v:value
                if k == "created_at" or k == "updated_at":
                    self.__dict__[k] = datetime.strptime(v, datetime_form)
                else:
                    self.__dict__[k] = v
        else:
            models.storage.new(self)

    def save(self):
        """Save method"""
        self.updated_at = datetime.today()
        models.storage.save()

    def __str__(self):
        """Dunder method str"""
        class_name = self.__class__.__name__
        return "[{}] ({}) {}".format(class_name, self.id, self.__dict__)

    def to_dict(self):
        """To dictinary method"""
        dic = self.__dict__.copy()
        dic["created_at"] = self.created_at.isoformat()
        dic["updated_at"] = self.updated_at.isoformat()
        dic["__class__"] = self.__class__.__name__
        return dic
