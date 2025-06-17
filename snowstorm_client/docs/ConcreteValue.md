# ConcreteValue


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data_type** | **str** |  | [optional] 
**value** | **str** |  | [optional] 
**value_with_prefix** | **str** |  | [optional] 

## Example

```python
from snowstorm_client.models.concrete_value import ConcreteValue

# TODO update the JSON string below
json = "{}"
# create an instance of ConcreteValue from a JSON string
concrete_value_instance = ConcreteValue.from_json(json)
# print the JSON string representation of the object
print(ConcreteValue.to_json())

# convert the object into a dict
concrete_value_dict = concrete_value_instance.to_dict()
# create an instance of ConcreteValue from a dict
concrete_value_from_dict = ConcreteValue.from_dict(concrete_value_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


