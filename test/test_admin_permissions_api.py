# coding: utf-8

"""
    Snowstorm

    SNOMED CT Terminology Server REST API

    The version of the OpenAPI document: 10.8.2
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from snowstorm_client.api.admin_permissions_api import AdminPermissionsApi


class TestAdminPermissionsApi(unittest.TestCase):
    """AdminPermissionsApi unit test stubs"""

    def setUp(self) -> None:
        self.api = AdminPermissionsApi()

    def tearDown(self) -> None:
        pass

    def test_find_all(self) -> None:
        """Test case for find_all

        Retrieve all permissions
        """
        pass

    def test_find_for_branch(self) -> None:
        """Test case for find_for_branch

        Retrieve all permissions on given branch
        """
        pass

    def test_find_global(self) -> None:
        """Test case for find_global

        Retrieve all global permissions
        """
        pass

    def test_find_user_group_permissions(self) -> None:
        """Test case for find_user_group_permissions

        Retrieve all permissions for a provided user group
        """
        pass


if __name__ == '__main__':
    unittest.main()
