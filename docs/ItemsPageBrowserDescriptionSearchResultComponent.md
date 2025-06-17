# ItemsPageBrowserDescriptionSearchResultComponent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[BrowserDescriptionSearchResultComponent]**](BrowserDescriptionSearchResultComponent.md) |  | [optional] 
**total** | **int** |  | [optional] 
**limit** | **int** |  | [optional] 
**offset** | **int** |  | [optional] 
**search_after** | **str** |  | [optional] 
**search_after_array** | **List[object]** |  | [optional] 

## Example

```python
from snowstorm_client.models.items_page_browser_description_search_result_component import ItemsPageBrowserDescriptionSearchResultComponent

# TODO update the JSON string below
json = "{}"
# create an instance of ItemsPageBrowserDescriptionSearchResultComponent from a JSON string
items_page_browser_description_search_result_component_instance = ItemsPageBrowserDescriptionSearchResultComponent.from_json(json)
# print the JSON string representation of the object
print(ItemsPageBrowserDescriptionSearchResultComponent.to_json())

# convert the object into a dict
items_page_browser_description_search_result_component_dict = items_page_browser_description_search_result_component_instance.to_dict()
# create an instance of ItemsPageBrowserDescriptionSearchResultComponent from a dict
items_page_browser_description_search_result_component_from_dict = ItemsPageBrowserDescriptionSearchResultComponent.from_dict(items_page_browser_description_search_result_component_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


