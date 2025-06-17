# ConceptMiniComponent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**concept_id** | **str** |  | [optional] 
**active** | **bool** |  | [optional] 
**definition_status** | **str** |  | [optional] 
**module_id** | **str** |  | [optional] 
**effective_time** | **str** |  | [optional] 
**fsn** | [**TermLangPojoComponent**](TermLangPojoComponent.md) |  | [optional] 
**pt** | [**TermLangPojoComponent**](TermLangPojoComponent.md) |  | [optional] 
**descendant_count** | **int** |  | [optional] 
**is_leaf_inferred** | **bool** |  | [optional] 
**is_leaf_stated** | **bool** |  | [optional] 
**id** | **str** |  | [optional] 
**definition_status_id** | **str** |  | [optional] 
**leaf_inferred** | [**ConceptMiniComponent**](ConceptMiniComponent.md) |  | [optional] 
**leaf_stated** | [**ConceptMiniComponent**](ConceptMiniComponent.md) |  | [optional] 
**extra_fields** | **Dict[str, object]** |  | [optional] 
**id_and_fsn_term** | **str** |  | [optional] 

## Example

```python
from snowstorm_client.models.concept_mini_component import ConceptMiniComponent

# TODO update the JSON string below
json = "{}"
# create an instance of ConceptMiniComponent from a JSON string
concept_mini_component_instance = ConceptMiniComponent.from_json(json)
# print the JSON string representation of the object
print(ConceptMiniComponent.to_json())

# convert the object into a dict
concept_mini_component_dict = concept_mini_component_instance.to_dict()
# create an instance of ConceptMiniComponent from a dict
concept_mini_component_from_dict = ConceptMiniComponent.from_dict(concept_mini_component_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


