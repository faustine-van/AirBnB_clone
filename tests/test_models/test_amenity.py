#!/usr/bin/python3
"""
     test Amenity
"""
from models.amenity import Amenity
from models.base_model import BaseModel
import unittest


class test_amenity(unittest.TestCase):
    """
         Amenity class test
    """

    @classmethod
    def setUpClass(cls):
        """
            setUpClass
        """
        cls.amenity = Amenity()

    @classmethod
    def tearDownClass(cls):
        """
            tearDownClass
        """
        del cls.amenity

    def test_string(self):
        """
            test attributes
        """
        b1 = Amenity()
        self.assertIsInstance(b1.name, str)

    def test_attributes(self):
        """
            test attributes
        """
        b1 = Amenity()
        self.assertTrue(hasattr(b1, "name"))

    def test_class(self):
        """
            test class
        """
        u1 = Amenity()
        self.assertIsInstance(u1, Amenity)

    def test_str(self):
        """
             test str for State class:

        """
        u1 = Amenity()
        class_name = u1.__class__.__name__
        string = "[{}] ({}) {}".format(class_name, u1.id, u1.__dict__)
        self.assertEqual(str(u1), string)

    def test_dict(self):
        """
            test_dict: test dictionary

        """
        user = Amenity()
        dictd = user.to_dict()
        self.assertTrue("created_at" in dictd)

    def test_dict_id(self):
        """
            test_dict: test dictionary

        """
        user = Amenity()
        dictd = user.to_dict()
        self.assertTrue("id" in dictd)

    def test_other_from_BaseModel(self):
        """
            test attributes

        """
        b1 = Amenity()
        self.assertTrue(hasattr(b1, "created_at"))
        self.assertTrue(hasattr(b1, "updated_at"))
        self.assertTrue(hasattr(b1, "id"))
