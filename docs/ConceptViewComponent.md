# ConceptViewComponent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**annotations** | [**List[AnnotationComponent]**](AnnotationComponent.md) |  | [optional] 
**active** | **bool** |  | [optional] 
**concept_id** | **str** |  | [optional] 
**effective_time** | **str** |  | [optional] 
**pt** | [**TermLangPojoComponent**](TermLangPojoComponent.md) |  | [optional] 
**descriptions** | [**List[DescriptionComponent]**](DescriptionComponent.md) |  | [optional] 
**fsn** | [**TermLangPojoComponent**](TermLangPojoComponent.md) |  | [optional] 
**relationships** | [**List[RelationshipComponent]**](RelationshipComponent.md) |  | [optional] 
**definition_status_id** | **str** |  | [optional] 
**module_id** | **str** |  | [optional] 
**class_axioms** | [**List[AxiomComponent]**](AxiomComponent.md) |  | [optional] 
**gci_axioms** | [**List[AxiomComponent]**](AxiomComponent.md) |  | [optional] 
**identifiers** | [**List[IdentifierComponent]**](IdentifierComponent.md) |  | [optional] 
**validation_results** | [**List[InvalidContentComponent]**](InvalidContentComponent.md) |  | [optional] 

## Example

```python
from snowstorm_client.models.concept_view_component import ConceptViewComponent

# TODO update the JSON string below
json = "{}"
# create an instance of ConceptViewComponent from a JSON string
concept_view_component_instance = ConceptViewComponent.from_json(json)
# print the JSON string representation of the object
print(ConceptViewComponent.to_json())

# convert the object into a dict
concept_view_component_dict = concept_view_component_instance.to_dict()
# create an instance of ConceptViewComponent from a dict
concept_view_component_from_dict = ConceptViewComponent.from_dict(concept_view_component_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


