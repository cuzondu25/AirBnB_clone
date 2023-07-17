#!/usr/bin/python3
"""testing the console"""

import unittest
from console import HBNBCommand


class Testconsole(unittest.TestCase):
    def test_prompt(self):
        self.assertEqual("(hbnb) ", HBNBCommand.prompt)
