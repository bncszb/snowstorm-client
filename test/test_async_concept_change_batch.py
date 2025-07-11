# coding: utf-8

"""
    Snowstorm

    SNOMED CT Terminology Server REST API

    The version of the OpenAPI document: 10.8.2
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from snowstorm_client.models.async_concept_change_batch import AsyncConceptChangeBatch

class TestAsyncConceptChangeBatch(unittest.TestCase):
    """AsyncConceptChangeBatch unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AsyncConceptChangeBatch:
        """Test AsyncConceptChangeBatch
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AsyncConceptChangeBatch`
        """
        model = AsyncConceptChangeBatch()
        if include_optional:
            return AsyncConceptChangeBatch(
                id = '',
                start_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                status = 'RUNNING',
                concept_ids = [
                    56
                    ],
                end_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                message = '',
                seconds_duration = 1.337
            )
        else:
            return AsyncConceptChangeBatch(
        )
        """

    def testAsyncConceptChangeBatch(self):
        """Test AsyncConceptChangeBatch"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
