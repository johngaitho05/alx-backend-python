#!/usr/bin/env python3
"""Test cases for utils"""
import unittest

from parameterized import parameterized
from utils import access_nested_map


class TestAccessNestedMap(unittest.TestCase):
    """Test cases"""

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map, nested_key, expected_result):
        """Test access_nested_map function"""
        self.assertEqual(access_nested_map(nested_map, nested_key),
                         expected_result)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b")),
    ])
    def test_access_nested_map_exception(self, nested_map, nested_key):
        """Test KeyError"""
        with self.assertRaises(KeyError):
            access_nested_map(nested_map, nested_key)
