# snowstorm_client.VersionApi

All URIs are relative to *https://snowstorm.snomedtools.org/snowstorm/snomed-ct*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_build_information**](VersionApi.md#get_build_information) | **GET** /version | Software build version and timestamp.


# **get_build_information**
> BuildVersion get_build_information()

Software build version and timestamp.

### Example


```python
import snowstorm_client
from snowstorm_client.models.build_version import BuildVersion
from snowstorm_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://snowstorm.snomedtools.org/snowstorm/snomed-ct
# See configuration.py for a list of all supported configuration parameters.
configuration = snowstorm_client.Configuration(
    host = "https://snowstorm.snomedtools.org/snowstorm/snomed-ct"
)


# Enter a context with an instance of the API client
with snowstorm_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = snowstorm_client.VersionApi(api_client)

    try:
        # Software build version and timestamp.
        api_response = api_instance.get_build_information()
        print("The response of VersionApi->get_build_information:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VersionApi->get_build_information: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**BuildVersion**](BuildVersion.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

