# InvalidContentComponent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rule_id** | **str** |  | [optional] 
**concept_id** | **str** |  | [optional] 
**concept_fsn** | **str** |  | [optional] 
**component** | [**ComponentComponent**](ComponentComponent.md) |  | [optional] 
**message** | **str** |  | [optional] 
**severity** | **str** |  | [optional] 
**ignore_published_check** | **bool** |  | [optional] 
**published** | **bool** |  | [optional] 
**component_id** | **str** |  | [optional] 

## Example

```python
from snowstorm_client.models.invalid_content_component import InvalidContentComponent

# TODO update the JSON string below
json = "{}"
# create an instance of InvalidContentComponent from a JSON string
invalid_content_component_instance = InvalidContentComponent.from_json(json)
# print the JSON string representation of the object
print(InvalidContentComponent.to_json())

# convert the object into a dict
invalid_content_component_dict = invalid_content_component_instance.to_dict()
# create an instance of InvalidContentComponent from a dict
invalid_content_component_from_dict = InvalidContentComponent.from_dict(invalid_content_component_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


