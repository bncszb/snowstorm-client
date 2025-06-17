# snowstorm_client.AdminApi

All URIs are relative to *https://browser.ihtsdotools.org/snowstorm/snomed-ct*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_ecl_cache_stats**](AdminApi.md#get_ecl_cache_stats) | **GET** /admin/cache/ecl/stats | 


# **get_ecl_cache_stats**
> Dict[str, Dict[str, int]] get_ecl_cache_stats()

### Example


```python
import snowstorm_client
from snowstorm_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://browser.ihtsdotools.org/snowstorm/snomed-ct
# See configuration.py for a list of all supported configuration parameters.
configuration = snowstorm_client.Configuration(
    host = "https://browser.ihtsdotools.org/snowstorm/snomed-ct"
)


# Enter a context with an instance of the API client
with snowstorm_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = snowstorm_client.AdminApi(api_client)

    try:
        api_response = api_instance.get_ecl_cache_stats()
        print("The response of AdminApi->get_ecl_cache_stats:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->get_ecl_cache_stats: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

**Dict[str, Dict[str, int]]**

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

