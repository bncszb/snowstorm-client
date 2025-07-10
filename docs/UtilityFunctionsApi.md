# snowstorm_client.UtilityFunctionsApi

All URIs are relative to *https://snowstorm.snomedtools.org/snowstorm/snomed-ct*

Method | HTTP request | Description
------------- | ------------- | -------------
[**parse_ecl**](UtilityFunctionsApi.md#parse_ecl) | **POST** /util/ecl-string-to-model | Parse ECL and convert to a model representation.
[**parse_ecl_model**](UtilityFunctionsApi.md#parse_ecl_model) | **POST** /util/ecl-model-to-string | Parse ECL model representation and convert it to ECL string.


# **parse_ecl**
> object parse_ecl(body)

Parse ECL and convert to a model representation.

This utility function can be used to parse Expression Constraint Language and convert to a model representation, to support ECL builder web applications. Please note that this function does not validate any concepts or terms within the expression.

### Example


```python
import snowstorm_client
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
    api_instance = snowstorm_client.UtilityFunctionsApi(api_client)
    body = 'body_example' # str | 

    try:
        # Parse ECL and convert to a model representation.
        api_response = api_instance.parse_ecl(body)
        print("The response of UtilityFunctionsApi->parse_ecl:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UtilityFunctionsApi->parse_ecl: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **str**|  | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **parse_ecl_model**
> EclString parse_ecl_model(body)

Parse ECL model representation and convert it to ECL string.

This utility function can be used to convert an Expression Constraint Language JSON model representation to an ECL string, to support ECL builder web application. Please note that this function does not validate any concepts or terms within the expression.

### Example


```python
import snowstorm_client
from snowstorm_client.models.ecl_string import EclString
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
    api_instance = snowstorm_client.UtilityFunctionsApi(api_client)
    body = 'body_example' # str | 

    try:
        # Parse ECL model representation and convert it to ECL string.
        api_response = api_instance.parse_ecl_model(body)
        print("The response of UtilityFunctionsApi->parse_ecl_model:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UtilityFunctionsApi->parse_ecl_model: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **str**|  | 

### Return type

[**EclString**](EclString.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

