# ImportJob


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | [optional] 
**error_message** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**branch_path** | **str** |  | [optional] 
**create_code_system_version** | **bool** |  | [optional] 
**patch_release_version** | **int** |  | [optional] 
**module_ids** | **List[str]** |  | [optional] 
**internal_release** | **bool** |  | [optional] 

## Example

```python
from snowstorm_client.models.import_job import ImportJob

# TODO update the JSON string below
json = "{}"
# create an instance of ImportJob from a JSON string
import_job_instance = ImportJob.from_json(json)
# print the JSON string representation of the object
print(ImportJob.to_json())

# convert the object into a dict
import_job_dict = import_job_instance.to_dict()
# create an instance of ImportJob from a dict
import_job_from_dict = ImportJob.from_dict(import_job_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


