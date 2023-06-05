import unittest
from src.main import add


class TestAdd(unittest.TestCase):
    def test_add_normal_with_int(self):
        a = 1
        b = 2
        self.assertEqual(add(a, b), 3)

    def test_add_with_floats(self):
        a = 5.0
        b = 7.0
        self.assertEqual(add(a, b), 12.0)

    def test_add_with_strings(self):
        a = "Hello "
        b = "World"
        self.assertRaises(TypeError, add, a, b)