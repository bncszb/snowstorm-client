# Relationship


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
**concrete_value** | [**ConcreteValue**](ConcreteValue.md) |  | [optional] 
**relationship_group** | **int** |  | [optional] 
**type_id** | **str** |  | 
**characteristic_type_id** | **str** |  | 
**modifier_id** | **str** |  | 
**source** | [**ConceptMini**](ConceptMini.md) |  | [optional] 
**type** | [**ConceptMini**](ConceptMini.md) |  | [optional] 
**target** | [**ConceptMini**](ConceptMini.md) |  | [optional] 
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
from snowstorm_client.models.relationship import Relationship

# TODO update the JSON string below
json = "{}"
# create an instance of Relationship from a JSON string
relationship_instance = Relationship.from_json(json)
# print the JSON string representation of the object
print(Relationship.to_json())

# convert the object into a dict
relationship_dict = relationship_instance.to_dict()
# create an instance of Relationship from a dict
relationship_from_dict = Relationship.from_dict(relationship_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


