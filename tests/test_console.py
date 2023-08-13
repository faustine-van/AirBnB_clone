#!/usr/bin/python3
"""
    test console
"""
from console import HBNBCommand
from models.base_model import BaseModel
import unittest
from unittest.mock import patch
from io import StringIO


class test_console(unittest.TestCase):
    """
        BaseModel test
    """

    def SetUp(self):

        """
            SetUp
        """
        self.console = HBNBCommand()

    def test_prompt(self):
        """
            test show cammand
        """
        prompt = "(hbnb) "
        c = HBNBCommand.prompt
        self.assertEqual(prompt, c)

    def test_help_quit(self):
        """
            test show cammand
        """
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("help quit"))
            output = f.getvalue().strip()
            expexted_output = "Quit command to exit the program"
            self.assertEqual(expexted_output, output)

    def test_help_Eof(self):
        """
            test show cammand
        """
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("help EOF"))
            output = f.getvalue().strip()
            expexted_output = "Exit console using shortcut Ctrl+D"
            self.assertEqual(expexted_output, output)

    def test_help_quit(self):
        """
            test show cammand
        """
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("help quit"))
            output = f.getvalue().strip()
            expexted_output = "Quit command to exit the program"
            self.assertEqual(expexted_output, output)

    def test_help_destroy(self):
        """
            test show cammand
        """
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("help quit"))
            output = f.getvalue().strip()
            expexted_output = "Quit command to exit the program"
            self.assertEqual(expexted_output, output)

    def test_quit(self):
        """
            test quit cammand
        """
        with patch('sys.stdout', new=StringIO()) as f:
            quit = HBNBCommand().onecmd("quit")
            self.assertTrue(quit)

    def test_EOF(self):
        """
            test show cammand
        """
        with patch('sys.stdout', new=StringIO()) as f:
            EOF = HBNBCommand().onecmd("EOF")
            self.assertTrue(EOF)

    def test_create(self):
        """
            test show cammand
        """
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("create"))
            output = f.getvalue().strip()
            expexted_output = "** class name missing **"
            self.assertEqual(expexted_output, output)

    def test_create_wrong_class(self):
        """
            test show cammand
        """
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("create Bade"))
            output = f.getvalue().strip()
            expexted_output = "** class doesn't exist **"
            self.assertEqual(expexted_output, output)

    def test_create_invalid(self):
        """
            test show cammand
        """
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("BaseModel.create()"))
            output = f.getvalue().strip()
            expexted_output = "*** Unknown syntax: BaseModel.create()"
            self.assertEqual(expexted_output, output)

    def test_show(self):
        """
            test show cammand
        """
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("show"))
            output = f.getvalue().strip()
            expexted_output = "** class name missing **"
            self.assertEqual(expexted_output, output)

    def test_show_wrong_class(self):
        """
            test show cammand
        """
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("show MyModel"))
            output = f.getvalue().strip()
            expexted_output = "** class doesn't exist **"
            self.assertEqual(expexted_output, output)

    def test_show_invalid(self):
        """
            test show cammand
        """
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("show BaseModel"))
            output = f.getvalue().strip()
            expexted_output = "** instance id missing **"
            self.assertEqual(expexted_output, output)

    def test_show_no_instance(self):
        """
            test show cammand
        """
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("show BaseModel My_First"))
            output = f.getvalue().strip()
            expexted_output = "** no instance found **"
            self.assertEqual(expexted_output, output)

    def test_destroy(self):
        """
            test destroy cammand
        """
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("destroy"))
            output = f.getvalue().strip()
            expexted_output = "** class name missing **"
            self.assertEqual(expexted_output, output)

    def test_destroy_wrong_class(self):
        """
            test destroy cammand
        """
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("destroy MyModel"))
            output = f.getvalue().strip()
            expexted_output = "** class doesn't exist **"
            self.assertEqual(expexted_output, output)

    def test_destroy_invalid(self):
        """
            test destroy cammand
        """
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("destroy User"))
            output = f.getvalue().strip()
            expexted_output = "** instance id missing **"
            self.assertEqual(expexted_output, output)

    def test_show_no_instance(self):
        """
            test show cammand
        """
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("destroy User My_First"))
            output = f.getvalue().strip()
            expexted_output = "** no instance found **"
            self.assertEqual(expexted_output, output)

    def test_all_wrong_class(self):
        """
            test destroy cammand
        """
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("all MyModel"))
            output = f.getvalue().strip()
            expexted_output = "** class doesn't exist **"
            self.assertEqual(expexted_output, output)

    def test_update(self):
        """
            test  cammand
        """
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("update"))
            output = f.getvalue().strip()
            expexted_output = "** class name missing **"
            self.assertEqual(expexted_output, output)

    def test_destroy_wrong_class(self):
        """
            test update cammand
        """
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("update MyModel"))
            output = f.getvalue().strip()
            expexted_output = "** class doesn't exist **"
            self.assertEqual(expexted_output, output)

    def test_destroy_invalid(self):
        """
            test destroy cammand
        """
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("update User"))
            output = f.getvalue().strip()
            expexted_output = "** instance id missing **"
            self.assertEqual(expexted_output, output)
