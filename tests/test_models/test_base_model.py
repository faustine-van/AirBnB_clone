#!/usr/bin/python3
"""test BaseModel"""
from models.base_model import BaseModel
import unittest
import re


class test_base(unittest.TestCase):
    """BaseModel test"""

    @classmethod
    def setUpClass(cls):
        """setup class"""
        cls.basemodel = BaseModel()

    @classmethod
    def tearDownClass(cls):
        print("tearDownClass")

    def test_valid_id(self):
        basemodel = self.basemodel
        self.assertIsInstance(basemodel, BaseModel)
    def test_id_is_string(self):
        basemodel = self.basemodel
        self.assertIsInstance(basemodel.id, str)
    def test_id_match(self):
        my_model = BaseModel()
        match = re.fullmatch(r"\w{8}-\w{4}-\w{4}-\w{4}-\w{12}", my_model.id)
        self.assertTrue(match)
