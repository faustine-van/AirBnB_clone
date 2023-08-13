#!/usr/bin/python3
"""
    test User information
"""
from models.base_model import BaseModel
from models.user import User
import unittest
import re


class test_user(unittest.TestCase):
    """
        User test class
    """

    @classmethod
    def setUpClass(cls):
        """
            setUpClass

        """
        print("setUpClass")

    @classmethod
    def tearDownClass(cls):
        """
            tearDownClass

        """
        print("tearDownClass")

    def test_string(self):
        """
            test attributes

        """
        b1 = User()
        self.assertIsInstance(b1.email, str)
        self.assertIsInstance(b1.password, str)
        self.assertIsInstance(b1.first_name, str)
        self.assertIsInstance(b1.last_name, str)


    def test_attributes(self):
        """
            test attributes

        """
        b1 = User()
        self.assertTrue(hasattr(b1, "email"))
        self.assertTrue(hasattr(b1, "password"))
        self.assertTrue(hasattr(b1, "first_name"))
        self.assertTrue(hasattr(b1, "last_name"))

    def test_class(self):
        """
            test_class
        """
        u1 = User()
        self.assertIsInstance(u1, User)

    def test_str(self):
        """
             User test:

        """
        u1 = User()
        class_name = u1.__class__.__name__
        string = "[{}] ({}) {}".format(class_name, u1.id, u1.__dict__)
        self.assertEqual(str(u1), string)

    def test_dict(self):
        """
            test_dict: test dictionary

        """
        user = User()
        dictd = user.to_dict()
        self.assertTrue("created_at" in dictd)

    def test_other_from_BaseModel(self):
        """
            test attributes

        """
        b1 = User()
        self.assertTrue(hasattr(b1, "created_at"))
        self.assertTrue(hasattr(b1, "updated_at"))
        self.assertTrue(hasattr(b1, "id"))
