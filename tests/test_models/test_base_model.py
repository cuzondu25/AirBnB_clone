#!/usr/bin/python3
"""Defines unittests for models/base_model.py.

Unittest classes:
    TestBaseModel_instantiation
    TestBaseModel_save
    TestBaseModel_to_dict
"""

from time import sleep
import os
import models
import unittest
from datetime import datetime
from models.base_model import BaseModel


class TestBaseModel_instantiation(unittest.TestCase):
    """Unittests for testing instantiation of the BaseModel class."""
    def test_new_instance_stored_in_objects(self):
        #self.skipTest("no reason")
        self.assertIn(BaseModel(), models.storage.all().values())

    def test_id_is_str(self):
        self.assertEqual(str, type(BaseModel().id))

    def test_created_at_is_datetime(self):
        self.assertEqual(datetime, type(BaseModel().created_at))

    def test_updated_at_is_datetime(self):
        self.assertEqual(datetime, type(BaseModel().updated_at))

    def test_two_models_unique_ids(self):
        b1 = BaseModel()
        b2 = BaseModel()
        self.assertNotEqual(b1.id, b2.id)


class TestBaseModel_to_dict(unittest.TestCase):
    """Unittests for testing to_dict method of the BaseModel class."""

    def test_to_dict_type(self):
        base = BaseModel()
        self.assertTrue(dict, type(base.to_dict()))

    def test_to_dict_contains_correct_keys(self):
        base = BaseModel()
        self.assertIn("id", base.to_dict())
        self.assertIn("created_at", base.to_dict())
        self.assertIn("updated_at", base.to_dict())
        self.assertIn("__class__", base.to_dict())

    def test_to_dict_contains_added_attributes(self):
        base = BaseModel()
        base.name = "Holberton"
        base.my_number = 98
        self.assertIn("name", base.to_dict())
        self.assertIn("my_number", base.to_dict())

    def test_str_(self):
        base = BaseModel()
        base.id = "123456"
        basestr = base.__str__()
        self.assertIn("[BaseModel] (123456)", basestr)
        self.assertIn("'id': '123456'", basestr)

class TestBaseModel_save(unittest.TestCase):
    """Unittests for testing save method of the BaseModel class."""

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

    def test_save(self):
        base = BaseModel()
        sleep(0.05)
        first_updated_at = base.updated_at
        base.save()
        self.assertLess(first_updated_at, base.updated_at)
