# ItemsPageCodeSystem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[CodeSystem]**](CodeSystem.md) |  | [optional] 
**total** | **int** |  | [optional] 
**limit** | **int** |  | [optional] 
**offset** | **int** |  | [optional] 
**search_after** | **str** |  | [optional] 
**search_after_array** | **List[object]** |  | [optional] 

## Example

```python
from snowstorm_client.models.items_page_code_system import ItemsPageCodeSystem

# TODO update the JSON string below
json = "{}"
# create an instance of ItemsPageCodeSystem from a JSON string
items_page_code_system_instance = ItemsPageCodeSystem.from_json(json)
# print the JSON string representation of the object
print(ItemsPageCodeSystem.to_json())

# convert the object into a dict
items_page_code_system_dict = items_page_code_system_instance.to_dict()
# create an instance of ItemsPageCodeSystem from a dict
items_page_code_system_from_dict = ItemsPageCodeSystem.from_dict(items_page_code_system_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


