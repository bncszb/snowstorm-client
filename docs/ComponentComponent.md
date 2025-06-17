# ComponentComponent


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
from snowstorm_client.models.component_component import ComponentComponent

# TODO update the JSON string below
json = "{}"
# create an instance of ComponentComponent from a JSON string
component_component_instance = ComponentComponent.from_json(json)
# print the JSON string representation of the object
print(ComponentComponent.to_json())

# convert the object into a dict
component_component_dict = component_component_instance.to_dict()
# create an instance of ComponentComponent from a dict
component_component_from_dict = ComponentComponent.from_dict(component_component_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


