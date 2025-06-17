# DescriptionComponent


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
**description_id** | **str** |  | [optional] 
**term** | **str** |  | 
**term_folded** | **str** |  | [optional] 
**term_len** | **int** |  | [optional] 
**tag** | **str** |  | [optional] 
**concept_id** | **str** |  | [optional] 
**language_code** | **str** |  | 
**type_id** | **str** |  | 
**case_significance_id** | **str** |  | 
**acceptability_map** | **Dict[str, str]** |  | [optional] 
**type** | **str** |  | [optional] 
**lang** | **str** |  | [optional] 
**inactivation_indicator** | **str** |  | [optional] 
**association_targets** | **Dict[str, List[str]]** |  | [optional] 
**language_refset_members** | [**DescriptionComponent**](DescriptionComponent.md) |  | [optional] 
**acceptability_map_from_lang_refset_members** | **Dict[str, str]** |  | [optional] 
**case_significance** | **str** |  | [optional] 
**effective_time** | **str** |  | [optional] 

## Example

```python
from snowstorm_client.models.description_component import DescriptionComponent

# TODO update the JSON string below
json = "{}"
# create an instance of DescriptionComponent from a JSON string
description_component_instance = DescriptionComponent.from_json(json)
# print the JSON string representation of the object
print(DescriptionComponent.to_json())

# convert the object into a dict
description_component_dict = description_component_instance.to_dict()
# create an instance of DescriptionComponent from a dict
description_component_from_dict = DescriptionComponent.from_dict(description_component_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


