# ItemsPageClassification


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[Classification]**](Classification.md) |  | [optional] 
**total** | **int** |  | [optional] 
**limit** | **int** |  | [optional] 
**offset** | **int** |  | [optional] 
**search_after** | **str** |  | [optional] 
**search_after_array** | **List[object]** |  | [optional] 

## Example

```python
from snowstorm_client.models.items_page_classification import ItemsPageClassification

# TODO update the JSON string below
json = "{}"
# create an instance of ItemsPageClassification from a JSON string
items_page_classification_instance = ItemsPageClassification.from_json(json)
# print the JSON string representation of the object
print(ItemsPageClassification.to_json())

# convert the object into a dict
items_page_classification_dict = items_page_classification_instance.to_dict()
# create an instance of ItemsPageClassification from a dict
items_page_classification_from_dict = ItemsPageClassification.from_dict(items_page_classification_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


