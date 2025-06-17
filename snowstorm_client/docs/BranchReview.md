# BranchReview


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**last_updated** | **datetime** |  | [optional] 
**status** | **str** |  | [optional] 
**source** | [**BranchState**](BranchState.md) |  | [optional] 
**target** | [**BranchState**](BranchState.md) |  | [optional] 
**changed_concepts** | **List[int]** |  | [optional] 
**source_parent** | **bool** |  | [optional] 

## Example

```python
from snowstorm_client.models.branch_review import BranchReview

# TODO update the JSON string below
json = "{}"
# create an instance of BranchReview from a JSON string
branch_review_instance = BranchReview.from_json(json)
# print the JSON string representation of the object
print(BranchReview.to_json())

# convert the object into a dict
branch_review_dict = branch_review_instance.to_dict()
# create an instance of BranchReview from a dict
branch_review_from_dict = BranchReview.from_dict(branch_review_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


