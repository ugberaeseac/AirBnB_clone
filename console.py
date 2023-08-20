#!/usr/bin/python3
"""
Module: console
This is a module  that contains the
entry point of the command interpreter
"""
import cmd
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review
from models import storage
import shlex


class HBNBCommand(cmd.Cmd):
    """
    Command Interpreter class
    """

    prompt = "(hbnb) "

    class_names = {

            "BaseModel": BaseModel,
            "User": User,
            "State": State,
            "City": City,
            "Place": Place,
            "Amenity": Amenity,
            "Review": Review
    }

    def emptyline(self):
        """
        Do nothing upon receiving an empty line.
        """
        pass

    def do_quit(self, args):
        """
        Quit command to exit the program.
        """
        return True

    def do_EOF(self, args):
        """
        Exits the program and prints a new line before exiting
        """
        print()
        return True

    def do_create(self, args):
        """
        Creates a new instance of BaseModel, saves it (to the JSON file)
        and prints the id
        """
        if args == "":
            print("** class name missing **")
            return

        class_name = args
        if class_name in self.class_names:
            new_obj = self.class_names[class_name]()
            new_obj.save()
            print(new_obj.id)
        else:
            print("** class doesn't exist **")

    def do_show(self, args):
        """
        Prints the string representation of an instance based
        on the class name and id
        """
        if args == "":
            print("** class name missing **")
            return

        cmd_args = args.split()
        class_name = cmd_args[0]

        if class_name not in self.class_names:
            print("** class doesn't exist **")
            return

        if len(cmd_args) < 2:
            print("** instance id missing **")
            return

        obj_id = cmd_args[1]
        unique_key = "{}.{}".format(class_name, obj_id)

        obj = storage.all().get(unique_key)

        if obj is None:
            print("** no instance found **")
        else:
            print(obj)

    def do_destroy(self, args):
        """
        Deletes an instance based on the class name and id
        (save the change into the JSON file)
        """
        if args == "":
            print("** class name missing **")
            return

        cmd_args = args.split()

        if len(cmd_args) == 1:
            print("** instance id missing **")
            return

        class_name = cmd_args[0]

        if class_name not in self.class_names:
            print("** class doesn't exist **")
            return

        obj_id = cmd_args[1]
        unique_key = "{}.{}".format(class_name, obj_id)
        obj = storage.all().get(unique_key)

        if obj is None:
            print("** no instance found **")
        else:
            del storage.all()[unique_key]
            storage.save()

    def do_all(self, args):
        """
        Prints all string representation of all instances based
        or not on the class name
        """

        cmd_args = args.split()

        if len(cmd_args) == 0:
            obj_list = []
            for obj in storage.all().values():
                obj_list.append(str(obj))
            print(obj_list)
            return

        class_name = cmd_args[0]

        if class_name not in self.class_names:
            print("** class doesn't exist **")
            return

        obj_list = []
        for key, obj in storage.all().items():
            if key.startswith(class_name):
                obj_list.append(str(obj))
        print(obj_list)


    def do_update(self, args):
        """
        Updates an instance based on the class name and id by adding or
        updating attribute (save the change into the JSON file)
        """
        if args == "":
            print("** class name missing **")
            return
        cmd_args = shlex.split(args)
        
        class_name = cmd_args[0]
        obj_id = cmd_args[1]
        unique_key = "{}.{}".format(class_name, obj_id)

        if class_name  not in self.class_names:
            print("** class doesn't exist **")
        elif len(cmd_args) == 1:
            print("** instance id missing **")
        elif unique_key not in storage.all():
            print ("** no instance found **")
        elif len(cmd_args) == 2:
            print("** attribute name missing **")
        elif len(cmd_args) == 3:
            print("** value missing **")
        else:
            obj = storage.all().get(unique_key)

            attr_name = cmd_args[2]
            attr_value = cmd_args[3]
            if hasattr(obj, attr_name):
                try:
                    if attr_value.isdigit():
                        attr_value = int(attr_value)
                    elif attr_value.replace('.', '', 1).isdigit():
                        attr_value = float(attr_value)
                except AttributeError:
                    pass
                setattr(obj, attr_name, attr_value)
            else:
                try:
                    if attr_value.isdigit():
                        attr_value = int(attr_value)
                    elif attr_value.replace('.', '', 1).isdigit():
                        attr_value = float(attr_value)
                except AttributeError:
                    pass
                setattr(obj, attr_name, attr_value)
            storage.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
