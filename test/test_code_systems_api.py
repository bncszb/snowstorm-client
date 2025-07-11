# coding: utf-8

"""
    Snowstorm

    SNOMED CT Terminology Server REST API

    The version of the OpenAPI document: 10.8.2
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from snowstorm_client.api.code_systems_api import CodeSystemsApi


class TestCodeSystemsApi(unittest.TestCase):
    """CodeSystemsApi unit test stubs"""

    def setUp(self) -> None:
        self.api = CodeSystemsApi()

    def tearDown(self) -> None:
        pass

    def test_find_all_versions(self) -> None:
        """Test case for find_all_versions

        Retrieve versions of a code system
        """
        pass

    def test_find_code_system(self) -> None:
        """Test case for find_code_system

        Retrieve a code system
        """
        pass

    def test_get_latest_daily_build(self) -> None:
        """Test case for get_latest_daily_build

        Check if daily build import matches today's date.
        """
        pass

    def test_get_upgrade_job(self) -> None:
        """Test case for get_upgrade_job

        Retrieve an upgrade job.
        """
        pass

    def test_list_code_systems(self) -> None:
        """Test case for list_code_systems

        List code systems
        """
        pass


if __name__ == '__main__':
    unittest.main()
