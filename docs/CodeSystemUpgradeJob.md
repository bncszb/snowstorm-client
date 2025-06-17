# CodeSystemUpgradeJob


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**new_dependant_version** | **int** |  | [optional] 
**code_system_shortname** | **str** |  | [optional] 
**status** | **str** |  | [optional] 
**error_message** | **str** |  | [optional] 
**creation_timestamp** | **int** |  | [optional] 

## Example

```python
from snowstorm_client.models.code_system_upgrade_job import CodeSystemUpgradeJob

# TODO update the JSON string below
json = "{}"
# create an instance of CodeSystemUpgradeJob from a JSON string
code_system_upgrade_job_instance = CodeSystemUpgradeJob.from_json(json)
# print the JSON string representation of the object
print(CodeSystemUpgradeJob.to_json())

# convert the object into a dict
code_system_upgrade_job_dict = code_system_upgrade_job_instance.to_dict()
# create an instance of CodeSystemUpgradeJob from a dict
code_system_upgrade_job_from_dict = CodeSystemUpgradeJob.from_dict(code_system_upgrade_job_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


