# coding: utf-8

"""
    Snowstorm

    SNOMED CT Terminology Server REST API

    The version of the OpenAPI document: 10.8.2
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from snowstorm_client.models.term_lang_pojo import TermLangPojo

class TestTermLangPojo(unittest.TestCase):
    """TermLangPojo unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TermLangPojo:
        """Test TermLangPojo
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TermLangPojo`
        """
        model = TermLangPojo()
        if include_optional:
            return TermLangPojo(
                term = '',
                lang = ''
            )
        else:
            return TermLangPojo(
        )
        """

    def testTermLangPojo(self):
        """Test TermLangPojo"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
