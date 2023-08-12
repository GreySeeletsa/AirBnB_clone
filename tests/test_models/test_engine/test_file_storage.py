#!/usr/bin/python3
"""Tests the suite for the FileStorage in a models/file_storage.py"""
import os.path
import unittest

import models
from models import base_model
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.amenity import Amenity
from models.city import City
from models.review import Review
from models.place import Place


class TestFileStorageInit(unittest.TestCase):
    """This contains the test cases for FileStorage initialization"""

    def test_file_path_is_a_private_class_attr(self):
        """Check if the file_path is the private class attribute"""
        self.assertFalse(hasattr(FileStorage(), "__file_path"))

    def test_objects_is_a_private_class_attr(self):
        """Check if the objects is the private class attribute"""
        self.assertFalse(hasattr(FileStorage(), "__objects"))

    def test_init_without_arg(self):
        """Test the initialization without the args"""
        self.assertEqual(type(FileStorage()), FileStorage)

    def test_init_with_arg(self):
        """Test the initialization with the args"""
        with self.assertRaises(TypeError):
            FileStorage(None)

    def test_storage_initialization(self):
        """Test the storage created in the __init__.py"""
        self.assertEqual(type(models.storage), FileStorage)


class TestStorageMethods(unittest.TestCase):
    """Contain the test cases for the methods presented in the FileStorage"""

    @classmethod
    def setUp(self):
        """The code to execute prior to testing"""
        try:
            os.rename("file.json", "tmp.json")
        except IOError:
            pass

    @classmethod
    def tearDown(self):
        """The code to execute after the tests is being executed"""
        # Remove the file.json if it does exists
        try:
            os.remove("file.json")
        except IOError:
            pass

        # Rename the tmp.json from the setUp() to file.json
        try:
            os.rename("tmp.json", "file.json")
        except IOError:
            pass

        FileStorage._FileStorage__objects = {}

    def test_all_method(self):
        """Test all() the method of FileStorage class"""
        self.assertTrue(type(models.storage.all()) is dict)

        # What if an argument is being passed? Well! TypeError, do your job please!
        with self.assertRaises(TypeError):
            models.storage.all(None)

    def test_new_method(self):
        """Test a new() method of a FileStorage class"""
        dummy_bm = BaseModel()
        dummy_user = User()
        dummy_state = State()
        dummy_city = City()
        dummy_place = Place()
        dummy_review = Review()
        dummy_amenity = Amenity()

        # Checks whether the objects created above are stored already
        self.assertIn("BaseModel." + dummy_bm.id,
                      models.storage.all().keys())
        self.assertIn(dummy_bm, models.storage.all().values())
        self.assertIn("User." + dummy_user.id, models.storage.all().keys())
        self.assertIn(dummy_user, models.storage.all().values())
        self.assertIn("State." + dummy_state.id, models.storage.all().keys())
        self.assertIn(dummy_state, models.storage.all().values())
        self.assertIn("Place." + dummy_place.id, models.storage.all().keys())
        self.assertIn(dummy_place, models.storage.all().values())
        self.assertIn("City." + dummy_city.id, models.storage.all().keys())
        self.assertIn(dummy_city, models.storage.all().values())
        self.assertIn("Amenity." + dummy_amenity.id,
                      models.storage.all().keys())
        self.assertIn(dummy_amenity, models.storage.all().values())
        self.assertIn("Review." + dummy_review.id,
                      models.storage.all().keys())
        self.assertIn(dummy_review, models.storage.all().values())

        # If more than one argument is passed to this?
        # TypeError, we definetely need you in here!
        with self.assertRaises(TypeError):
            models.storage.new(BaseModel(), 1)

        # If none is passed? you need to learn the lesson...
        # AttributeError, can you join us?
        with self.assertRaises(AttributeError):
            models.storage.new(None)

    def test_save_method(self):
        """Is time to deal with the reload() method in the FileStorage class"""
        dummy_bm = BaseModel()
        dummy_user = User()
        dummy_state = State()
        dummy_city = City()
        dummy_place = Place()
        dummy_review = Review()
        dummy_amenity = Amenity()

        models.storage.save()

        with open("file.json", "r") as f:
            save_text = f.read()
            self.assertIn("BaseModel." + dummy_bm.id, save_text)
            self.assertIn("User." + dummy_user.id, save_text)
            self.assertIn("State." + dummy_state.id, save_text)
            self.assertIn("Place." + dummy_place.id, save_text)
            self.assertIn("City." + dummy_city.id, save_text)
            self.assertIn("Amenity." + dummy_amenity.id, save_text)
            self.assertIn("Review." + dummy_review.id, save_text)

        # What will happen if the argument has passed? TypeError this has been indeed my agent!
        with self.assertRaises(TypeError):
            models.storage.save(None)

    def test_reload_method(self):
        """Test a reload method... this quite a tricky!"""
        dummy_bm = BaseModel()
        dummy_user = User()
        dummy_state = State()
        dummy_city = City()
        dummy_place = Place()
        dummy_review = Review()
        dummy_amenity = Amenity()

        models.storage.save()
        models.storage.reload()
        objects = FileStorage._FileStorage__objects

        self.assertIn("BaseModel." + dummy_bm.id, objects)
        self.assertIn("User." + dummy_user.id, objects)
        self.assertIn("State." + dummy_state.id, objects)
        self.assertIn("Place." + dummy_place.id, objects)
        self.assertIn("City." + dummy_city.id, objects)
        self.assertIn("Amenity." + dummy_amenity.id, objects)
        self.assertIn("Review." + dummy_review.id, objects)

        # What will happen if the argument is passed? TypeError raised
        with self.assertRaises(TypeError):
            models.storage.reload(None)


if __name__ == "__main__":
    unittest.main()
