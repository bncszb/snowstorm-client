# ConceptMicro


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**primitive** | **bool** |  | [optional] 
**term** | **str** |  | [optional] 

## Example

```python
from snowstorm_client.models.concept_micro import ConceptMicro

# TODO update the JSON string below
json = "{}"
# create an instance of ConceptMicro from a JSON string
concept_micro_instance = ConceptMicro.from_json(json)
# print the JSON string representation of the object
print(ConceptMicro.to_json())

# convert the object into a dict
concept_micro_dict = concept_micro_instance.to_dict()
# create an instance of ConceptMicro from a dict
concept_micro_from_dict = ConceptMicro.from_dict(concept_micro_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


