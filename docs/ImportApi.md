# snowstorm_client.ImportApi

All URIs are relative to *https://snowstorm.snomedtools.org/snowstorm/snomed-ct*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_import_job**](ImportApi.md#get_import_job) | **GET** /imports/{importId} | Retrieve an import job.


# **get_import_job**
> ImportJob get_import_job(import_id)

Retrieve an import job.

Retrieves the latest state of an import job. Used to view the import configuration and check its status.

### Example


```python
import snowstorm_client
from snowstorm_client.models.import_job import ImportJob
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
    api_instance = snowstorm_client.ImportApi(api_client)
    import_id = 'import_id_example' # str | 

    try:
        # Retrieve an import job.
        api_response = api_instance.get_import_job(import_id)
        print("The response of ImportApi->get_import_job:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ImportApi->get_import_job: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **import_id** | **str**|  | 

### Return type

[**ImportJob**](ImportJob.md)

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

