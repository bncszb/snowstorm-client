# coding: utf-8

"""
    Snowstorm

    SNOMED CT Terminology Server REST API

    The version of the OpenAPI document: 10.8.2
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from snowstorm_client.models.permission_record_component import PermissionRecordComponent

class TestPermissionRecordComponent(unittest.TestCase):
    """PermissionRecordComponent unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PermissionRecordComponent:
        """Test PermissionRecordComponent
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PermissionRecordComponent`
        """
        model = PermissionRecordComponent()
        if include_optional:
            return PermissionRecordComponent(
                role = '',
                path = '',
                var_global = True,
                user_groups = [
                    ''
                    ]
            )
        else:
            return PermissionRecordComponent(
        )
        """

    def testPermissionRecordComponent(self):
        """Test PermissionRecordComponent"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
