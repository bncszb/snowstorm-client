# PageBrowserDescriptionSearchResultComponent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_elements** | **int** |  | [optional] 
**total_pages** | **int** |  | [optional] 
**size** | **int** |  | [optional] 
**content** | [**List[BrowserDescriptionSearchResultComponent]**](BrowserDescriptionSearchResultComponent.md) |  | [optional] 
**number** | **int** |  | [optional] 
**sort** | [**List[SortObject]**](SortObject.md) |  | [optional] 
**first** | **bool** |  | [optional] 
**last** | **bool** |  | [optional] 
**number_of_elements** | **int** |  | [optional] 
**pageable** | [**PageableObjectComponent**](PageableObjectComponent.md) |  | [optional] 
**empty** | **bool** |  | [optional] 

## Example

```python
from snowstorm_client.models.page_browser_description_search_result_component import PageBrowserDescriptionSearchResultComponent

# TODO update the JSON string below
json = "{}"
# create an instance of PageBrowserDescriptionSearchResultComponent from a JSON string
page_browser_description_search_result_component_instance = PageBrowserDescriptionSearchResultComponent.from_json(json)
# print the JSON string representation of the object
print(PageBrowserDescriptionSearchResultComponent.to_json())

# convert the object into a dict
page_browser_description_search_result_component_dict = page_browser_description_search_result_component_instance.to_dict()
# create an instance of PageBrowserDescriptionSearchResultComponent from a dict
page_browser_description_search_result_component_from_dict = PageBrowserDescriptionSearchResultComponent.from_dict(page_browser_description_search_result_component_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


