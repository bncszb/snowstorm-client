# Description


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
**language_refset_members** | [**Description**](Description.md) |  | [optional] 
**acceptability_map_from_lang_refset_members** | **Dict[str, str]** |  | [optional] 
**case_significance** | **str** |  | [optional] 
**effective_time** | **str** |  | [optional] 

## Example

```python
from snowstorm_client.models.description import Description

# TODO update the JSON string below
json = "{}"
# create an instance of Description from a JSON string
description_instance = Description.from_json(json)
# print the JSON string representation of the object
print(Description.to_json())

# convert the object into a dict
description_dict = description_instance.to_dict()
# create an instance of Description from a dict
description_from_dict = Description.from_dict(description_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


