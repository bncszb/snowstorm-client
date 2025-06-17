# Identifier


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**alternate_identifier** | **str** |  | 
**effective_time** | **str** |  | [optional] 
**active** | **bool** |  | [optional] 
**module_id** | **str** |  | [optional] 
**identifier_scheme_id** | **str** |  | 
**identifier_scheme** | [**ConceptMini**](ConceptMini.md) |  | [optional] 
**referenced_component_id** | **str** |  | 
**released** | **bool** |  | [optional] 
**released_effective_time** | **int** |  | [optional] 
**internal_id** | **str** |  | [optional] 
**path** | **str** |  | [optional] 
**start** | **datetime** |  | [optional] 
**end** | **datetime** |  | [optional] 
**deleted** | **bool** |  | [optional] 
**changed** | **bool** |  | [optional] 
**effective_time_i** | **int** |  | [optional] 
**release_hash** | **str** |  | [optional] 
**referenced_component_snomed_component** | [**SnomedComponentObject**](SnomedComponentObject.md) |  | [optional] 
**id** | **str** |  | [optional] 
**referenced_component** | **object** |  | [optional] 

## Example

```python
from snowstorm_client.models.identifier import Identifier

# TODO update the JSON string below
json = "{}"
# create an instance of Identifier from a JSON string
identifier_instance = Identifier.from_json(json)
# print the JSON string representation of the object
print(Identifier.to_json())

# convert the object into a dict
identifier_dict = identifier_instance.to_dict()
# create an instance of Identifier from a dict
identifier_from_dict = Identifier.from_dict(identifier_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


