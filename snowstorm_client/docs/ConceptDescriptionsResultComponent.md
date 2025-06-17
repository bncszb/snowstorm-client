# ConceptDescriptionsResultComponent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**concept_descriptions** | [**List[DescriptionComponent]**](DescriptionComponent.md) |  | [optional] 

## Example

```python
from snowstorm_client.models.concept_descriptions_result_component import ConceptDescriptionsResultComponent

# TODO update the JSON string below
json = "{}"
# create an instance of ConceptDescriptionsResultComponent from a JSON string
concept_descriptions_result_component_instance = ConceptDescriptionsResultComponent.from_json(json)
# print the JSON string representation of the object
print(ConceptDescriptionsResultComponent.to_json())

# convert the object into a dict
concept_descriptions_result_component_dict = concept_descriptions_result_component_instance.to_dict()
# create an instance of ConceptDescriptionsResultComponent from a dict
concept_descriptions_result_component_from_dict = ConceptDescriptionsResultComponent.from_dict(concept_descriptions_result_component_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


