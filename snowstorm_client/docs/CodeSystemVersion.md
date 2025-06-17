# CodeSystemVersion


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**short_name** | **str** |  | [optional] 
**import_date** | **datetime** |  | [optional] 
**parent_branch_path** | **str** |  | [optional] 
**effective_date** | **int** |  | [optional] 
**version** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**release_package** | **str** |  | [optional] 
**dependant_version_effective_time** | **int** |  | [optional] 
**code_system** | [**CodeSystem**](CodeSystem.md) |  | [optional] 
**branch_path** | **str** |  | [optional] 

## Example

```python
from snowstorm_client.models.code_system_version import CodeSystemVersion

# TODO update the JSON string below
json = "{}"
# create an instance of CodeSystemVersion from a JSON string
code_system_version_instance = CodeSystemVersion.from_json(json)
# print the JSON string representation of the object
print(CodeSystemVersion.to_json())

# convert the object into a dict
code_system_version_dict = code_system_version_instance.to_dict()
# create an instance of CodeSystemVersion from a dict
code_system_version_from_dict = CodeSystemVersion.from_dict(code_system_version_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


