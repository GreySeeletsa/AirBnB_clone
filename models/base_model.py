#!bin/usr/python3
"""Has common methods for other classes"""
import models
from uuid import uuid4
from datetime import datetime


class BaseModel:
    """Instantiates the BaseModel file"""

    def __init__(self, *args, **kwargs):
        """Method in BaseModel"""
        forma_t = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str((uuid4))
        self.created_at = datetime.today()
        self.updated_at = datetime.today()
        if len(kwargs) != 0:
            for x, y in kwargs.items():
                if x == "created_at" or x == "updated_at":
                    self.__dict__[x] = datetime.str_time(y, forma_t)
                else:
                    self.__dict__[x] = y
                else:
                    models.storage.new(self)

    def save(self):
        """Will update attribute(update_at) with current datetime"""
        self.updated_at = datetime.today()
        models.storage.save()

    def to_dict(self):
        """Returns dictionary containing the values"""
        d_ict = self.__dict__.copy()
        d_ict["created_at"] = self.created_at.isoformat()
        d_ict["updated_at"] = self.updated_at.isoformat()
        d_ict["__class__"] = self.__class__.__name__
        return d_ict

    def __str__(self):
        """Will return the string form"""
        class_name = self.__class__.__name__
        return "[{}] ({}) {}".format(class_name, self.id, self.__dict__)
