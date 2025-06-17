# MergeReviewConceptVersions


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source_concept** | [**Concept**](Concept.md) |  | [optional] 
**target_concept** | [**Concept**](Concept.md) |  | [optional] 
**auto_merged_concept** | [**Concept**](Concept.md) |  | [optional] 
**manually_merged_concept** | [**Concept**](Concept.md) |  | [optional] 
**target_concept_version_behind** | **bool** |  | [optional] 

## Example

```python
from snowstorm_client.models.merge_review_concept_versions import MergeReviewConceptVersions

# TODO update the JSON string below
json = "{}"
# create an instance of MergeReviewConceptVersions from a JSON string
merge_review_concept_versions_instance = MergeReviewConceptVersions.from_json(json)
# print the JSON string representation of the object
print(MergeReviewConceptVersions.to_json())

# convert the object into a dict
merge_review_concept_versions_dict = merge_review_concept_versions_instance.to_dict()
# create an instance of MergeReviewConceptVersions from a dict
merge_review_concept_versions_from_dict = MergeReviewConceptVersions.from_dict(merge_review_concept_versions_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


