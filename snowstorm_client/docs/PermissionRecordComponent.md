# PermissionRecordComponent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**role** | **str** |  | [optional] 
**path** | **str** |  | [optional] 
**var_global** | **bool** |  | [optional] 
**user_groups** | **List[str]** |  | [optional] 

## Example

```python
from snowstorm_client.models.permission_record_component import PermissionRecordComponent

# TODO update the JSON string below
json = "{}"
# create an instance of PermissionRecordComponent from a JSON string
permission_record_component_instance = PermissionRecordComponent.from_json(json)
# print the JSON string representation of the object
print(PermissionRecordComponent.to_json())

# convert the object into a dict
permission_record_component_dict = permission_record_component_instance.to_dict()
# create an instance of PermissionRecordComponent from a dict
permission_record_component_from_dict = PermissionRecordComponent.from_dict(permission_record_component_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


