# ConceptMini


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**concept_id** | **str** |  | [optional] 
**active** | **bool** |  | [optional] 
**definition_status** | **str** |  | [optional] 
**module_id** | **str** |  | [optional] 
**effective_time** | **str** |  | [optional] 
**fsn** | [**TermLangPojo**](TermLangPojo.md) |  | [optional] 
**pt** | [**TermLangPojo**](TermLangPojo.md) |  | [optional] 
**descendant_count** | **int** |  | [optional] 
**is_leaf_inferred** | **bool** |  | [optional] 
**is_leaf_stated** | **bool** |  | [optional] 
**id** | **str** |  | [optional] 
**definition_status_id** | **str** |  | [optional] 
**leaf_inferred** | [**ConceptMini**](ConceptMini.md) |  | [optional] 
**leaf_stated** | [**ConceptMini**](ConceptMini.md) |  | [optional] 
**extra_fields** | **Dict[str, object]** |  | [optional] 
**id_and_fsn_term** | **str** |  | [optional] 

## Example

```python
from snowstorm_client.models.concept_mini import ConceptMini

# TODO update the JSON string below
json = "{}"
# create an instance of ConceptMini from a JSON string
concept_mini_instance = ConceptMini.from_json(json)
# print the JSON string representation of the object
print(ConceptMini.to_json())

# convert the object into a dict
concept_mini_dict = concept_mini_instance.to_dict()
# create an instance of ConceptMini from a dict
concept_mini_from_dict = ConceptMini.from_dict(concept_mini_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


