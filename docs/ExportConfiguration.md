# ExportConfiguration


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**start_date** | **datetime** |  | [optional] 
**branch_path** | **str** |  | 
**type** | **str** |  | [default to 'DELTA']
**filename_effective_date** | **str** |  | [optional] 
**concepts_and_relationships_only** | **bool** |  | [optional] [default to False]
**unpromoted_changes_only** | **bool** |  | [optional] [default to False]
**legacy_zip_naming** | **bool** |  | [optional] [default to False]
**transient_effective_time** | **str** | Format: yyyymmdd. Add a transient effectiveTime to rows of content which are not yet versioned. | [optional] 
**start_effective_time** | **str** | Format: yyyymmdd. Can be used to produce a delta after content is versioned by filtering a SNAPSHOT export by effectiveTime. | [optional] 
**module_ids** | **List[str]** |  | [optional] 
**refset_ids** | **List[str]** | If refsetIds are included, this indicates that the export will be a refset-only export. | [optional] 
**status** | **str** |  | [optional] [default to 'PENDING']
**export_file_path** | **str** |  | [optional] 
**start_export** | **bool** |  | [optional] [default to False]

## Example

```python
from snowstorm_client.models.export_configuration import ExportConfiguration

# TODO update the JSON string below
json = "{}"
# create an instance of ExportConfiguration from a JSON string
export_configuration_instance = ExportConfiguration.from_json(json)
# print the JSON string representation of the object
print(ExportConfiguration.to_json())

# convert the object into a dict
export_configuration_dict = export_configuration_instance.to_dict()
# create an instance of ExportConfiguration from a dict
export_configuration_from_dict = ExportConfiguration.from_dict(export_configuration_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


