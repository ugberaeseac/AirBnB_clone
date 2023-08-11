#!/usr/bin/python3
"""
Module: test_basemodel
unittests for BaseModel class
"""


import unittest
from models.base_model import BaseModel
import os


class Test_BaseModel(unittest.TestCase):
    """
    BaseMode; testcases class
    """

    def setUp(self):
        self.base = BaseModel()
        self.base.name = "Charles"
        self.base.my_number = "12"

    def tearDown(self):
        del self.base
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass
    
    def test_instance_creation(self):
        self.assertIsInstance(self.base, BaseModel)

    def test_docstring(self):
        self.assertIsNotNone(BaseModel.__doc__)
        self.assertIsNotNone(BaseModel.__init__.__doc__)
        self.assertIsNotNone(BaseModel.__str__.__doc__)
        self.assertIsNotNone(BaseModel.save.__doc__)
        self.assertIsNotNone(BaseModel.to_dict.__doc__)

    def test_timedelta(self):
        self.base.save()
        self.assertNotEqual(self.base.created_at, self.base.updated_at)

    def test_attributes(self):
        self.assertTrue(hasattr(self.base, 'id'))
        self.assertTrue(hasattr(self.base, 'created_at'))
        self.assertTrue(hasattr(self.base, 'updated_at'))

    def test_classattributes(self):
        self.assertTrue(hasattr(BaseModel, '__init__'))
        self.assertTrue(hasattr(BaseModel, '__str__'))
        self.assertTrue(hasattr(BaseModel, 'save'))
        self.assertTrue(hasattr(BaseModel, 'to_dict'))

    def test_sting_representation(self):
        self.assertIsInstance(self.__str__(), str)

    def test_to_dictionary(self):
        a_dict = self.base.to_dict()
        self.assertIsInstance(a_dict['created_at'], str)
        self.assertIsInstance(a_dict['updated_at'], str)
        self.assertEqual(self.base.__class__.__name__, 'BaseModel')



if __name__ == '__main__':
    unittest.main()
