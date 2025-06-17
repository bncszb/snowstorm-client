# ExpressionStringPojo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**expression** | **str** |  | [optional] 

## Example

```python
from snowstorm_client.models.expression_string_pojo import ExpressionStringPojo

# TODO update the JSON string below
json = "{}"
# create an instance of ExpressionStringPojo from a JSON string
expression_string_pojo_instance = ExpressionStringPojo.from_json(json)
# print the JSON string representation of the object
print(ExpressionStringPojo.to_json())

# convert the object into a dict
expression_string_pojo_dict = expression_string_pojo_instance.to_dict()
# create an instance of ExpressionStringPojo from a dict
expression_string_pojo_from_dict = ExpressionStringPojo.from_dict(expression_string_pojo_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


