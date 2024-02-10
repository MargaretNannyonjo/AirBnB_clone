#!/usr/bin/python3

import unittest
from models.base_model import BaseModel

class TestBaseModel(unittest.TestCase):
    def test_creation(self):
        model = BaseModel()
        self.assertIsInstance(model, BaseModel)
