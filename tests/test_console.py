#!/usr/bin/python3
"""Defines unittests for console.py.
"""
import uuid
import console
import os
import sys
import unittest
from models.user import User
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
            HBNBCommand.emptyline,
            HBNBCommand.do_create,
            HBNBCommand.do_show,
            HBNBCommand.do_destroy,
            HBNBCommand.do_all,
            HBNBCommand.do_update,
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

    def test_create_with_invalid_class_name(self):
        """ Test create with invalid class name"""
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("create MyModel")
            output = f.getvalue().strip()
            self.assertEqual(output, "** class doesn't exist **")

    def test_show_with_valid_class_and_id(self):
        """ Test show with valid class and id"""
        test_inst = User()
        test_inst.save()
        cmd = f"show User {test_inst.id}"
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd(cmd)
            output = f.getvalue().strip()
            self.assertIn(f"[User] ({test_inst.id})", output)
            self.assertIn("created_at", output)
            self.assertIn("updated_at", output)
            self.assertIn("id", output)
            self.assertNotIn("__class__", output)
            self.assertFalse(output.startswith('["'))
            self.assertFalse(output.endswith('"]'))

    def test_show_without_class_name(self):
        """ Test show without class name"""
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("show")
            output = f.getvalue().strip()
            self.assertEqual(output, "** class name missing **")

    def test_show_with_invalid_class_name(self):
        """ Test show with invalid class name"""
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("show MyModel")
            output = f.getvalue().strip()
            self.assertEqual(output, "** class doesn't exist **")

    def test_show_without_instance_id(self):
        """ Test show without instance id"""
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("show User")
            output = f.getvalue().strip()
            self.assertEqual(output, "** instance id missing **")

    def test_show_with_invalid_instance_id(self):
        """ Test show with invalid instance id"""
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("show User 121212")
            output = f.getvalue().strip()
            self.assertEqual(output, "** no instance found **")

    def test_destroy_with_valid_class_and_id(self):
        """ Test destroy with valid class and id"""
        test_inst = User()
        test_inst.save()
        cmd = f"destroy User {test_inst.id}"
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd(cmd)
            HBNBCommand().onecmd(f"show User {test_inst.id}")
            output = f.getvalue().strip()
            self.assertEqual(output, "** no instance found **")

    def test_destroy_with_missing_class_name(self):
        """ Test destroy with missing class name"""
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("destroy")
            output = f.getvalue().strip()
            self.assertEqual(output, "** class name missing **")

    def test_destroy_with_nonexistent_instance(self):
        """ Test destroy with nonexistent instance"""
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("destroy BaseModel 121212")
            output = f.getvalue().strip()
            self.assertEqual(output, "** no instance found **")


if __name__ == "__main__":
    unittest.main()
