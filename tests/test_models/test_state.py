#!/usr/bin/python3
"""
    State
"""
from models.state import State
from models.base_model import BaseModel
from models.user import User
from models.city import City
from models.review import Review
from models.place import Place
import unittest


class test_state(unittest.TestCase):
    """
         State class test
    """

    @classmethod
    def setUpClass(cls):
        """
            setUpClass
        """
        cls.state = State()

    @classmethod
    def tearDownClass(cls):
        """
            tearDownClass
        """
        del cls.state

    def test_string(self):
        """
            test attributes
        """
        b1 = State()
        self.assertIsInstance(b1.name, str)

    def test_attributes(self):
        """
            test attributes
        """
        b1 = State()
        self.assertTrue(hasattr(b1, "name"))

    def test_class(self):
        """
            test class
        """
        u1 = State()
        self.assertIsInstance(u1, State)

    def test_str(self):
        """
             test str for State class:

        """
        u1 = State()
        class_name = u1.__class__.__name__
        string = "[{}] ({}) {}".format(class_name, u1.id, u1.__dict__)
        self.assertEqual(str(u1), string)

    def test_dict(self):
        """
            test_dict: test dictionary

        """
        user = State()
        dictd = user.to_dict()
        self.assertTrue("created_at" in dictd)

    def test_dict_id(self):
        """
            test_dict: test dictionary

        """
        user = State()
        dictd = user.to_dict()
        self.assertTrue("id" in dictd)

    def test_other_from_BaseModel(self):
        """
            test attributes

        """
        b1 = State()
        self.assertTrue(hasattr(b1, "created_at"))
        self.assertTrue(hasattr(b1, "updated_at"))
        self.assertTrue(hasattr(b1, "id"))
