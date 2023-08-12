#!/usr/bin/python3
"""
Module: state
unittests for derived class State
"""


import unittest
from models.base_model import BaseModel
from models.state import State
import os


class Test_State(unittest.TestCase):
    """
    State testcases class
    """

    def setUp(self):
        self.state = State()
        self.state.name = "Lagos"

    def tearDown(self):
        del self.state
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_instance_creation(self):
        self.assertIsInstance(self.state, BaseModel)

    def test_docstring(self):
        self.assertIsNotNone(State.__doc__)

    def test_timedelta(self):
        self.state.save()
        self.assertNotEqual(self.state.created_at, self.state.updated_at)

    def test_attributes(self):
        self.assertTrue(hasattr(self.state, 'name'))
        self.assertTrue(hasattr(self.state, 'id'))
        self.assertTrue(hasattr(self.state, 'created_at'))
        self.assertTrue(hasattr(self.state, 'updated_at'))

    def test_sting_representation(self):
        self.assertIsInstance(self.state.__str__(), str)

    def test_to_dictionary(self):
        a_dict = self.state.to_dict()
        self.assertIsInstance(a_dict['created_at'], str)
        self.assertIsInstance(a_dict['updated_at'], str)
        self.assertEqual(self.state.__class__.__name__, 'State')


if __name__ == '__main__':
    unittest.main()
