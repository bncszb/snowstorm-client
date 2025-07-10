# snowstorm_client.IdentifiersApi

All URIs are relative to *https://snowstorm.snomedtools.org/snowstorm/snomed-ct*

Method | HTTP request | Description
------------- | ------------- | -------------
[**find_identifier_referenced_concept**](IdentifiersApi.md#find_identifier_referenced_concept) | **GET** /{branch}/identifiers/{alternateIdentifier}/referenced-concept | 
[**find_identifiers**](IdentifiersApi.md#find_identifiers) | **GET** /{branch}/identifiers | 


# **find_identifier_referenced_concept**
> ConceptMiniComponent find_identifier_referenced_concept(branch, alternate_identifier, accept_language=accept_language)

### Example


```python
import snowstorm_client
from snowstorm_client.models.concept_mini_component import ConceptMiniComponent
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
    api_instance = snowstorm_client.IdentifiersApi(api_client)
    branch = 'branch_example' # str | 
    alternate_identifier = 'alternate_identifier_example' # str | 
    accept_language = 'en-X-900000000000509007,en-X-900000000000508004,en' # str | Accept-Language header can take the format en-x-900000000000508004 which sets the language reference set to use in the results. (optional) (default to 'en-X-900000000000509007,en-X-900000000000508004,en')

    try:
        api_response = api_instance.find_identifier_referenced_concept(branch, alternate_identifier, accept_language=accept_language)
        print("The response of IdentifiersApi->find_identifier_referenced_concept:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IdentifiersApi->find_identifier_referenced_concept: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **branch** | **str**|  | 
 **alternate_identifier** | **str**|  | 
 **accept_language** | **str**| Accept-Language header can take the format en-x-900000000000508004 which sets the language reference set to use in the results. | [optional] [default to &#39;en-X-900000000000509007,en-X-900000000000508004,en&#39;]

### Return type

[**ConceptMiniComponent**](ConceptMiniComponent.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/csv

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_identifiers**
> ItemsPageIdentifierComponent find_identifiers(branch, alternate_identifier=alternate_identifier, identifier_scheme_id=identifier_scheme_id, active_filter=active_filter, is_null_effective_time=is_null_effective_time, module=module, referenced_component_ids=referenced_component_ids, offset=offset, limit=limit, search_after=search_after, accept_language=accept_language)

### Example


```python
import snowstorm_client
from snowstorm_client.models.items_page_identifier_component import ItemsPageIdentifierComponent
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
    api_instance = snowstorm_client.IdentifiersApi(api_client)
    branch = 'branch_example' # str | 
    alternate_identifier = 'alternate_identifier_example' # str |  (optional)
    identifier_scheme_id = 'identifier_scheme_id_example' # str |  (optional)
    active_filter = True # bool |  (optional)
    is_null_effective_time = True # bool |  (optional)
    module = 'module_example' # str |  (optional)
    referenced_component_ids = ['referenced_component_ids_example'] # List[str] |  (optional)
    offset = 0 # int |  (optional) (default to 0)
    limit = 50 # int |  (optional) (default to 50)
    search_after = 'search_after_example' # str |  (optional)
    accept_language = 'en-X-900000000000509007,en-X-900000000000508004,en' # str | Accept-Language header can take the format en-x-900000000000508004 which sets the language reference set to use in the results. (optional) (default to 'en-X-900000000000509007,en-X-900000000000508004,en')

    try:
        api_response = api_instance.find_identifiers(branch, alternate_identifier=alternate_identifier, identifier_scheme_id=identifier_scheme_id, active_filter=active_filter, is_null_effective_time=is_null_effective_time, module=module, referenced_component_ids=referenced_component_ids, offset=offset, limit=limit, search_after=search_after, accept_language=accept_language)
        print("The response of IdentifiersApi->find_identifiers:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IdentifiersApi->find_identifiers: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **branch** | **str**|  | 
 **alternate_identifier** | **str**|  | [optional] 
 **identifier_scheme_id** | **str**|  | [optional] 
 **active_filter** | **bool**|  | [optional] 
 **is_null_effective_time** | **bool**|  | [optional] 
 **module** | **str**|  | [optional] 
 **referenced_component_ids** | [**List[str]**](str.md)|  | [optional] 
 **offset** | **int**|  | [optional] [default to 0]
 **limit** | **int**|  | [optional] [default to 50]
 **search_after** | **str**|  | [optional] 
 **accept_language** | **str**| Accept-Language header can take the format en-x-900000000000508004 which sets the language reference set to use in the results. | [optional] [default to &#39;en-X-900000000000509007,en-X-900000000000508004,en&#39;]

### Return type

[**ItemsPageIdentifierComponent**](ItemsPageIdentifierComponent.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/csv

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

