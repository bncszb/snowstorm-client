# ConceptComponent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**concept_id** | **str** |  | [optional] 
**descendant_count** | **int** |  | [optional] 
**fsn** | [**TermLangPojoComponent**](TermLangPojoComponent.md) |  | [optional] 
**pt** | [**TermLangPojoComponent**](TermLangPojoComponent.md) |  | [optional] 
**active** | **bool** |  | [optional] 
**effective_time** | **str** |  | [optional] 
**released** | **bool** |  | [optional] 
**released_effective_time** | **int** |  | [optional] 
**inactivation_indicator** | **str** |  | [optional] 
**association_targets** | **Dict[str, List[str]]** |  | [optional] 
**module_id** | **str** |  | [optional] 
**definition_status** | **str** |  | [optional] 
**definition_status_id** | **str** |  | 
**descriptions** | [**List[DescriptionComponent]**](DescriptionComponent.md) |  | [optional] 
**annotations** | [**List[AnnotationComponent]**](AnnotationComponent.md) |  | [optional] 
**class_axioms** | [**List[AxiomComponent]**](AxiomComponent.md) |  | [optional] 
**gci_axioms** | [**List[AxiomComponent]**](AxiomComponent.md) |  | [optional] 
**relationships** | [**List[RelationshipComponent]**](RelationshipComponent.md) |  | [optional] 
**alternate_identifiers** | [**List[IdentifierComponent]**](IdentifierComponent.md) |  | [optional] 
**validation_results** | [**List[InvalidContentComponent]**](InvalidContentComponent.md) |  | [optional] 
**internal_id** | **str** |  | [optional] 
**path** | **str** |  | [optional] 
**start** | **datetime** |  | [optional] 
**end** | **datetime** |  | [optional] 
**deleted** | **bool** |  | [optional] 
**changed** | **bool** |  | [optional] 
**effective_time_i** | **int** |  | [optional] 
**release_hash** | **str** |  | [optional] 
**primitive** | **bool** |  | [optional] 
**active_descriptions** | [**List[DescriptionComponent]**](DescriptionComponent.md) |  | [optional] 
**all_owl_axiom_members** | [**List[ReferenceSetMemberComponent]**](ReferenceSetMemberComponent.md) |  | [optional] 
**all_annotation_members** | [**List[ReferenceSetMemberComponent]**](ReferenceSetMemberComponent.md) |  | [optional] 
**active_inferred_relationships** | [**List[RelationshipComponent]**](RelationshipComponent.md) |  | [optional] 

## Example

```python
from snowstorm_client.models.concept_component import ConceptComponent

# TODO update the JSON string below
json = "{}"
# create an instance of ConceptComponent from a JSON string
concept_component_instance = ConceptComponent.from_json(json)
# print the JSON string representation of the object
print(ConceptComponent.to_json())

# convert the object into a dict
concept_component_dict = concept_component_instance.to_dict()
# create an instance of ConceptComponent from a dict
concept_component_from_dict = ConceptComponent.from_dict(concept_component_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


