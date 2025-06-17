# RefSetMemberPageWithBucketAggregationsReferenceSetMember


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**content** | [**List[ReferenceSetMember]**](ReferenceSetMember.md) |  | [optional] 
**pageable** | [**PageableObject**](PageableObject.md) |  | [optional] 
**member_counts_by_reference_set** | **Dict[str, int]** |  | [optional] 
**reference_sets** | [**Dict[str, ConceptMini]**](ConceptMini.md) |  | [optional] 
**search_after_array** | **List[object]** |  | [optional] 
**search_after** | **str** |  | [optional] 
**last** | **bool** |  | [optional] 
**total_elements** | **int** |  | [optional] 
**total_pages** | **int** |  | [optional] 
**size** | **int** |  | [optional] 
**number** | **int** |  | [optional] 
**sort** | [**List[SortObject]**](SortObject.md) |  | [optional] 
**first** | **bool** |  | [optional] 
**number_of_elements** | **int** |  | [optional] 
**empty** | **bool** |  | [optional] 

## Example

```python
from snowstorm_client.models.ref_set_member_page_with_bucket_aggregations_reference_set_member import RefSetMemberPageWithBucketAggregationsReferenceSetMember

# TODO update the JSON string below
json = "{}"
# create an instance of RefSetMemberPageWithBucketAggregationsReferenceSetMember from a JSON string
ref_set_member_page_with_bucket_aggregations_reference_set_member_instance = RefSetMemberPageWithBucketAggregationsReferenceSetMember.from_json(json)
# print the JSON string representation of the object
print(RefSetMemberPageWithBucketAggregationsReferenceSetMember.to_json())

# convert the object into a dict
ref_set_member_page_with_bucket_aggregations_reference_set_member_dict = ref_set_member_page_with_bucket_aggregations_reference_set_member_instance.to_dict()
# create an instance of RefSetMemberPageWithBucketAggregationsReferenceSetMember from a dict
ref_set_member_page_with_bucket_aggregations_reference_set_member_from_dict = RefSetMemberPageWithBucketAggregationsReferenceSetMember.from_dict(ref_set_member_page_with_bucket_aggregations_reference_set_member_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


