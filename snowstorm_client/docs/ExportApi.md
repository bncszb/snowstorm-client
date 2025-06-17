# snowstorm_client.ExportApi

All URIs are relative to *https://browser.ihtsdotools.org/snowstorm/snomed-ct*

Method | HTTP request | Description
------------- | ------------- | -------------
[**download_rf2_archive**](ExportApi.md#download_rf2_archive) | **GET** /exports/{exportId}/archive | Download the RF2 archive from an export job.
[**get_export_job**](ExportApi.md#get_export_job) | **GET** /exports/{exportId} | Retrieve an export job.


# **download_rf2_archive**
> download_rf2_archive(export_id)

Download the RF2 archive from an export job.

NOT SUPPORTED IN SWAGGER UI. Instead open the URL in a new browser tab or make a GET request another way. This endpoint can only be called once per exportId.

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
    api_instance = snowstorm_client.ExportApi(api_client)
    export_id = 'export_id_example' # str | 

    try:
        # Download the RF2 archive from an export job.
        api_instance.download_rf2_archive(export_id)
    except Exception as e:
        print("Exception when calling ExportApi->download_rf2_archive: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **export_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_export_job**
> ExportConfiguration get_export_job(export_id)

Retrieve an export job.

### Example


```python
import snowstorm_client
from snowstorm_client.models.export_configuration import ExportConfiguration
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
    api_instance = snowstorm_client.ExportApi(api_client)
    export_id = 'export_id_example' # str | 

    try:
        # Retrieve an export job.
        api_response = api_instance.get_export_job(export_id)
        print("The response of ExportApi->get_export_job:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ExportApi->get_export_job: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **export_id** | **str**|  | 

### Return type

[**ExportConfiguration**](ExportConfiguration.md)

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

