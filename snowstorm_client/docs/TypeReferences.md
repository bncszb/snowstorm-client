# TypeReferences


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reference_type** | [**ConceptMini**](ConceptMini.md) |  | [optional] 
**referencing_concepts** | [**List[ConceptMini]**](ConceptMini.md) |  | [optional] 

## Example

```python
from snowstorm_client.models.type_references import TypeReferences

# TODO update the JSON string below
json = "{}"
# create an instance of TypeReferences from a JSON string
type_references_instance = TypeReferences.from_json(json)
# print the JSON string representation of the object
print(TypeReferences.to_json())

# convert the object into a dict
type_references_dict = type_references_instance.to_dict()
# create an instance of TypeReferences from a dict
type_references_from_dict = TypeReferences.from_dict(type_references_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


