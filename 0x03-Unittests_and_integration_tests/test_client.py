#!/usr/bin/env python3
"""Unittests and Integeration tests"""
import unittest
from unittest.mock import patch
from parameterized import parameterized
from client import GithubOrgClient

class TestGithubOrgClient(unittest.TestCase):
    """Test cases for GithubOrgClient.org method."""

    @parameterized.expand([
        ("google",),
        ("abc",),
    ])
    @patch('client.get_json')
    def test_org(self, org_name, mock_get_json):
        """Test that get_json is called with correct org."""
        client = GithubOrgClient(org_name)
        client.org()
        mock_get_json.assert_called_once_with(f"https://api.github.com/orgs/{org_name}")


class TestGithubOrgClient(unittest.TestCase):
    """Test cases for _public_repos_url method."""

    @patch('client.GithubOrgClient.org', return_value={"repos_url": "http://github.com/repos"})
    def test_public_repos_url(self, mock_org):
        """Test that _public_repos_url returns correct URL."""
        client = GithubOrgClient("google")
        self.assertEqual(client._public_repos_url, "http://github.com/repos")


class TestGithubOrgClient(unittest.TestCase):
    """Test cases for public_repos method."""

    @patch('client.get_json')
    @patch('client.GithubOrgClient._public_repos_url', new_callable=lambda: "http://github.com/repos")
    def test_public_repos(self, mock_repos_url, mock_get_json):
        """Test public_repos method."""
        mock_get_json.return_value = [{"name": "repo1"}, {"name": "repo2"}]
        client = GithubOrgClient("google")
        self.assertEqual(client.public_repos(), ["repo1", "repo2"])
        mock_repos_url.assert_called_once()
        mock_get_json.assert_called_once()


class TestGithubOrgClient(unittest.TestCase):
    """Test cases for has_license method."""

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False),
    ])
    def test_has_license(self, repo, license_key, expected):
        """Test that has_license returns correct value."""
        client = GithubOrgClient("google")
        self.assertEqual(client.has_license(repo, license_key), expected)

