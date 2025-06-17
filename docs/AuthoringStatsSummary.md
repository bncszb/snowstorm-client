# AuthoringStatsSummary


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**new_concepts_count** | **int** |  | [optional] 
**inactivated_concepts_count** | **int** |  | [optional] 
**reactivated_concepts_count** | **int** |  | [optional] 
**changed_fsn_count** | **int** |  | [optional] 
**inactivated_synonyms_count** | **int** |  | [optional] 
**new_synonyms_for_existing_concepts_count** | **int** |  | [optional] 
**reactivated_synonyms_count** | **int** |  | [optional] 
**execution_time** | **datetime** |  | [optional] 
**title** | **str** |  | [optional] 

## Example

```python
from snowstorm_client.models.authoring_stats_summary import AuthoringStatsSummary

# TODO update the JSON string below
json = "{}"
# create an instance of AuthoringStatsSummary from a JSON string
authoring_stats_summary_instance = AuthoringStatsSummary.from_json(json)
# print the JSON string representation of the object
print(AuthoringStatsSummary.to_json())

# convert the object into a dict
authoring_stats_summary_dict = authoring_stats_summary_instance.to_dict()
# create an instance of AuthoringStatsSummary from a dict
authoring_stats_summary_from_dict = AuthoringStatsSummary.from_dict(authoring_stats_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


