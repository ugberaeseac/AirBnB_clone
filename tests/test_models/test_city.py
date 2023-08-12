#!/usr/bin/python3
"""
Module: city
unittests for derived class City
"""


import unittest
from models.base_model import BaseModel
from models.city import City
import os


class Test_City(unittest.TestCase):
    """
    City testcases class
    """

    def setUp(self):
        self.city = City()
        self.city.state_id = "LAG"
        self.city.name = "Victoria Island"

    def tearDown(self):
        del self.city
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_instance_creation(self):
        self.assertIsInstance(self.city, BaseModel)

    def test_docstring(self):
        self.assertIsNotNone(City.__doc__)

    def test_timedelta(self):
        self.city.save()
        self.assertNotEqual(self.city.created_at, self.city.updated_at)

    def test_attributes(self):
        self.assertTrue(hasattr(self.city, 'state_id'))
        self.assertTrue(hasattr(self.city, 'name'))
        self.assertTrue(hasattr(self.city, 'created_at'))
        self.assertTrue(hasattr(self.city, 'updated_at'))

    def test_string_representation(self):
        self.assertIsInstance(self.city.__str__(), str)

    def test_to_dictionary(self):
        a_dict = self.city.to_dict()
        self.assertIsInstance(a_dict['state_id'], str)
        self.assertIsInstance(a_dict['name'], str)
        self.assertIsInstance(a_dict['created_at'], str)
        self.assertIsInstance(a_dict['updated_at'], str)
        self.assertEqual(self.city.__class__.__name__, 'City')


if __name__ == '__main__':
    unittest.main()
