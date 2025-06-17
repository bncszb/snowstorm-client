# snowstorm_client.WebRouteApi

All URIs are relative to *https://browser.ihtsdotools.org/snowstorm/snomed-ct*

Method | HTTP request | Description
------------- | ------------- | -------------
[**issue_redirect**](WebRouteApi.md#issue_redirect) | **GET** /web-route | Issue 302 redirection based on locally configured web routing


# **issue_redirect**
> object issue_redirect(uri, format=format, accept=accept)

Issue 302 redirection based on locally configured web routing

Swagger will attempt to follow the 302 redirection, so use developer's tools network tab to view the redirection issued.

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
    api_instance = snowstorm_client.WebRouteApi(api_client)
    uri = 'uri_example' # str | 
    format = 'format_example' # str |  (optional)
    accept = 'accept_example' # str |  (optional)

    try:
        # Issue 302 redirection based on locally configured web routing
        api_response = api_instance.issue_redirect(uri, format=format, accept=accept)
        print("The response of WebRouteApi->issue_redirect:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebRouteApi->issue_redirect: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uri** | **str**|  | 
 **format** | **str**|  | [optional] 
 **accept** | **str**|  | [optional] 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

