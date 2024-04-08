#!/usr/bin/env python3
"""Test cases for client module"""
import unittest
from unittest.mock import patch, MagicMock, PropertyMock

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

    def test_public_repos_url(self):
        """Test _public_repos_url method of GithubOrgClient"""
        # Define a known payload for the org method
        known_payload = {
            "repos_url": "https://api.github.com/orgs/example_org/repos"
        }

        # Patch the org method to return the known payload
        with patch.object(GithubOrgClient, 'org') as mock_org:
            # Set the return value of the mock to the known payload
            mock_org.return_value = known_payload

            # Create a GithubOrgClient instance
            client = GithubOrgClient("example_org")

            # Call the _public_repos_url method
            result = client._public_repos_url

            # Assert that the result matches the expected repos_url
            # from the known payload
            self.assertEqual(result, known_payload["repos_url"])

    @patch('client.get_json')
    def test_public_repos(self, mocked_method):
        '''self descriptive'''
        payload = [{"name": "Google"}, {"name": "TT"}]
        mocked_method.return_value = payload

        with patch('client.GithubOrgClient._public_repos_url',
                   new_callable=PropertyMock) as mocked_public:
            mocked_public.return_value = "world"
            response = GithubOrgClient('test').public_repos()

            self.assertEqual(response, ["Google", "TT"])

            mocked_public.assert_called_once()
            mocked_method.assert_called_once()


if __name__ == '__main__':
    unittest.main()
