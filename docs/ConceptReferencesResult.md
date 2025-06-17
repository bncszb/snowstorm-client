# ConceptReferencesResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total** | **int** |  | [optional] 
**limit** | **int** |  | [optional] 
**offset** | **int** |  | [optional] 
**references_by_type** | [**List[TypeReferences]**](TypeReferences.md) |  | [optional] 

## Example

```python
from snowstorm_client.models.concept_references_result import ConceptReferencesResult

# TODO update the JSON string below
json = "{}"
# create an instance of ConceptReferencesResult from a JSON string
concept_references_result_instance = ConceptReferencesResult.from_json(json)
# print the JSON string representation of the object
print(ConceptReferencesResult.to_json())

# convert the object into a dict
concept_references_result_dict = concept_references_result_instance.to_dict()
# create an instance of ConceptReferencesResult from a dict
concept_references_result_from_dict = ConceptReferencesResult.from_dict(concept_references_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


