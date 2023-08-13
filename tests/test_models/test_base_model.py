#!/usr/bin/python3
"""test BaseModel"""
from models.base_model import BaseModel
import unittest


class test_base(unittest.TestCase):
    """BaseModel test"""

    @classmethod
    def setup(self):
        print("setUp")

    def tearDown(self):
        print("tearDown")

    @classmethod
    def setUpClass(cls):
        print("setUpClass")

    @classmethod
    def tearDownClass(cls):
        print("tearDownClass")

    def test_equal(self):
      my_model = BaseModel()
      my_model.name = "My First Model"
      self.assertEqual(my_model.name, "My First Model")

    def test_Base(self):
        my_model = BaseModel()
        my_model.my_number = 89
        self.assertEqual(my_model.my_number, 89)
