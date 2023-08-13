#!/usr/bin/python3
"""
    test BaseModel
"""
from models.city import City
from models.base_model import BaseModel
import unittest


class test_city(unittest.TestCase):
    """BaseModel test"""

    @classmethod
    def setUpClass(cls):
        cls.city = City()

    @classmethod
    def tearDownClass(cls):
        del cls.city

    def test_string(self):
        """
            test attributes
        """
        b1 = City()
        self.assertIsInstance(b1.state_id, str)
        self.assertIsInstance(b1.name, str)

    def test_attributes(self):
        """
            test attributes
        """
        b1 = City()
        self.assertTrue(hasattr(b1, "state_id"))
        self.assertTrue(hasattr(b1, "name"))

    def test_class(self):
        """
            test_class
        """
        u1 = City()
        self.assertIsInstance(u1, City)

    def test_str(self):
        """
             User test:

        """
        u1 = City()
        class_name = u1.__class__.__name__
        string = "[{}] ({}) {}".format(class_name, u1.id, u1.__dict__)
        self.assertEqual(str(u1), string)

    def test_dict(self):
        """
            test_dict: test dictionary

        """
        user = City()
        dictd = user.to_dict()
        self.assertTrue("created_at" in dictd)

    def test_other_from_BaseModel(self):
        """
            test attributes

        """
        b1 = City()
        self.assertTrue(hasattr(b1, "created_at"))
        self.assertTrue(hasattr(b1, "updated_at"))
        self.assertTrue(hasattr(b1, "id"))
