#!/usr/bin/python3
"""
This contains a FileStorage class model


"""
import json

from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review


class FileStorage:
    """
    Serialize instances to the JSON file and
    Deserialize JSON file to the instances
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        Returning a dictionary __objects
        """
        return self.__objects

    def new(self, obj):
        """
        Set in __objects `obj` with the key <obj class name>.id
        """
        self.__objects["{}.{}".format(obj.__class__.__name__, obj.id)] = obj

    def save(self):
        """
        Serializing __objects to a JSON file
        """
        with open(self.__file_path, mode="w") as f:
            dict_storage = {}
            for k, v in self.__objects.items():
                dict_storage[k] = v.to_dict()
            json.dump(dict_storage, f)

    def reload(self):
        """
        Deserialize a JSON file to the __objects
        -> only if it does exist!
        """
        try:
            with open(self.__file_path, encoding="utf-8") as f:
                for obj in json.load(f).values():
                    self.new(eval(obj["__class__"])(**obj))
        except FileNotFoundError:
            return
