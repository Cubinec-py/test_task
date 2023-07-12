import unittest
import random

from hash_map import MyHashMap


class HashMapTest(unittest.TestCase):

    def setUp(self):
        self.map = MyHashMap()

    def test_key_int_put(self):
        for _ in range(100):
            key = random.randint(1, 100)
            self.map.put(key, 'value')
            self.assertEqual(self.map.get(key), 'value')

    def test_key_str_put(self):
        for _ in range(100):
            key = f'key_{random.randint(1, 100)}'
            self.map.put(key, 1)
            self.assertEqual(self.map.get(key), 1)

    def test_value_int_put(self):
        for _ in range(100):
            value = random.randint(1, 100)
            self.map.put(1, value)
            self.assertEqual(self.map.get(1), value)

    def test_value_str_put(self):
        for _ in range(100):
            value = f'value_{random.randint(1, 100)}'
            self.map.put(1, value)
            self.assertEqual(self.map.get(1), value)

    def test_value_error(self):
        self.map.put(1, 'value')
        with self.assertRaises(ValueError):
            self.map.get(2)

    def test_value_2_error(self):
        for key in range(1, 101):
            value = random.randint(1, 100)
            self.map.put(key, value)
        with self.assertRaises(ValueError):
            self.map.get(101)

