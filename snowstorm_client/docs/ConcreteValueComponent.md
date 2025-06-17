# ConcreteValueComponent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data_type** | **str** |  | [optional] 
**value** | **str** |  | [optional] 
**value_with_prefix** | **str** |  | [optional] 

## Example

```python
from snowstorm_client.models.concrete_value_component import ConcreteValueComponent

# TODO update the JSON string below
json = "{}"
# create an instance of ConcreteValueComponent from a JSON string
concrete_value_component_instance = ConcreteValueComponent.from_json(json)
# print the JSON string representation of the object
print(ConcreteValueComponent.to_json())

# convert the object into a dict
concrete_value_component_dict = concrete_value_component_instance.to_dict()
# create an instance of ConcreteValueComponent from a dict
concrete_value_component_from_dict = ConcreteValueComponent.from_dict(concrete_value_component_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


