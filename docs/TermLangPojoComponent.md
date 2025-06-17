# TermLangPojoComponent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**term** | **str** |  | [optional] 
**lang** | **str** |  | [optional] 

## Example

```python
from snowstorm_client.models.term_lang_pojo_component import TermLangPojoComponent

# TODO update the JSON string below
json = "{}"
# create an instance of TermLangPojoComponent from a JSON string
term_lang_pojo_component_instance = TermLangPojoComponent.from_json(json)
# print the JSON string representation of the object
print(TermLangPojoComponent.to_json())

# convert the object into a dict
term_lang_pojo_component_dict = term_lang_pojo_component_instance.to_dict()
# create an instance of TermLangPojoComponent from a dict
term_lang_pojo_component_from_dict = TermLangPojoComponent.from_dict(term_lang_pojo_component_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


