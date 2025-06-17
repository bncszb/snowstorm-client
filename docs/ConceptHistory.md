# ConceptHistory


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**concept_id** | **str** |  | [optional] 
**history** | [**List[ConceptHistoryItem]**](ConceptHistoryItem.md) |  | [optional] 

## Example

```python
from snowstorm_client.models.concept_history import ConceptHistory

# TODO update the JSON string below
json = "{}"
# create an instance of ConceptHistory from a JSON string
concept_history_instance = ConceptHistory.from_json(json)
# print the JSON string representation of the object
print(ConceptHistory.to_json())

# convert the object into a dict
concept_history_dict = concept_history_instance.to_dict()
# create an instance of ConceptHistory from a dict
concept_history_from_dict = ConceptHistory.from_dict(concept_history_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


