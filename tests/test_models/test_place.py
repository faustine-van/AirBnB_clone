#!/usr/bin/python3
"""
       test Place
"""
from models.place import Place
from models.base_model import BaseModel
import unittest


class test_place(unittest.TestCase):
    """BaseModel test"""
    """
        Review class test
    """

    @classmethod
    def setUpClass(cls):
        """
             setupClass
        """
        cls.place = Place()

    @classmethod
    def tearDownClass(cls):
        """
            tearDownClass
        """
        del cls.place

    def test_dict(self):
        """
            test_dict: test dictionary

        """
        user = Place()
        dictd = user.to_dict()
        self.assertTrue("created_at" in dictd)

    def test_dict1(self):
        """
            test_dict: test dictionary

        """
        user = Place()
        dictd = user.to_dict()
        self.assertTrue("id" in dictd)

    def test_string_attr(self):
        """
            test attributes
        """
        b1 = Place()
        self.assertIsInstance(b1.user_id, str)
        self.assertIsInstance(b1.city_id, str)
        self.assertIsInstance(b1.name, str)
        self.assertIsInstance(b1.description, str)

    def test_int_attr(self):
        """
            test attributes
        """
        b1 = Place()
        self.assertIsInstance(b1.number_rooms, int)
        self.assertIsInstance(b1.number_bathrooms, int)
        self.assertIsInstance(b1.max_guest, int)
        self.assertIsInstance(b1.price_by_night, int)

    def test_int_attr(self):
        """
            test attributes
        """
        b1 = Place()
        self.assertIsInstance(b1.latitude, float)
        self.assertIsInstance(b1.longitude,  float)
        self.assertIsInstance(b1.amenity_ids, list)

    def test_attributes(self):
        """
            test attributes
        """
        b1 = Place()
        self.assertTrue(hasattr(b1, "user_id"))

    def test_class(self):
        """
            test class
        """
        u1 = self.place
        self.assertIsInstance(u1, Place)

    def test_str(self):
        """
             test str for state class:

        """
        u1 = Place()
        class_name = u1.__class__.__name__
        string = "[{}] ({}) {}".format(class_name, u1.id, u1.__dict__)
        self.assertEqual(str(u1), string)

    def test_dict_id(self):
        """
            test_dict: test dictionary

        """
        user = Place()
        dictd = user.to_dict()
        self.assertTrue("id" in dictd)

    def test_dict_id(self):
        """
            test_dict: test dictionary

        """
        u1 = Place()
        dictd = u1.to_dict()
        self.assertTrue("updated_at" in dictd)

    def test_other_from_basemodel(self):
        """
            test attributes

        """
        b1 = Place()
        self.assertTrue(hasattr(b1, "created_at"))
        self.assertTrue(hasattr(b1, "updated_at"))
        self.assertTrue(hasattr(b1, "id"))
