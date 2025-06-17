# Classification


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**path** | **str** |  | [optional] 
**status** | **str** |  | [optional] 
**error_message** | **str** |  | [optional] 
**reasoner_id** | **str** |  | [optional] 
**user_id** | **str** |  | [optional] 
**creation_date** | **datetime** |  | [optional] 
**completion_date** | **datetime** |  | [optional] 
**last_commit_date** | **datetime** |  | [optional] 
**save_date** | **datetime** |  | [optional] 
**inferred_relationship_changes_found** | **bool** |  | [optional] 
**redundant_stated_relationships_found** | **bool** |  | [optional] 
**equivalent_concepts_found** | **bool** |  | [optional] 

## Example

```python
from snowstorm_client.models.classification import Classification

# TODO update the JSON string below
json = "{}"
# create an instance of Classification from a JSON string
classification_instance = Classification.from_json(json)
# print the JSON string representation of the object
print(Classification.to_json())

# convert the object into a dict
classification_dict = classification_instance.to_dict()
# create an instance of Classification from a dict
classification_from_dict = Classification.from_dict(classification_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


