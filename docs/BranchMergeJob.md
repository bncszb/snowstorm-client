# BranchMergeJob


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**source** | **str** |  | [optional] 
**target** | **str** |  | [optional] 
**scheduled_date** | **datetime** |  | [optional] 
**start_date** | **datetime** |  | [optional] 
**status** | **str** |  | [optional] 
**end_date** | **datetime** |  | [optional] 
**message** | **str** |  | [optional] 
**api_error** | [**ApiError**](ApiError.md) |  | [optional] 

## Example

```python
from snowstorm_client.models.branch_merge_job import BranchMergeJob

# TODO update the JSON string below
json = "{}"
# create an instance of BranchMergeJob from a JSON string
branch_merge_job_instance = BranchMergeJob.from_json(json)
# print the JSON string representation of the object
print(BranchMergeJob.to_json())

# convert the object into a dict
branch_merge_job_dict = branch_merge_job_instance.to_dict()
# create an instance of BranchMergeJob from a dict
branch_merge_job_from_dict = BranchMergeJob.from_dict(branch_merge_job_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


