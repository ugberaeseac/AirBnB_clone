#!/usr/bin/python3
"""
Module: user
unittests for derived class User
"""


import unittest
from models.base_model import BaseModel
from models.user import User
import os


class Test_User(unittest.TestCase):
    """
    User testcases class
    """

    def setUp(self):
        self.user = User()
        self.user.email = "ugberaeseac@gmail.com"
        self.user.password = "ALX_SE AirBnB Clone"
        self.user.first_name = "Amowie"
        self.user.last_name = "Ugberaese"

    def tearDown(self):
        del self.user
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_instance_creation(self):
        self.assertIsInstance(self.user, BaseModel)

    def test_docstring(self):
        self.assertIsNotNone(User.__doc__)

    def test_timedelta(self):
        self.user.save()
        self.assertNotEqual(self.user.created_at, self.user.updated_at)

    def test_attributes(self):
        self.assertTrue(hasattr(self.user, 'id'))
        self.assertTrue(hasattr(self.user, 'email'))
        self.assertTrue(hasattr(self.user, 'password'))
        self.assertTrue(hasattr(self.user, 'first_name'))
        self.assertTrue(hasattr(self.user, 'last_name'))
        self.assertTrue(hasattr(self.user, 'created_at'))
        self.assertTrue(hasattr(self.user, 'updated_at'))

    def test_string_representation(self):
        self.assertIsInstance(self.user.__str__(), str)

    def test_to_dictionary(self):
        a_dict = self.user.to_dict()
        self.assertIsInstance(a_dict['email'], str)
        self.assertIsInstance(a_dict['password'], str)
        self.assertIsInstance(a_dict['first_name'], str)
        self.assertIsInstance(a_dict['last_name'], str)
        self.assertIsInstance(a_dict['created_at'], str)
        self.assertIsInstance(a_dict['updated_at'], str)
        self.assertEqual(self.user.__class__.__name__, 'User')


if __name__ == '__main__':
    unittest.main()
