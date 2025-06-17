# AsyncRefsetMemberChangeBatch


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**start_time** | **datetime** |  | [optional] 
**status** | **str** |  | [optional] 
**member_ids** | **List[str]** |  | [optional] 
**end_time** | **datetime** |  | [optional] 
**message** | **str** |  | [optional] 
**seconds_duration** | **float** |  | [optional] 

## Example

```python
from snowstorm_client.models.async_refset_member_change_batch import AsyncRefsetMemberChangeBatch

# TODO update the JSON string below
json = "{}"
# create an instance of AsyncRefsetMemberChangeBatch from a JSON string
async_refset_member_change_batch_instance = AsyncRefsetMemberChangeBatch.from_json(json)
# print the JSON string representation of the object
print(AsyncRefsetMemberChangeBatch.to_json())

# convert the object into a dict
async_refset_member_change_batch_dict = async_refset_member_change_batch_instance.to_dict()
# create an instance of AsyncRefsetMemberChangeBatch from a dict
async_refset_member_change_batch_from_dict = AsyncRefsetMemberChangeBatch.from_dict(async_refset_member_change_batch_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


