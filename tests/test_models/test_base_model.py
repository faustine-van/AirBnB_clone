#!/usr/bin/python3
"""
    test BaseModel
"""
from models.base_model import BaseModel
import unittest
import re
from datetime import datetime


class test_base(unittest.TestCase):
    """
        BaseModel test
     """

    @classmethod
    def setUpClass(cls):
        """setup class"""
        cls.basemodel = BaseModel()

    @classmethod
    def tearDownClass(cls):
        """
            User test:
        """
        del cls.basemodel

    def test_valid_id(self):
        """
            test_valid_id
        """
        basemodel = self.basemodel
        self.assertIsInstance(basemodel, BaseModel)

    def test_attributes(self):
        """
            test attributes

        """
        b1 = BaseModel()
        self.assertTrue(hasattr(b1, "created_at"))
        self.assertTrue(hasattr(b1, "id"))
        self.assertTrue(hasattr(b1, "updated_at"))

    def test_id_is_string(self):
        """
           test if id is string
        """
        basemodel = self.basemodel
        self.assertIsInstance(basemodel.id, str)

    def test_id_match(self):
        """
            match id
        """
        my_model = BaseModel()
        match = re.fullmatch(r"\w{8}-\w{4}-\w{4}-\w{4}-\w{12}", my_model.id)
        self.assertTrue(match)

    def test_id_is_string(self):
        basemodel = self.basemodel
        self.assertIsInstance(basemodel.id, str)

    def test_create_at(self):
        basemodel = self.basemodel
        self.assertIsInstance(basemodel.created_at, datetime)

    def test_updated_at(self):
        basemodel = self.basemodel
        self.assertIsInstance(basemodel.updated_at, datetime)

    def test_str(self):
        b1 = BaseModel()
        class_name = "BaseModel"
        string = "[{}] ({}) {}".format(class_name, b1.id, b1.__dict__)
        self.assertEqual(str(b1), string)

    def test_to_dict(self):
        b1 = BaseModel()
        dictd = b1.to_dict()
        self.assertTrue("created_at" in dictd)
        self.assertTrue("updated_at" in dictd)
        self.assertTrue("id" in dictd)

    def test_is_equal(self):
        b1 = BaseModel()
        dictd = b1.to_dict()
        self.assertTrue("__class__" in dictd)
