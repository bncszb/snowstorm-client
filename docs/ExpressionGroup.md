# ExpressionGroup


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attributes** | [**List[ExpressionAttribute]**](ExpressionAttribute.md) |  | [optional] 

## Example

```python
from snowstorm_client.models.expression_group import ExpressionGroup

# TODO update the JSON string below
json = "{}"
# create an instance of ExpressionGroup from a JSON string
expression_group_instance = ExpressionGroup.from_json(json)
# print the JSON string representation of the object
print(ExpressionGroup.to_json())

# convert the object into a dict
expression_group_dict = expression_group_instance.to_dict()
# create an instance of ExpressionGroup from a dict
expression_group_from_dict = ExpressionGroup.from_dict(expression_group_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


