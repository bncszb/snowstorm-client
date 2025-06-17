# ExpressionAttribute


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**ConceptMicro**](ConceptMicro.md) |  | [optional] 
**target** | [**ConceptMicro**](ConceptMicro.md) |  | [optional] 
**value** | [**ConcreteValue**](ConcreteValue.md) |  | [optional] 
**concrete** | **bool** |  | [optional] 

## Example

```python
from snowstorm_client.models.expression_attribute import ExpressionAttribute

# TODO update the JSON string below
json = "{}"
# create an instance of ExpressionAttribute from a JSON string
expression_attribute_instance = ExpressionAttribute.from_json(json)
# print the JSON string representation of the object
print(ExpressionAttribute.to_json())

# convert the object into a dict
expression_attribute_dict = expression_attribute_instance.to_dict()
# create an instance of ExpressionAttribute from a dict
expression_attribute_from_dict = ExpressionAttribute.from_dict(expression_attribute_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


