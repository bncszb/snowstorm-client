# InactivationTypeAndConceptIdListComponent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**inactivation_indicator** | [**ConceptMiniComponent**](ConceptMiniComponent.md) |  | [optional] 
**concept_ids** | **List[int]** |  | [optional] 

## Example

```python
from snowstorm_client.models.inactivation_type_and_concept_id_list_component import InactivationTypeAndConceptIdListComponent

# TODO update the JSON string below
json = "{}"
# create an instance of InactivationTypeAndConceptIdListComponent from a JSON string
inactivation_type_and_concept_id_list_component_instance = InactivationTypeAndConceptIdListComponent.from_json(json)
# print the JSON string representation of the object
print(InactivationTypeAndConceptIdListComponent.to_json())

# convert the object into a dict
inactivation_type_and_concept_id_list_component_dict = inactivation_type_and_concept_id_list_component_instance.to_dict()
# create an instance of InactivationTypeAndConceptIdListComponent from a dict
inactivation_type_and_concept_id_list_component_from_dict = InactivationTypeAndConceptIdListComponent.from_dict(inactivation_type_and_concept_id_list_component_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


