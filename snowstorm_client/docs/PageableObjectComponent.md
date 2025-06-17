# PageableObjectComponent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**offset** | **int** |  | [optional] 
**sort** | [**List[SortObject]**](SortObject.md) |  | [optional] 
**page_number** | **int** |  | [optional] 
**page_size** | **int** |  | [optional] 
**paged** | **bool** |  | [optional] 
**unpaged** | **bool** |  | [optional] 

## Example

```python
from snowstorm_client.models.pageable_object_component import PageableObjectComponent

# TODO update the JSON string below
json = "{}"
# create an instance of PageableObjectComponent from a JSON string
pageable_object_component_instance = PageableObjectComponent.from_json(json)
# print the JSON string representation of the object
print(PageableObjectComponent.to_json())

# convert the object into a dict
pageable_object_component_dict = pageable_object_component_instance.to_dict()
# create an instance of PageableObjectComponent from a dict
pageable_object_component_from_dict = PageableObjectComponent.from_dict(pageable_object_component_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


