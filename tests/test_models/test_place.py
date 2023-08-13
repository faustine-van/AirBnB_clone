#!/usr/bin/python3
"""test BaseModel"""
from models.place import Place
import unittest


class test_place(unittest.TestCase):
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
