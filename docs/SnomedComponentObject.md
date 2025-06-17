# SnomedComponentObject


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
**effective_time** | **str** |  | [optional] 
**id** | **str** |  | [optional] 

## Example

```python
from snowstorm_client.models.snomed_component_object import SnomedComponentObject

# TODO update the JSON string below
json = "{}"
# create an instance of SnomedComponentObject from a JSON string
snomed_component_object_instance = SnomedComponentObject.from_json(json)
# print the JSON string representation of the object
print(SnomedComponentObject.to_json())

# convert the object into a dict
snomed_component_object_dict = snomed_component_object_instance.to_dict()
# create an instance of SnomedComponentObject from a dict
snomed_component_object_from_dict = SnomedComponentObject.from_dict(snomed_component_object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


