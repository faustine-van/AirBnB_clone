#!/usr/bin/python3
"""the entry point of the command interpreter"""
import cmd
import sys
import re
from shlex import split
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.place import Place
from models.state import State
from models.city import City
from models.review import Review
import models


intro_text = """\
 ------------------------------
 |     Welcome to AirBnB       |
 ------------------------------

 Type 'quit' or 'Ctrl-D' to quit.
 Type 'help' command for overview or more details

"""


class HBNBCommand(cmd.Cmd):
    """class HBNBCommand"""
    intro = intro_text.format()

    prompt = ("(hbnb) ")
    __all_classes = {
          "BaseModel", "User", "Place", "State", "City", "Amenity", "Review"
       }

    def do_create(self, arg):
        """Creates a new instance of BaseModel, saves it (to the JSON file)
           and prints the id
           usage: create <class>
        """

        if not arg:
            print("** class name missing **")

        args = arg.split(" ")

        if len(args) == 1 and args[0] not in HBNBCommand.__all_classes:
            print("** class doesn't exist **")
            return False
        newInstance = eval(args[0])()
        newInstance.save()
        print(newInstance.id)

    def do_show(self, ag):
        """Prints the string representation of an instance based
           on the class name and id
           Usage: show <class> <id> or <class name>.show(<id>)
        """
        ags = ag.split()

        if len(ags) == 0:
            print("** class name missing **")
            return False

        class_name = ags[0]
        if class_name not in HBNBCommand.__all_classes:
            print("** class doesn't exist **")
            return False

        if len(ags) == 1:
            print("** instance id missing **")
            return False

        class_id = ags[1]
        key = f"{class_name}.{class_id}"
        if key in models.storage.all():
            all_objs = models.storage.all()
            print(all_objs[key])
        else:
            print("** no instance found **")
            return

    def do_destroy(self, ag):
        """Deletes an instance based on the class name and id and
           save the change into the JSON file)
           Usage: destroy <class> <id> or <class name>.destroy(<id>).
        """
        ags = ag.split()
        all_objs = models.storage.all()

        if len(ags) == 0:
            print("** class name missing **")
            return False

        class_name = ags[0]
        if class_name not in HBNBCommand.__all_classes:
            print("** class doesn't exist **")
            return False

        if len(ags) == 1:
            print("** instance id missing **")
            return

        class_id = ags[1]
        key = f"{class_name}.{class_id}"
        if key in all_objs:
            del all_objs[key]
            models.storage.save()
        else:
            print("** no instance found **")

    def do_all(self, ag):
        """Prints all string representation of all instances based or not
           on the class name
           Usage: all <class name> or all or <class name>.all()
        """
        ags = ag.split()
        all_objs = models.storage.all()

        if len(ags) > 0 and ags[0] not in HBNBCommand.__all_classes:
            print("** class doesn't exist **")
            return False
        all_obj = []

        for obj_id in all_objs.values():
            if len(ags) == 0:
                all_obj.append(obj_id.__str__())
            elif len(ags) > 0 and ags[0] == obj_id.__class__.__name__:
                all_obj.append(obj_id.__str__())
        print(all_obj)

    def do_update(self, arg):
        """Updates an instance based on the class name and id by adding or
           updating attribute (save the change into the JSON file
           Usage: update <class name> <id> <attribute name> "<attribute value>"
          or
           Usage: <class name>.update(<id>, <dictionary representation>).
        """
        arg = re.sub(r"[\"]", "", arg)
        args = arg.split()
        all_objs = models.storage.all()

        if len(args) == 0:
            print("** class name missing **")
            return False
        if len(args) > 0 and args[0] not in HBNBCommand.__all_classes:
            print("** class doesn't exist **")
            return False
        if len(args) == 1:
            print("** instance id missing **")
            return False

        if len(args) == 2:
            print("** attribute name missing **")
            return False
        if len(args) == 3:
            print("** value missing **")
            return False

        class_name = args[0]
        class_id = args[1]
        key = f"{class_name}.{class_id}"

        if len(args) == 4:
            obj = all_objs[key]
            dict_obj = obj.__class__.__dict__
            if args[2] in dict_obj.keys():
                arg_2_type = type(dict_obj[args[2]])
                obj.__dict__[args[2]] = arg_2_type(args[3])
            else:
                obj.__dict__[args[2]] = args[3]

        elif type(eval(args[2])) == dict:
            obj = all_objs[key]
            types = {str, float, int}
            for _key, val in eval(args[2]).items():
                if (_key in dict_obj.keys() and type(dict_obj[_key]) in types):
                    arg_2_type = type(dict_obj[_key])
                    obj.__dict__[_key] = arg_2_type(val)
                else:
                    obj.__dict__[_key] = val

        models.storage.save()

    def default(self, line):
        """handle class method like:
           Usage: <class name>.count()
           Usage: <class name>.all()
        """
        ags = re.match(r"^(\w+)\.(\w+)\((.*?)\)", line)
        all_commands = {
                     "all": self.do_all, "count": self.do_count,
                     "show": self.do_show, "destroy": self.do_destroy,
                     "update": self.do_update
                    }
        if ags:
            ags = ags.groups()
        if not ags or len(ags) < 2 or ags[0] not in HBNBCommand.__all_classes\
                or ags[1] not in all_commands.keys():
            super().default(line)
            return

        if ags[1] == "all" or ags[1] == "count":
            all_commands[ags[1]](ags[0])
        elif ags[1] == "show" or ags[1] == "destroy":
            all_commands[ags[1]](ags[0] + ' ' + ags[2])
        elif ags[1] == "update":
            parameters = re.match(r"\"(.+?)\", (.+)", ags[2])
            if parameters.groups()[1][0] == '{':
                dict_ob = eval(parameters.groups()[1])
                for key, val in dict_ob.items():
                    grp1 = ags[0] + " " + parameters.groups()[0]
                    grp2 = " " + key + " " + str(val)
                    all_commands[ags[1]](grp1 + grp2)
            else:
                others = parameters.groups()[1].split(", ")
                gp1 = ags[0] + " " + parameters.groups()[0]
                gp2 = " " + others[0] + " " + others[1]
                all_commands[ags[1]](gp1 + gp2)

    def do_count(self, arg):
        """retrieve the number of instances of a class:
           Usage: <class name>.count()
        """
        args = arg.split()
        numberOfInstance = 0
        class_name = args[0]
        all_objs = models.storage.all()
        for obj_id in models.storage.all().values():
            if class_name == obj_id.__class__.__name__:
                numberOfInstance += 1
        print(numberOfInstance)

    def emptyline(self):
        """disable the repetition of the last command"""
        pass

    def help_quit(self):
        """help for quit command"""
        print('\n'.join(['Quit command to exit the program' + '\n']))

    def do_quit(self, line):
        """quit command"""
        return True

    def do_EOF(self, line):
        """quit command"""
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
