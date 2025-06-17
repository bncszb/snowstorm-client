# EquivalentConceptsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**equivalent_concepts** | [**ItemsPageConceptMini**](ItemsPageConceptMini.md) |  | [optional] 

## Example

```python
from snowstorm_client.models.equivalent_concepts_response import EquivalentConceptsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of EquivalentConceptsResponse from a JSON string
equivalent_concepts_response_instance = EquivalentConceptsResponse.from_json(json)
# print the JSON string representation of the object
print(EquivalentConceptsResponse.to_json())

# convert the object into a dict
equivalent_concepts_response_dict = equivalent_concepts_response_instance.to_dict()
# create an instance of EquivalentConceptsResponse from a dict
equivalent_concepts_response_from_dict = EquivalentConceptsResponse.from_dict(equivalent_concepts_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


