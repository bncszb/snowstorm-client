# ItemsPageRelationshipChange


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[RelationshipChange]**](RelationshipChange.md) |  | [optional] 
**total** | **int** |  | [optional] 
**limit** | **int** |  | [optional] 
**offset** | **int** |  | [optional] 
**search_after** | **str** |  | [optional] 
**search_after_array** | **List[object]** |  | [optional] 

## Example

```python
from snowstorm_client.models.items_page_relationship_change import ItemsPageRelationshipChange

# TODO update the JSON string below
json = "{}"
# create an instance of ItemsPageRelationshipChange from a JSON string
items_page_relationship_change_instance = ItemsPageRelationshipChange.from_json(json)
# print the JSON string representation of the object
print(ItemsPageRelationshipChange.to_json())

# convert the object into a dict
items_page_relationship_change_dict = items_page_relationship_change_instance.to_dict()
# create an instance of ItemsPageRelationshipChange from a dict
items_page_relationship_change_from_dict = ItemsPageRelationshipChange.from_dict(items_page_relationship_change_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


