# BranchPojo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**path** | **str** |  | [optional] 
**state** | **str** |  | [optional] 
**contains_content** | **bool** |  | [optional] 
**locked** | **bool** |  | [optional] 
**creation** | **datetime** |  | [optional] 
**base** | **datetime** |  | [optional] 
**head** | **datetime** |  | [optional] 
**creation_timestamp** | **int** |  | [optional] 
**base_timestamp** | **int** |  | [optional] 
**head_timestamp** | **int** |  | [optional] 
**user_roles** | **List[str]** |  | [optional] 
**global_user_roles** | **List[str]** |  | [optional] 
**versions_replaced_counts** | **Dict[str, int]** |  | [optional] 
**metadata** | **Dict[str, object]** |  | [optional] 
**versions_replaced** | **Dict[str, List[str]]** |  | [optional] 

## Example

```python
from snowstorm_client.models.branch_pojo import BranchPojo

# TODO update the JSON string below
json = "{}"
# create an instance of BranchPojo from a JSON string
branch_pojo_instance = BranchPojo.from_json(json)
# print the JSON string representation of the object
print(BranchPojo.to_json())

# convert the object into a dict
branch_pojo_dict = branch_pojo_instance.to_dict()
# create an instance of BranchPojo from a dict
branch_pojo_from_dict = BranchPojo.from_dict(branch_pojo_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


