# CodingComponent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**system** | **str** |  | [optional] 
**code** | **str** |  | [optional] 
**display** | **str** |  | [optional] 

## Example

```python
from snowstorm_client.models.coding_component import CodingComponent

# TODO update the JSON string below
json = "{}"
# create an instance of CodingComponent from a JSON string
coding_component_instance = CodingComponent.from_json(json)
# print the JSON string representation of the object
print(CodingComponent.to_json())

# convert the object into a dict
coding_component_dict = coding_component_instance.to_dict()
# create an instance of CodingComponent from a dict
coding_component_from_dict = CodingComponent.from_dict(coding_component_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


