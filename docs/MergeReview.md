# MergeReview


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**source_path** | **str** |  | [optional] 
**target_path** | **str** |  | [optional] 
**source_to_target_review_id** | **str** |  | [optional] 
**target_to_source_review_id** | **str** |  | [optional] 
**status** | **str** |  | [optional] 
**message** | **str** |  | [optional] 
**created** | **datetime** |  | [optional] 

## Example

```python
from snowstorm_client.models.merge_review import MergeReview

# TODO update the JSON string below
json = "{}"
# create an instance of MergeReview from a JSON string
merge_review_instance = MergeReview.from_json(json)
# print the JSON string representation of the object
print(MergeReview.to_json())

# convert the object into a dict
merge_review_dict = merge_review_instance.to_dict()
# create an instance of MergeReview from a dict
merge_review_from_dict = MergeReview.from_dict(merge_review_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


