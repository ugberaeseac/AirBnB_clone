#!/usr/bin/python3
"""Defines unittests for models/engine/file_storage.py.

Unittest classes:
    TestFileStorage_instantiation
    TestFileStorage_methods
"""
import os
import json
import models
import unittest
from datetime import datetime
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestFileStorage_instantiation(unittest.TestCase):
    """Tests for creating instances of the FileStorage class."""

    def test_instantiation_with_no_arguments(self):
        file_storage_instance = FileStorage()
        self.assertEqual(type(file_storage_instance), FileStorage)

    def test_instantiation_with_argument_raises_error(self):
        with self.assertRaises(TypeError):
            FileStorage(None)

    def test_file_path_is_a_private_string_attribute(self):
        self.assertEqual(str, type(FileStorage._FileStorage__file_path))

    def test_objects_is_a_private_dictionary_attribute(self):
        self.assertEqual(dict, type(FileStorage._FileStorage__objects))

    def test_storage_initialized_as_FileStorage_instance(self):
        self.assertEqual(type(models.storage), FileStorage)


class TestFileStorage_methods(unittest.TestCase):
    """Unittests for testing methods of the FileStorage class."""

    @classmethod
    def setUp(self):
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass

    @classmethod
    def clean_up(self):
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("tmp", "file.json")
        except IOError:
            pass
        FileStorage._FileStorage__objects = {}

    def test_all_method_returns_dict(self):
        result = models.storage.all()
        self.assertEqual(dict, type(result))

    def test_all_method_with_argument_raises_error(self):
        with self.assertRaises(TypeError):
            models.storage.all(None)

    def test_new(self):
        bm = BaseModel()
        us = User()
        st = State()
        plc = Place()
        cty = City()
        am = Amenity()
        rev = Review()

        models.storage.new(bm)
        models.storage.new(us)
        models.storage.new(st)
        models.storage.new(plc)
        models.storage.new(cty)
        models.storage.new(am)
        models.storage.new(rev)

        self.verify_instance_added_to_storage(bm, "BaseModel")
        self.verify_instance_added_to_storage(us, "User")
        self.verify_instance_added_to_storage(st, "State")
        self.verify_instance_added_to_storage(plc, "Place")
        self.verify_instance_added_to_storage(cty, "City")
        self.verify_instance_added_to_storage(am, "Amenity")
        self.verify_instance_added_to_storage(rev, "Review")

    def verify_instance_added_to_storage(self, instance, class_name):
        key = f"{class_name}.{instance.id}"
        self.assertIn(key, models.storage.all().keys())

        self.assertIn(instance, models.storage.all().values())


if __name__ == "__main__":
    unittest.main()
