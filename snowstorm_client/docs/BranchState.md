# BranchState


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**path** | **str** |  | [optional] 
**base_timestamp** | **int** |  | [optional] 
**head_timestamp** | **int** |  | [optional] 

## Example

```python
from snowstorm_client.models.branch_state import BranchState

# TODO update the JSON string below
json = "{}"
# create an instance of BranchState from a JSON string
branch_state_instance = BranchState.from_json(json)
# print the JSON string representation of the object
print(BranchState.to_json())

# convert the object into a dict
branch_state_dict = branch_state_instance.to_dict()
# create an instance of BranchState from a dict
branch_state_from_dict = BranchState.from_dict(branch_state_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


