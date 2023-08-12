#!/usr/bin/python3
"""
Module: review
unittests for derived class Review
"""


import unittest
from models.base_model import BaseModel
from models.review import Review
import os


class Test_Review(unittest.TestCase):
    """
    Review testcases class
    """

    def setUp(self):
        self.review = Review()
        self.review.place_id = "San Francisco"
        self.review.user_id = "Maarten"
        self.review.text = "Its a 5-star rating for me"

    def tearDown(self):
        del self.review
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_instance_creation(self):
        self.assertIsInstance(self.review, BaseModel)

    def test_docstring(self):
        self.assertIsNotNone(Review.__doc__)

    def test_timedelta(self):
        self.review.save()
        self.assertNotEqual(self.review.created_at, self.review.updated_at)

    def test_attributes(self):
        self.assertTrue(hasattr(self.review, 'place_id'))
        self.assertTrue(hasattr(self.review, 'user_id'))
        self.assertTrue(hasattr(self.review, 'text'))
        self.assertTrue(hasattr(self.review, 'created_at'))
        self.assertTrue(hasattr(self.review, 'updated_at'))

    def test_string_representation(self):
        self.assertIsInstance(self.review.__str__(), str)

    def test_to_dictionary(self):
        a_dict = self.review.to_dict()
        self.assertIsInstance(a_dict['place_id'], str)
        self.assertIsInstance(a_dict['user_id'], str)
        self.assertIsInstance(a_dict['text'], str)
        self.assertIsInstance(a_dict['created_at'], str)
        self.assertIsInstance(a_dict['updated_at'], str)
        self.assertEqual(self.review.__class__.__name__, 'Review')


if __name__ == '__main__':
    unittest.main()
