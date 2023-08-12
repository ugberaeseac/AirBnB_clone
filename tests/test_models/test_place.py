#!/usr/bin/python3
"""
Module: place
unittests for derived class Place
"""


import unittest
from models.base_model import BaseModel
from models.place import Place
import os


class Test_Place(unittest.TestCase):
    """
    Place testcases class
    """

    def setUp(self):
        self.place = Place()
        self.place.city_id = "Victoria Island"
        self.place.user_id = "Amowie"
        self.place.name = "Ugberaese Charles"
        self.place.description = "Feel the Ocean"
        self.place.number_rooms = 3
        self.place.number_bathrooms = 3
        self.place.max_guest = 5
        self.place.price_by_night = 240
        self.place.latitude = 37.5
        self.place.longitude = 62.8
        self.place.amenity_ids = ["Free WIFI", "Ocean View", "Gym"]

    def tearDown(self):
        del self.place
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_instance_creation(self):
        self.assertIsInstance(self.place, BaseModel)

    def test_docstring(self):
        self.assertIsNotNone(Place.__doc__)

    def test_timedelta(self):
        self.place.save()
        self.assertNotEqual(self.place.created_at, self.place.updated_at)

    def test_attributes(self):
        self.assertTrue(hasattr(self.place, 'city_id'))
        self.assertTrue(hasattr(self.place, 'user_id'))
        self.assertTrue(hasattr(self.place, 'name'))
        self.assertTrue(hasattr(self.place, 'description'))
        self.assertTrue(hasattr(self.place, 'number_rooms'))
        self.assertTrue(hasattr(self.place, 'number_bathrooms'))
        self.assertTrue(hasattr(self.place, 'max_guest'))
        self.assertTrue(hasattr(self.place, 'price_by_night'))
        self.assertTrue(hasattr(self.place, 'latitude'))
        self.assertTrue(hasattr(self.place, 'longitude'))
        self.assertTrue(hasattr(self.place, 'amenity_ids'))
        self.assertTrue(hasattr(self.place, 'created_at'))
        self.assertTrue(hasattr(self.place, 'updated_at'))

    def test_string_representation(self):
        self.assertIsInstance(self.place.__str__(), str)

    def test_to_dictionary(self):
        a_dict = self.place.to_dict()
        self.assertIsInstance(a_dict['city_id'], str)
        self.assertIsInstance(a_dict['user_id'], str)
        self.assertIsInstance(a_dict['name'], str)
        self.assertIsInstance(a_dict['description'], str)
        self.assertIsInstance(a_dict['number_rooms'], int)
        self.assertIsInstance(a_dict['number_bathrooms'], int)
        self.assertIsInstance(a_dict['max_guest'], int)
        self.assertIsInstance(a_dict['price_by_night'], int)
        self.assertIsInstance(a_dict['latitude'], float)
        self.assertIsInstance(a_dict['longitude'], float)
        self.assertIsInstance(a_dict['amenity_ids'], list)
        self.assertIsInstance(a_dict['created_at'], str)
        self.assertIsInstance(a_dict['updated_at'], str)
        self.assertEqual(self.place.__class__.__name__, 'Place')


if __name__ == '__main__':
    unittest.main()
