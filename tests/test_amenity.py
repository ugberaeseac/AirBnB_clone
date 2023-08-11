#!/usr/bin/python3
"""
Module: amenity
unittests for derived class Amenity
"""


import unittest
from models.base_model import BaseModel
from models.amenity import Amenity
import os


class Test_Amenity(unittest.TestCase):
    """
    Amenity testcases class
    """

    def setUp(self):
        self.amenity = Amenity()
        self.amenity.name = "Ocean View"

    def tearDown(self):
        del self.amenity
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_instance_creation(self):
        self.assertIsInstance(self.amenity, BaseModel)

    def test_docstring(self):
        self.assertIsNotNone(Amenity.__doc__)

    def test_timedelta(self):
        self.amenity.save()
        self.assertNotEqual(self.amenity.created_at, self.amenity.updated_at)

    def test_attributes(self):
        self.assertTrue(hasattr(self.amenity, 'name'))
        self.assertTrue(hasattr(self.amenity, 'id'))
        self.assertTrue(hasattr(self.amenity, 'created_at'))
        self.assertTrue(hasattr(self.amenity, 'updated_at'))

    def test_sting_representation(self):
        self.assertIsInstance(self.__str__(), str)

    def test_to_dictionary(self):
        a_dict = self.amenity.to_dict()
        self.assertIsInstance(a_dict['created_at'], str)
        self.assertIsInstance(a_dict['updated_at'], str)
        self.assertEqual(self.amenity.__class__.__name__, 'Amenity')


if __name__ == '__main__':
    unittest.main()
