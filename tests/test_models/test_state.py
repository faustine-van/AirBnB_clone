#!/usr/bin/python3
"""test BaseModel"""
from models.state import State
import unittest


class test_state(unittest.TestCase):
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
