#!/usr/bin/python3
"""
    test FileStorage
"""
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
import unittest
import models
import re


class test_file_storage(unittest.TestCase):
    """FileStorage test"""

    @classmethod
    def setUpClass(cls):
        """
             setUpClass
        """
        cls.f1 = FileStorage()
        cls.basemodel = BaseModel()

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

    def test_all(self):
        """
             test all
        """
        all_objs = models.storage.all()
        self.assertEqual(dict, type(all_objs))
        self.assertIsInstance(all_objs, dict)
        all_obj1 = models.storage.all()
        with self.assertRaises(TypeError):
            models.storage.all(None)

    def test_new(self):
        """
             test new() method
        """
        b1 = BaseModel()
        models.storage.new(b1)
        models.storage.save()
        models.storage.reload()
        objs = FileStorage._FileStorage__objects
        self.assertIn("BaseModel." + b1.id, objs)

        with self.assertRaises(TypeError):
            models.storage.new()

    def test_reload(self):
        """
             test reload() method
        """
        with self.assertRaises(TypeError):
            models.storage.reload(None)

    def test_save(self):
        """
             test save() method
        """
        b1 = BaseModel()
        str_b1 = "BaseModel."
        models.storage.new(b1)
        models.storage.save()
        text = ""
        with open("file.json", "r") as file:
            text = file.read()
            self.assertIn(str_b1 + b1.id, text)

    def test_save(self):
        """
             test save() method
        """
        b1 = BaseModel()
        str_b1 = "BaseModel."
        models.storage.new(b1)
        models.storage.save()
        text = ""
        with open("file.json", "r") as file:
            text = file.read()
            self.assertIn(str_b1 + b1.id, text)

    def test_save_updated_at(self):
        """
            test

        """
        bs = self.basemodel
        old_updated_at = bs.updated_at
        bs.save()
        new_updated_at = bs.updated_at
        self.assertNotEqual(old_updated_at, new_updated_at)
