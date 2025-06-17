# AsyncConceptChangeBatch


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**start_time** | **datetime** |  | [optional] 
**status** | **str** |  | [optional] 
**concept_ids** | **List[int]** |  | [optional] 
**end_time** | **datetime** |  | [optional] 
**message** | **str** |  | [optional] 
**seconds_duration** | **float** |  | [optional] 

## Example

```python
from snowstorm_client.models.async_concept_change_batch import AsyncConceptChangeBatch

# TODO update the JSON string below
json = "{}"
# create an instance of AsyncConceptChangeBatch from a JSON string
async_concept_change_batch_instance = AsyncConceptChangeBatch.from_json(json)
# print the JSON string representation of the object
print(AsyncConceptChangeBatch.to_json())

# convert the object into a dict
async_concept_change_batch_dict = async_concept_change_batch_instance.to_dict()
# create an instance of AsyncConceptChangeBatch from a dict
async_concept_change_batch_from_dict = AsyncConceptChangeBatch.from_dict(async_concept_change_batch_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


