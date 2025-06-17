# Concept


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**concept_id** | **str** |  | [optional] 
**descendant_count** | **int** |  | [optional] 
**fsn** | [**TermLangPojo**](TermLangPojo.md) |  | [optional] 
**pt** | [**TermLangPojo**](TermLangPojo.md) |  | [optional] 
**active** | **bool** |  | [optional] 
**effective_time** | **str** |  | [optional] 
**released** | **bool** |  | [optional] 
**released_effective_time** | **int** |  | [optional] 
**inactivation_indicator** | **str** |  | [optional] 
**association_targets** | **Dict[str, List[str]]** |  | [optional] 
**module_id** | **str** |  | [optional] 
**definition_status** | **str** |  | [optional] 
**definition_status_id** | **str** |  | 
**descriptions** | [**List[Description]**](Description.md) |  | [optional] 
**annotations** | [**List[Annotation]**](Annotation.md) |  | [optional] 
**class_axioms** | [**List[Axiom]**](Axiom.md) |  | [optional] 
**gci_axioms** | [**List[Axiom]**](Axiom.md) |  | [optional] 
**relationships** | [**List[Relationship]**](Relationship.md) |  | [optional] 
**alternate_identifiers** | [**List[Identifier]**](Identifier.md) |  | [optional] 
**validation_results** | [**List[InvalidContent]**](InvalidContent.md) |  | [optional] 
**internal_id** | **str** |  | [optional] 
**path** | **str** |  | [optional] 
**start** | **datetime** |  | [optional] 
**end** | **datetime** |  | [optional] 
**deleted** | **bool** |  | [optional] 
**changed** | **bool** |  | [optional] 
**effective_time_i** | **int** |  | [optional] 
**release_hash** | **str** |  | [optional] 
**primitive** | **bool** |  | [optional] 
**active_descriptions** | [**List[Description]**](Description.md) |  | [optional] 
**all_owl_axiom_members** | [**List[ReferenceSetMember]**](ReferenceSetMember.md) |  | [optional] 
**all_annotation_members** | [**List[ReferenceSetMember]**](ReferenceSetMember.md) |  | [optional] 
**active_inferred_relationships** | [**List[Relationship]**](Relationship.md) |  | [optional] 

## Example

```python
from snowstorm_client.models.concept import Concept

# TODO update the JSON string below
json = "{}"
# create an instance of Concept from a JSON string
concept_instance = Concept.from_json(json)
# print the JSON string representation of the object
print(Concept.to_json())

# convert the object into a dict
concept_dict = concept_instance.to_dict()
# create an instance of Concept from a dict
concept_from_dict = Concept.from_dict(concept_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


