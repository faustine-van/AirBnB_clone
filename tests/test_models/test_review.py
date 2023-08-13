#!/usr/bin/python3
"""
     test Review
"""
from models.base_model import BaseModel
from models.review import Review
import unittest


class test_review(unittest.TestCase):
    """
        Review class test
    """

    @classmethod
    def setUpClass(cls):
        """
             setupClass
        """
        cls.review = Review()

    @classmethod
    def tearDownClass(cls):
        """
            tearDownClass
        """
        del cls.review

    def test_dict(self):
        """
            test_dict: test dictionary

        """
        user = Review()
        dictd = user.to_dict()
        self.assertTrue("created_at" in dictd)

    def test_string(self):
        """
            test attributes
        """
        b1 = Review()
        self.assertIsInstance(b1.user_id, str)
        self.assertIsInstance(b1.place_id, str)
        self.assertIsInstance(b1.text, str)

    def test_attributes(self):
        """
            test attributes
        """
        b1 = Review()
        self.assertTrue(hasattr(b1, "user_id"))

    def test_class(self):
        """
            test class
        """
        u1 = self.review
        self.assertIsInstance(u1, Review)

    def test_str(self):
        """
             test str for state class:

        """
        u1 = Review()
        class_name = u1.__class__.__name__
        string = "[{}] ({}) {}".format(class_name, u1.id, u1.__dict__)
        self.assertEqual(str(u1), string)

    def test_dict_id(self):
        """
            test_dict: test dictionary

        """
        user = Review()
        dictd = user.to_dict()
        self.assertTrue("id" in dictd)

    def test_other_from_basemodel(self):
        """
            test attributes

        """
        b1 = Review()
        self.assertTrue(hasattr(b1, "created_at"))
        self.assertTrue(hasattr(b1, "updated_at"))
        self.assertTrue(hasattr(b1, "id"))
