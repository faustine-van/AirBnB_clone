#!/usr/bin/python3
"""test BaseModel"""
from models.base_model import BaseModel
import unittest


class test_console(unittest.TestCase):
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
