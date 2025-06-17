# RelationshipComponent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**internal_id** | **str** |  | [optional] 
**path** | **str** |  | [optional] 
**start** | **datetime** |  | [optional] 
**end** | **datetime** |  | [optional] 
**deleted** | **bool** |  | [optional] 
**changed** | **bool** |  | [optional] 
**active** | **bool** |  | [optional] 
**module_id** | **str** |  | [optional] 
**effective_time_i** | **int** |  | [optional] 
**released** | **bool** |  | [optional] 
**release_hash** | **str** |  | [optional] 
**released_effective_time** | **int** |  | [optional] 
**relationship_id** | **str** |  | [optional] 
**source_id** | **str** |  | [optional] 
**destination_id** | **str** |  | [optional] 
**concrete_value** | [**ConcreteValueComponent**](ConcreteValueComponent.md) |  | [optional] 
**relationship_group** | **int** |  | [optional] 
**type_id** | **str** |  | 
**characteristic_type_id** | **str** |  | 
**modifier_id** | **str** |  | 
**source** | [**ConceptMiniComponent**](ConceptMiniComponent.md) |  | [optional] 
**type** | [**ConceptMiniComponent**](ConceptMiniComponent.md) |  | [optional] 
**target** | [**ConceptMiniComponent**](ConceptMiniComponent.md) |  | [optional] 
**concrete** | **bool** |  | [optional] 
**group_id** | **int** |  | [optional] 
**grouped** | **bool** |  | [optional] 
**inferred** | **bool** |  | [optional] 
**modifier** | **str** |  | [optional] 
**relationship_id_as_long** | **int** |  | [optional] 
**characteristic_type** | **str** |  | [optional] 
**effective_time** | **str** |  | [optional] 
**id** | **str** |  | [optional] 

## Example

```python
from snowstorm_client.models.relationship_component import RelationshipComponent

# TODO update the JSON string below
json = "{}"
# create an instance of RelationshipComponent from a JSON string
relationship_component_instance = RelationshipComponent.from_json(json)
# print the JSON string representation of the object
print(RelationshipComponent.to_json())

# convert the object into a dict
relationship_component_dict = relationship_component_instance.to_dict()
# create an instance of RelationshipComponent from a dict
relationship_component_from_dict = RelationshipComponent.from_dict(relationship_component_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


