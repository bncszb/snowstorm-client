# RelationshipChange


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**internal_id** | **str** |  | [optional] 
**classification_id** | **str** |  | [optional] 
**relationship_id** | **str** |  | [optional] 
**active** | **bool** |  | [optional] 
**source_id** | **str** |  | [optional] 
**destination_id** | **str** |  | [optional] 
**value** | **str** |  | [optional] 
**group** | **int** |  | [optional] 
**type_id** | **str** |  | [optional] 
**modifier_id** | **str** |  | [optional] 
**inferred_not_stated** | **bool** |  | [optional] 
**source** | [**ConceptMini**](ConceptMini.md) |  | [optional] 
**destination** | [**ConceptMini**](ConceptMini.md) |  | [optional] 
**type** | [**ConceptMini**](ConceptMini.md) |  | [optional] 
**concrete** | **bool** |  | [optional] 
**change_nature** | **str** |  | [optional] 
**destination_or_value** | **str** |  | [optional] 
**characteristic_type_id** | **str** |  | [optional] 
**destination_or_value_without_prefix** | **str** |  | [optional] 
**destination_or_raw_value** | **object** |  | [optional] 
**source_fsn** | **str** |  | [optional] 
**type_fsn** | **str** |  | [optional] 
**destination_fsn** | **str** |  | [optional] 
**union_group** | **int** |  | [optional] 

## Example

```python
from snowstorm_client.models.relationship_change import RelationshipChange

# TODO update the JSON string below
json = "{}"
# create an instance of RelationshipChange from a JSON string
relationship_change_instance = RelationshipChange.from_json(json)
# print the JSON string representation of the object
print(RelationshipChange.to_json())

# convert the object into a dict
relationship_change_dict = relationship_change_instance.to_dict()
# create an instance of RelationshipChange from a dict
relationship_change_from_dict = RelationshipChange.from_dict(relationship_change_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


