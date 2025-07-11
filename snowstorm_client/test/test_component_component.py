# coding: utf-8

"""
    Snowstorm

    SNOMED CT Terminology Server REST API

    The version of the OpenAPI document: 10.8.2
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from snowstorm_client.models.component_component import ComponentComponent

class TestComponentComponent(unittest.TestCase):
    """ComponentComponent unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ComponentComponent:
        """Test ComponentComponent
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ComponentComponent`
        """
        model = ComponentComponent()
        if include_optional:
            return ComponentComponent(
                id = '',
                active = True,
                released = True,
                module_id = '',
                published = True
            )
        else:
            return ComponentComponent(
        )
        """

    def testComponentComponent(self):
        """Test ComponentComponent"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
