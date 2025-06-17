# Coding


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**system** | **str** |  | [optional] 
**code** | **str** |  | [optional] 
**display** | **str** |  | [optional] 

## Example

```python
from snowstorm_client.models.coding import Coding

# TODO update the JSON string below
json = "{}"
# create an instance of Coding from a JSON string
coding_instance = Coding.from_json(json)
# print the JSON string representation of the object
print(Coding.to_json())

# convert the object into a dict
coding_dict = coding_instance.to_dict()
# create an instance of Coding from a dict
coding_from_dict = Coding.from_dict(coding_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


