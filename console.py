#!/usr/bin/python3

import cmd
import models
import shlex
from datetime import datetime
from models.base_model import BaseModel
from models import storage
from models.user import User
from models.state import State
from models.review import Review
from models.city import City
from models.place import Place
from models.amenity import Amenity

class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb) '
    __classes = [
            "Amenity",
            "BaseModel",
            "City",
            "Place",
            "Review",
            "State",
            "User"
]

    def do_create(self, args):
        """create a new instance of BaseModel,save it & prints id Usage: create <class name>
        """

        args = args.split()
        if len(args) = 0:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.__classes:
            print("** class doesn't exit **")
        else:
            new_create = eval(args[0] + '()')
            models.storage.save()
            print(new_create.id)

    def check_class_name(self, name=""):
        """check if stdin user is typed class name & id."""
        if len(name) == 0:
            print("** class name missing **")
            return False
        else:
            return True

    def found_class_name(self, name=""):
        """find name class."""
        if self.check_class_name(name):
            args = shlex.split(name)
            if args[0] in HBNBCommand.__classes:
                if self.check_class_id(name):
                    key = args[0] + '.' + args[1]
                    return key
                else:
                    print("** class doesn't exit **")
                    return None
    def check_class_id(self, name=""):
        """check class id."""
        if len(name.split(' ')) == 1:
            print("** instance id missing **")
            return False
        else:
            return True

    def do_show(self, args):
        """print strings representation of a specific instance Usage: show <class name> <id>
        """

        strings = args.split()
        if len(strings) == 0:
            print("** class name missing **")
        elif strings[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(strings) == 1:
            print("** instance id missing **")
        else:
            obj = models.storage.all()
            key_value = strings[0] + '.' + strings[1]
            if key_value in obj:
                print(obj[key_value])
            else:
                print("** no instance found **")

     def do_destroy(self, args):
        """Delete an instance
        Usage: destroy <class name> <id>
        """
        args = args.split()
        objects = models.storage.all()

        if len(args) == 0:
            print('** class name missing **')
        elif args[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print('** instance id missing **')
        else:
            key_find = args[0] + '.' + args[1]
            if key_find in objects.keys():
                objects.pop(key_find, None)
                models.storage.save()
            else:
                print('** no instance found **')

    def do_all(self, args):
        """Print a string representation of all instances
        Usage: all <class name>
        """
        args = args.split()
        objects = models.storage.all()
        new_list = []

        if len(args) == 0:
            for obj in objects.values():
                new_list.append(obj.__str__())
            print(new_list)
        elif args[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            for obj in objects.values():
                if obj.__class__.__name__ == args[0]:
                    new_list.append(obj.__str__())
            print(new_list)

     def do_update(self, args):
        """update an instance
        Usage update <class name> <id> <attribute name> "<attribute value>"
        """
        objects = models.storage.all()
        args = args.split()

        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif len(args) == 2:
            print("** attribute name missing **")
        elif len(args) == 3:
            print("** value missing **")
        else:
            key_find = args[0] + '.' + args[1]
            obj = objects.get(key_find, None)

            if not obj:
                print("** no instance found **")
                return

            setattr(obj, args[2], args[3].lstrip('"').rstrip('"'))
            models.storage.save()

    def do_quit(self, args):
        """<Quit> command to exit the program"""
        return True

    def do_EOF(self, args):
        """Handles end of the file"""
        return True

    def emptyline(self):
        """don't execute anything when user press enter an empty line."""

        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
