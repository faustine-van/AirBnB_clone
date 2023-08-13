#!/usr/bin/python3
"""
    test FileStorage
"""
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
import unittest


class test_file_storage(unittest.TestCase):
    """FileStorage test"""

    @classmethod
    def setUpClass(cls):
        """
             setUpClass
        """
        cls.f1 = FileStorage()

    @classmethod
    def tearDownClass(cls):
        """
             tearDownClass
        """
        del cls.f1

    def test_attr(self):
        """
             test attributes
        """
        f1 = FileStorage()
        self.assertTrue(hasattr(f1, "_FileStorage__objects"))
        self.assertTrue(hasattr(f1, "_FileStorage__file_path"))
        self.assertIsInstance(f1._FileStorage__objects, dict)
        self.assertIsInstance(f1._FileStorage__file_path, str)
        self.assertEqual(f1._FileStorage__file_path, "file.json")
