# Component


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**active** | **bool** |  | [optional] 
**released** | **bool** |  | [optional] 
**module_id** | **str** |  | [optional] 
**published** | **bool** |  | [optional] 

## Example

```python
from snowstorm_client.models.component import Component

# TODO update the JSON string below
json = "{}"
# create an instance of Component from a JSON string
component_instance = Component.from_json(json)
# print the JSON string representation of the object
print(Component.to_json())

# convert the object into a dict
component_dict = component_instance.to_dict()
# create an instance of Component from a dict
component_from_dict = Component.from_dict(component_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


