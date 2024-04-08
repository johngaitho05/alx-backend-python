#!/usr/bin/env python3
"""Test cases for client module"""
import unittest
from unittest.mock import patch, Mock

from parameterized import parameterized
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """Test GithubOrgClient"""

    @parameterized.expand([
        ("google",),
        ("abc",)
    ])
    @patch('client.get_json')
    def test_org(self, org_name, mock_get_json):
        """Test org method of GithubOrgClient"""
        # Create a GithubOrgClient instance
        client = GithubOrgClient(org_name)

        # Mock the return value of get_json
        expected_result = {"org_info": "example"}
        mock_get_json.return_value = expected_result

        # Call the org method
        result = client.org

        # Assert that get_json is called once with the correct argument
        mock_get_json.assert_called_once_with(
            GithubOrgClient.ORG_URL.format(org=org_name))

        # Assert that the result matches the expected result
        self.assertEqual(result, expected_result)


if __name__ == '__main__':
    unittest.main()
