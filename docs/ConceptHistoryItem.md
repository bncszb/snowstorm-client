# ConceptHistoryItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**effective_time** | **str** |  | [optional] 
**branch** | **str** |  | [optional] 
**component_types** | **List[str]** |  | [optional] 

## Example

```python
from snowstorm_client.models.concept_history_item import ConceptHistoryItem

# TODO update the JSON string below
json = "{}"
# create an instance of ConceptHistoryItem from a JSON string
concept_history_item_instance = ConceptHistoryItem.from_json(json)
# print the JSON string representation of the object
print(ConceptHistoryItem.to_json())

# convert the object into a dict
concept_history_item_dict = concept_history_item_instance.to_dict()
# create an instance of ConceptHistoryItem from a dict
concept_history_item_from_dict = ConceptHistoryItem.from_dict(concept_history_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


