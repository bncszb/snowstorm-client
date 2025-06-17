# TermLangPojo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**term** | **str** |  | [optional] 
**lang** | **str** |  | [optional] 

## Example

```python
from snowstorm_client.models.term_lang_pojo import TermLangPojo

# TODO update the JSON string below
json = "{}"
# create an instance of TermLangPojo from a JSON string
term_lang_pojo_instance = TermLangPojo.from_json(json)
# print the JSON string representation of the object
print(TermLangPojo.to_json())

# convert the object into a dict
term_lang_pojo_dict = term_lang_pojo_instance.to_dict()
# create an instance of TermLangPojo from a dict
term_lang_pojo_from_dict = TermLangPojo.from_dict(term_lang_pojo_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


