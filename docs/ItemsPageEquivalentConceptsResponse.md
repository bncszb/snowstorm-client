# ItemsPageEquivalentConceptsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[EquivalentConceptsResponse]**](EquivalentConceptsResponse.md) |  | [optional] 
**total** | **int** |  | [optional] 
**limit** | **int** |  | [optional] 
**offset** | **int** |  | [optional] 
**search_after** | **str** |  | [optional] 
**search_after_array** | **List[object]** |  | [optional] 

## Example

```python
from snowstorm_client.models.items_page_equivalent_concepts_response import ItemsPageEquivalentConceptsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ItemsPageEquivalentConceptsResponse from a JSON string
items_page_equivalent_concepts_response_instance = ItemsPageEquivalentConceptsResponse.from_json(json)
# print the JSON string representation of the object
print(ItemsPageEquivalentConceptsResponse.to_json())

# convert the object into a dict
items_page_equivalent_concepts_response_dict = items_page_equivalent_concepts_response_instance.to_dict()
# create an instance of ItemsPageEquivalentConceptsResponse from a dict
items_page_equivalent_concepts_response_from_dict = ItemsPageEquivalentConceptsResponse.from_dict(items_page_equivalent_concepts_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


