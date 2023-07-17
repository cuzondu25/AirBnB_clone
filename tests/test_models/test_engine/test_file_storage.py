#!/usr/bin/python3
"""unittests for file_storage.py.

Unittest classes:
    Test_FileStorage_instantiation
    Test_FileStorage_methods
"""
import os
import json
import models
import unittest
from datetime import datetime
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestFileStorage_instantiation(unittest.TestCase):
    """testing instantiation of the FileStorage class."""

    def test_FileStorage_instantiation_with_arg(self):
        with self.assertRaises(TypeError):
            FileStorage(None)

    def test_file_path_is_private_str(self):
        self.assertEqual(str, type(FileStorage._FileStorage__file_path))

    def test_objects_is_private_dict(self):
        self.assertEqual(dict, type(FileStorage._FileStorage__objects))


class TestFileStorage_methods(unittest.TestCase):
    """Unittests for testing methods of the FileStorage class."""

    @classmethod
    def setUp(self):
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass

    @classmethod
    def tearDown(self):
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("tmp", "file.json")
        except IOError:
            pass
        FileStorage._FileStorage__objects = {}

    def test_all(self):
        self.assertEqual(dict, type(models.storage.all()))

    def test_all_with_arg(self):
        with self.assertRaises(TypeError):
            models.storage.all(None)

    def test_new(self):
        base = BaseModel()
        models.storage.new(base)
        self.assertIn("BaseModel." + base.id, models.storage.all().keys())
        self.assertIn(base, models.storage.all().values())

    def test_save(self):
        base = BaseModel()
        models.storage.new(base)
        models.storage.save()
        save_text = ""
        with open("file.json", "r") as f:
            save_text = f.read()
            self.assertIn("BaseModel." + base.id, save_text)

    def test_reload(self):
        base = BaseModel()
        models.storage.new(base)
        obj = FileStorage._FileStorage__objects
        self.assertIn("BaseModel." + base.id, obj)
