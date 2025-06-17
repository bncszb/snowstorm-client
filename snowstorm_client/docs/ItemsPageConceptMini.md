# ItemsPageConceptMini


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[ConceptMini]**](ConceptMini.md) |  | [optional] 
**total** | **int** |  | [optional] 
**limit** | **int** |  | [optional] 
**offset** | **int** |  | [optional] 
**search_after** | **str** |  | [optional] 
**search_after_array** | **List[object]** |  | [optional] 

## Example

```python
from snowstorm_client.models.items_page_concept_mini import ItemsPageConceptMini

# TODO update the JSON string below
json = "{}"
# create an instance of ItemsPageConceptMini from a JSON string
items_page_concept_mini_instance = ItemsPageConceptMini.from_json(json)
# print the JSON string representation of the object
print(ItemsPageConceptMini.to_json())

# convert the object into a dict
items_page_concept_mini_dict = items_page_concept_mini_instance.to_dict()
# create an instance of ItemsPageConceptMini from a dict
items_page_concept_mini_from_dict = ItemsPageConceptMini.from_dict(items_page_concept_mini_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


