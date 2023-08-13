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
    User test:

    """

    @classmethod
    def setUpClass(cls):
        print("setUpClass")

    @classmethod
    def tearDownClass(cls):
        print("tearDownClass")

    def test_string(self):
        b1 = User()
        self.assertIsInstance(b1.email, str)
        self.assertIsInstance(b1.password, str)
        self.assertIsInstance(b1.first_name, str)
        self.assertIsInstance(b1.last_name, str)

    def test_class(self):
        u1 = User()
        self.assertIsInstance(u1, User)

    def test_str(self):
        u1 = User()
        class_name = u1.__class__.__name__
        string = "[{}] ({}) {}".format(class_name, u1.id, u1.__dict__)
        self.assertEqual(str(u1), string)

    def test_dict(self):
        user = User()
        dictd = user.to_dict()
        self.assertTrue("created_at" in dictd)
