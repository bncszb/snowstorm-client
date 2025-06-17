# InboundRelationshipsResultComponent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**inbound_relationships** | [**List[RelationshipComponent]**](RelationshipComponent.md) |  | [optional] 
**total** | **int** |  | [optional] 

## Example

```python
from snowstorm_client.models.inbound_relationships_result_component import InboundRelationshipsResultComponent

# TODO update the JSON string below
json = "{}"
# create an instance of InboundRelationshipsResultComponent from a JSON string
inbound_relationships_result_component_instance = InboundRelationshipsResultComponent.from_json(json)
# print the JSON string representation of the object
print(InboundRelationshipsResultComponent.to_json())

# convert the object into a dict
inbound_relationships_result_component_dict = inbound_relationships_result_component_instance.to_dict()
# create an instance of InboundRelationshipsResultComponent from a dict
inbound_relationships_result_component_from_dict = InboundRelationshipsResultComponent.from_dict(inbound_relationships_result_component_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


