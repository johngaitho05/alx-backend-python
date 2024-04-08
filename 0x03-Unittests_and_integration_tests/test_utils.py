#!/usr/bin/env python3
"""Test cases for utils"""
import unittest
from unittest.mock import patch, Mock

from parameterized import parameterized
from utils import access_nested_map, get_json


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


class TestGetJson(unittest.TestCase):
    """Test get_json function"""

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    @patch('requests.get')
    def test_get_json(self, test_url, test_payload, mock_get):
        """Test get_json function"""
        mock_get.return_value = Mock()
        mock_get.return_value.json.return_value = test_payload

        # Call the function
        result = get_json(test_url)

        # Assert that requests.get is called once with the correct URL
        mock_get.assert_called_once_with(test_url)

        # Assert that the output of get_json is equal to test_payload
        self.assertEqual(result, test_payload)
