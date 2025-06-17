# Branch


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**internal_id** | **str** |  | [optional] 
**path** | **str** |  | [optional] 
**start** | **datetime** |  | [optional] 
**end** | **datetime** |  | [optional] 
**deleted** | **bool** |  | [optional] 
**base** | **datetime** |  | [optional] 
**head** | **datetime** |  | [optional] 
**creation** | **datetime** |  | [optional] 
**last_promotion** | **datetime** |  | [optional] 
**locked** | **bool** |  | [optional] 
**contains_content** | **bool** |  | [optional] 
**versions_replaced** | **Dict[str, List[str]]** |  | [optional] 
**metadata_internal** | **Dict[str, str]** |  | [optional] 
**metadata** | [**Metadata**](Metadata.md) |  | [optional] 
**state** | **str** |  | [optional] 
**head_timestamp** | **int** |  | [optional] 
**base_timestamp** | **int** |  | [optional] 
**creation_timestamp** | **int** |  | [optional] 
**versions_replaced_counts** | **Dict[str, int]** |  | [optional] 

## Example

```python
from snowstorm_client.models.branch import Branch

# TODO update the JSON string below
json = "{}"
# create an instance of Branch from a JSON string
branch_instance = Branch.from_json(json)
# print the JSON string representation of the object
print(Branch.to_json())

# convert the object into a dict
branch_dict = branch_instance.to_dict()
# create an instance of Branch from a dict
branch_from_dict = Branch.from_dict(branch_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


