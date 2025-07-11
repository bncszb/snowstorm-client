# coding: utf-8

"""
    Snowstorm

    SNOMED CT Terminology Server REST API

    The version of the OpenAPI document: 10.8.2
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from snowstorm_client.models.annotation_component import AnnotationComponent

class TestAnnotationComponent(unittest.TestCase):
    """AnnotationComponent unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AnnotationComponent:
        """Test AnnotationComponent
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AnnotationComponent`
        """
        model = AnnotationComponent()
        if include_optional:
            return AnnotationComponent(
                internal_id = '',
                path = '',
                start = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                end = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                deleted = True,
                changed = True,
                active = True,
                module_id = '01234',
                effective_time_i = 56,
                released = True,
                release_hash = '',
                released_effective_time = 56,
                refset_id = '01234',
                referenced_component_id = '01234',
                concept_id = '',
                referenced_component_snomed_component = snowstorm_client.models.snomed_component_object_component.SnomedComponentObject_Component(
                    internal_id = '', 
                    path = '', 
                    start = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    end = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    deleted = True, 
                    changed = True, 
                    active = True, 
                    module_id = '01234', 
                    effective_time_i = 56, 
                    released = True, 
                    release_hash = '', 
                    released_effective_time = 56, 
                    effective_time = '', 
                    id = '', ),
                map_target_coding = snowstorm_client.models.coding_component.Coding_Component(
                    system = '', 
                    code = '', 
                    display = '', ),
                annotation_id = '',
                type_id = '',
                value = '',
                language_dialect_code = '',
                type_pt = snowstorm_client.models.term_lang_pojo_component.TermLangPojo_Component(
                    term = '', 
                    lang = '', ),
                effective_time = '',
                map_group = '',
                map_priority = '',
                referenced_component = None
            )
        else:
            return AnnotationComponent(
                refset_id = '01234',
                referenced_component_id = '01234',
        )
        """

    def testAnnotationComponent(self):
        """Test AnnotationComponent"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
