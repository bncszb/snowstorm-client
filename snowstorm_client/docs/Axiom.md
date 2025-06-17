# Axiom


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**axiom_id** | **str** |  | [optional] 
**module_id** | **str** |  | [optional] 
**active** | **bool** |  | [optional] 
**released** | **bool** |  | [optional] 
**definition_status_id** | **str** |  | [optional] 
**relationships** | [**List[Relationship]**](Relationship.md) |  | [optional] 
**id** | **str** |  | [optional] 
**definition_status** | **str** |  | [optional] 
**effective_time** | **int** |  | [optional] 

## Example

```python
from snowstorm_client.models.axiom import Axiom

# TODO update the JSON string below
json = "{}"
# create an instance of Axiom from a JSON string
axiom_instance = Axiom.from_json(json)
# print the JSON string representation of the object
print(Axiom.to_json())

# convert the object into a dict
axiom_dict = axiom_instance.to_dict()
# create an instance of Axiom from a dict
axiom_from_dict = Axiom.from_dict(axiom_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


