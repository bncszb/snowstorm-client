# BrowserDescriptionSearchResultComponent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**term** | **str** |  | [optional] 
**active** | **bool** |  | [optional] 
**language_code** | **str** |  | [optional] 
**module** | **str** |  | [optional] 
**concept** | [**ConceptMiniComponent**](ConceptMiniComponent.md) |  | [optional] 

## Example

```python
from snowstorm_client.models.browser_description_search_result_component import BrowserDescriptionSearchResultComponent

# TODO update the JSON string below
json = "{}"
# create an instance of BrowserDescriptionSearchResultComponent from a JSON string
browser_description_search_result_component_instance = BrowserDescriptionSearchResultComponent.from_json(json)
# print the JSON string representation of the object
print(BrowserDescriptionSearchResultComponent.to_json())

# convert the object into a dict
browser_description_search_result_component_dict = browser_description_search_result_component_instance.to_dict()
# create an instance of BrowserDescriptionSearchResultComponent from a dict
browser_description_search_result_component_from_dict = BrowserDescriptionSearchResultComponent.from_dict(browser_description_search_result_component_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


