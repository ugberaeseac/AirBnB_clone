#!/usr/bin/python3
"""Defines unittests for console.py.
"""
import uuid
import console
import os
import sys
import unittest
from models import storage
from models.engine.file_storage import FileStorage
from console import HBNBCommand
from io import StringIO
from unittest.mock import patch


class TestConsole(unittest.TestCase):
    def setUp(self):
        try:
            os.remove("file.json")
        except IOError:
            pass
        FileStorage._FileStorage__objects = {}

    def tearDown(self):
        try:
            os.remove("file.json")
        except IOError:
            pass

    def test_module_doc(self):
        self.assertIsNotNone(console.__doc__)

    def test_class_doc(self):
        self.assertIsNotNone(HBNBCommand.__doc__)

    def test_method_docs(self):
        """Test all methods in ``console`` for docs"""
        methods = [
            HBNBCommand.do_EOF,
            HBNBCommand.do_quit,
            HBNBCommand.help_quit,
            HBNBCommand.emptyline,
            HBNBCommand.is_valid,
            HBNBCommand.value_type,
            HBNBCommand.do_create,
            HBNBCommand.help_create,
            HBNBCommand.do_show,
            HBNBCommand.help_show,
            HBNBCommand.do_destroy,
            HBNBCommand.help_destroy,
            HBNBCommand.do_all,
            HBNBCommand.help_all,
            HBNBCommand.count,
            HBNBCommand.do_update,
            HBNBCommand.default,
        ]
        for meth in methods:
            self.assertIsNotNone(meth.__doc__)

    def test_quit(self):
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("quit")
            output = f.getvalue().strip()
            self.assertEqual(output, "")

    def test_EOF(self):
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("EOF")
            output = f.getvalue().strip()
            self.assertEqual(output, "")

    def test_empty_line(self):
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("")
            output = f.getvalue().strip()
            self.assertEqual(output, "")

    def test_help_create(self):
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("help create")
            output = f.getvalue().strip()
            self.assertIsNotNone(output)

    def test_help_show(self):
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("help show")
            output = f.getvalue().strip()
            self.assertIsNotNone(output)

    def test_help_destroy(self):
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("help destroy")
            output = f.getvalue().strip()
            self.assertIsNotNone(output)

    def test_help_all(self):
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("help all")
            output = f.getvalue().strip()
            self.assertIsNotNone(output)

    def test_help_update(self):
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("help update")
            output = f.getvalue().strip()
            self.assertIsNotNone(output)

    def test_create_with_valid_class_name_BaseModel(self):
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("create BaseModel")
            output = f.getvalue().strip()
            try:
                uuid.UUID(output)
            except ValueError:
                self.fail("Output is not a valid UUID")

    def test_create_with_valid_class_name_User(self):
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("create User")
            output = f.getvalue().strip()
            try:
                uuid.UUID(output)
            except ValueError:
                self.fail("Output is not a valid UUID")

    def test_create_with_valid_class_name_Place(self):
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("create Place")
            output = f.getvalue().strip()
            try:
                uuid.UUID(output)
            except ValueError:
                self.fail("Output is not a valid UUID")

    def test_create_with_valid_class_name_State(self):
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("create State")
            output = f.getvalue().strip()
            try:
                uuid.UUID(output)
            except ValueError:
                self.fail("Output is not a valid UUID")

    def test_create_with_valid_class_name_City(self):
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("create City")
            output = f.getvalue().strip()
            try:
                uuid.UUID(output)
            except ValueError:
                self.fail("Output is not a valid UUID")

    def test_create_with_valid_class_name_Amenity(self):
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("create Amenity")
            output = f.getvalue().strip()
            try:
                uuid.UUID(output)
            except ValueError:
                self.fail("Output is not a valid UUID")

    def test_create_with_valid_class_name_Review(self):
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("create Review")
            output = f.getvalue().strip()
            try:
                uuid.UUID(output)
            except ValueError:
                self.fail("Output is not a valid UUID")

    def test_create_without_class_name(self):
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("create")
            output = f.getvalue().strip()
            self.assertEqual(output, "** class name missing **")

if __name__ == "__main__":
    unittest.main()
