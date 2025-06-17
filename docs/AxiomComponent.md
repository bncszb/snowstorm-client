# AxiomComponent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**axiom_id** | **str** |  | [optional] 
**module_id** | **str** |  | [optional] 
**active** | **bool** |  | [optional] 
**released** | **bool** |  | [optional] 
**definition_status_id** | **str** |  | [optional] 
**relationships** | [**List[RelationshipComponent]**](RelationshipComponent.md) |  | [optional] 
**id** | **str** |  | [optional] 
**definition_status** | **str** |  | [optional] 
**effective_time** | **int** |  | [optional] 

## Example

```python
from snowstorm_client.models.axiom_component import AxiomComponent

# TODO update the JSON string below
json = "{}"
# create an instance of AxiomComponent from a JSON string
axiom_component_instance = AxiomComponent.from_json(json)
# print the JSON string representation of the object
print(AxiomComponent.to_json())

# convert the object into a dict
axiom_component_dict = axiom_component_instance.to_dict()
# create an instance of AxiomComponent from a dict
axiom_component_from_dict = AxiomComponent.from_dict(axiom_component_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


