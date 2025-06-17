# EclString


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ecl_string** | **str** |  | [optional] 

## Example

```python
from snowstorm_client.models.ecl_string import EclString

# TODO update the JSON string below
json = "{}"
# create an instance of EclString from a JSON string
ecl_string_instance = EclString.from_json(json)
# print the JSON string representation of the object
print(EclString.to_json())

# convert the object into a dict
ecl_string_dict = ecl_string_instance.to_dict()
# create an instance of EclString from a dict
ecl_string_from_dict = EclString.from_dict(ecl_string_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


