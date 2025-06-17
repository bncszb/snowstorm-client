# DescriptionMicro


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**concept_id** | **str** |  | [optional] 
**term** | **str** |  | [optional] 

## Example

```python
from snowstorm_client.models.description_micro import DescriptionMicro

# TODO update the JSON string below
json = "{}"
# create an instance of DescriptionMicro from a JSON string
description_micro_instance = DescriptionMicro.from_json(json)
# print the JSON string representation of the object
print(DescriptionMicro.to_json())

# convert the object into a dict
description_micro_dict = description_micro_instance.to_dict()
# create an instance of DescriptionMicro from a dict
description_micro_from_dict = DescriptionMicro.from_dict(description_micro_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


