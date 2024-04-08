#!/usr/bin/env python3
"""Test cases for client module"""
import unittest
from unittest.mock import patch, MagicMock

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

    class TestGithubOrgClient(unittest.TestCase):
        """Test cases for GithubOrgClient"""

        def test_public_repos(self):
            """Test public_repos method of GithubOrgClient"""
            # Define a known payload for the mocked get_json
            known_payload = [
                {"name": "repo1", "license": {"key": "MIT"}},
                {"name": "repo2", "license": {"key": "GPL-3.0"}},
                {"name": "repo3"}  # No license key in this repo
            ]

            # Define a known URL for _public_repos_url
            known_url = "https://api.github.com/orgs/example_org/repos"

            # Patch get_json as a context manager
            with (patch('github_org_client.get_json') as mock_get_json):
                # Set the return value of the mock get_json
                mock_get_json.return_value = known_payload

                # Patch _public_repos_url as a context manager
                with patch.object(GithubOrgClient, '_public_repos_url'
                                  ) as mock_repos_url:
                    # Set the return value of the mock _public_repos_url
                    mock_repos_url.return_value = known_url

                    # Create a GithubOrgClient instance
                    client = GithubOrgClient("example_org")

                    # Call the public_repos method
                    result = client.public_repos(license="MIT")

                    # Assert that get_json was called once with the
                    # correct argument
                    mock_get_json.assert_called_once_with(known_url)

                    # Assert the result
                    self.assertEqual(result, ["repo1"])


if __name__ == '__main__':
    unittest.main()
