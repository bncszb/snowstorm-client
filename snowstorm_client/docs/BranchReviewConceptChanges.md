# BranchReviewConceptChanges


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**changed_concepts** | **List[int]** |  | [optional] 

## Example

```python
from snowstorm_client.models.branch_review_concept_changes import BranchReviewConceptChanges

# TODO update the JSON string below
json = "{}"
# create an instance of BranchReviewConceptChanges from a JSON string
branch_review_concept_changes_instance = BranchReviewConceptChanges.from_json(json)
# print the JSON string representation of the object
print(BranchReviewConceptChanges.to_json())

# convert the object into a dict
branch_review_concept_changes_dict = branch_review_concept_changes_instance.to_dict()
# create an instance of BranchReviewConceptChanges from a dict
branch_review_concept_changes_from_dict = BranchReviewConceptChanges.from_dict(branch_review_concept_changes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


