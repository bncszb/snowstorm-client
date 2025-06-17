# CodeSystem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**owner** | **str** |  | [optional] 
**short_name** | **str** |  | 
**branch_path** | **str** |  | 
**dependant_version_effective_time** | **int** |  | [optional] 
**daily_build_available** | **bool** |  | [optional] 
**latest_daily_build** | **str** |  | [optional] 
**country_code** | **str** |  | [optional] 
**default_language_code** | **str** |  | [optional] 
**default_language_reference_sets** | **List[str]** |  | [optional] 
**maintainer_type** | **str** |  | [optional] 
**latest_version** | [**CodeSystemVersion**](CodeSystemVersion.md) |  | [optional] 
**languages** | **Dict[str, str]** |  | [optional] 
**modules** | [**List[ConceptMini]**](ConceptMini.md) |  | [optional] 
**user_roles** | **List[str]** |  | [optional] 

## Example

```python
from snowstorm_client.models.code_system import CodeSystem

# TODO update the JSON string below
json = "{}"
# create an instance of CodeSystem from a JSON string
code_system_instance = CodeSystem.from_json(json)
# print the JSON string representation of the object
print(CodeSystem.to_json())

# convert the object into a dict
code_system_dict = code_system_instance.to_dict()
# create an instance of CodeSystem from a dict
code_system_from_dict = CodeSystem.from_dict(code_system_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


