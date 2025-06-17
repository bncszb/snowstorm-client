# InvalidContent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rule_id** | **str** |  | [optional] 
**concept_id** | **str** |  | [optional] 
**concept_fsn** | **str** |  | [optional] 
**component** | [**Component**](Component.md) |  | [optional] 
**message** | **str** |  | [optional] 
**severity** | **str** |  | [optional] 
**ignore_published_check** | **bool** |  | [optional] 
**published** | **bool** |  | [optional] 
**component_id** | **str** |  | [optional] 

## Example

```python
from snowstorm_client.models.invalid_content import InvalidContent

# TODO update the JSON string below
json = "{}"
# create an instance of InvalidContent from a JSON string
invalid_content_instance = InvalidContent.from_json(json)
# print the JSON string representation of the object
print(InvalidContent.to_json())

# convert the object into a dict
invalid_content_dict = invalid_content_instance.to_dict()
# create an instance of InvalidContent from a dict
invalid_content_from_dict = InvalidContent.from_dict(invalid_content_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


