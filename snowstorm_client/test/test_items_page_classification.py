# coding: utf-8

"""
    Snowstorm

    SNOMED CT Terminology Server REST API

    The version of the OpenAPI document: 10.8.2
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from snowstorm_client.models.items_page_classification import ItemsPageClassification

class TestItemsPageClassification(unittest.TestCase):
    """ItemsPageClassification unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ItemsPageClassification:
        """Test ItemsPageClassification
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ItemsPageClassification`
        """
        model = ItemsPageClassification()
        if include_optional:
            return ItemsPageClassification(
                items = [
                    snowstorm_client.models.classification.Classification(
                        id = '', 
                        path = '', 
                        status = 'SCHEDULED', 
                        error_message = '', 
                        reasoner_id = '', 
                        user_id = '', 
                        creation_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        completion_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        last_commit_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        save_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        inferred_relationship_changes_found = True, 
                        redundant_stated_relationships_found = True, 
                        equivalent_concepts_found = True, )
                    ],
                total = 56,
                limit = 56,
                offset = 56,
                search_after = '',
                search_after_array = [
                    None
                    ]
            )
        else:
            return ItemsPageClassification(
        )
        """

    def testItemsPageClassification(self):
        """Test ItemsPageClassification"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
