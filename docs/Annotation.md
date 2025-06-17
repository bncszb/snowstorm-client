# Annotation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**internal_id** | **str** |  | [optional] 
**path** | **str** |  | [optional] 
**start** | **datetime** |  | [optional] 
**end** | **datetime** |  | [optional] 
**deleted** | **bool** |  | [optional] 
**changed** | **bool** |  | [optional] 
**active** | **bool** |  | [optional] 
**module_id** | **str** |  | [optional] 
**effective_time_i** | **int** |  | [optional] 
**released** | **bool** |  | [optional] 
**release_hash** | **str** |  | [optional] 
**released_effective_time** | **int** |  | [optional] 
**member_id** | **str** |  | [optional] 
**refset_id** | **str** |  | 
**referenced_component_id** | **str** |  | 
**concept_id** | **str** |  | [optional] 
**additional_fields** | **Dict[str, str]** |  | [optional] 
**referenced_component_snomed_component** | [**SnomedComponentObject**](SnomedComponentObject.md) |  | [optional] 
**map_target_coding** | [**Coding**](Coding.md) |  | [optional] 
**annotation_id** | **str** |  | [optional] 
**type_id** | **str** |  | [optional] 
**value** | **str** |  | [optional] 
**language_dialect_code** | **str** |  | [optional] 
**type_pt** | [**TermLangPojo**](TermLangPojo.md) |  | [optional] 
**effective_time** | **str** |  | [optional] 
**map_group** | **str** |  | [optional] 
**map_priority** | **str** |  | [optional] 
**referenced_component** | **object** |  | [optional] 

## Example

```python
from snowstorm_client.models.annotation import Annotation

# TODO update the JSON string below
json = "{}"
# create an instance of Annotation from a JSON string
annotation_instance = Annotation.from_json(json)
# print the JSON string representation of the object
print(Annotation.to_json())

# convert the object into a dict
annotation_dict = annotation_instance.to_dict()
# create an instance of Annotation from a dict
annotation_from_dict = Annotation.from_dict(annotation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


