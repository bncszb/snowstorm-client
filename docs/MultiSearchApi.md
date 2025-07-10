# snowstorm_client.MultiSearchApi

All URIs are relative to *https://snowstorm.snomedtools.org/snowstorm/snomed-ct*

Method | HTTP request | Description
------------- | ------------- | -------------
[**find_concepts1**](MultiSearchApi.md#find_concepts1) | **GET** /multisearch/concepts | Search concepts across multiple Code Systems.
[**find_descriptions1**](MultiSearchApi.md#find_descriptions1) | **GET** /multisearch/descriptions | 
[**find_descriptions_reference_sets**](MultiSearchApi.md#find_descriptions_reference_sets) | **GET** /multisearch/descriptions/referencesets | Search descriptions across multiple Code Systems returning reference set membership bucket.


# **find_concepts1**
> ItemsPageConceptMiniComponent find_concepts1(concept_ids=concept_ids, active=active, offset=offset, limit=limit, accept_language=accept_language)

Search concepts across multiple Code Systems.

### Example


```python
import snowstorm_client
from snowstorm_client.models.items_page_concept_mini_component import ItemsPageConceptMiniComponent
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
    api_instance = snowstorm_client.MultiSearchApi(api_client)
    concept_ids = ['concept_ids_example'] # List[str] |  (optional)
    active = True # bool |  (optional)
    offset = 0 # int |  (optional) (default to 0)
    limit = 50 # int |  (optional) (default to 50)
    accept_language = 'en-X-900000000000509007,en-X-900000000000508004,en' # str |  (optional) (default to 'en-X-900000000000509007,en-X-900000000000508004,en')

    try:
        # Search concepts across multiple Code Systems.
        api_response = api_instance.find_concepts1(concept_ids=concept_ids, active=active, offset=offset, limit=limit, accept_language=accept_language)
        print("The response of MultiSearchApi->find_concepts1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MultiSearchApi->find_concepts1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **concept_ids** | [**List[str]**](str.md)|  | [optional] 
 **active** | **bool**|  | [optional] 
 **offset** | **int**|  | [optional] [default to 0]
 **limit** | **int**|  | [optional] [default to 50]
 **accept_language** | **str**|  | [optional] [default to &#39;en-X-900000000000509007,en-X-900000000000508004,en&#39;]

### Return type

[**ItemsPageConceptMiniComponent**](ItemsPageConceptMiniComponent.md)

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

# **find_descriptions1**
> ItemsPageBrowserDescriptionSearchResultComponent find_descriptions1(term, active=active, module=module, ecl=ecl, language=language, type=type, concept_active=concept_active, content_scope=content_scope, offset=offset, limit=limit, accept_language=accept_language)

Search descriptions across multiple Code Systems.

### Example


```python
import snowstorm_client
from snowstorm_client.models.items_page_browser_description_search_result_component import ItemsPageBrowserDescriptionSearchResultComponent
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
    api_instance = snowstorm_client.MultiSearchApi(api_client)
    term = 'term_example' # str | 
    active = True # bool |  (optional)
    module = ['module_example'] # List[str] |  (optional)
    ecl = 'ecl_example' # str |  (optional)
    language = ['language_example'] # List[str] | Set of two character language codes to match. The English language code 'en' will not be added automatically, in contrast to the Accept-Language header which always includes it. Accept-Language header still controls result FSN and PT language selection. (optional)
    type = [56] # List[int] | Set of description types to include. Pick descendants of '900000000000446008 | Description type (core metadata concept) |'. (optional)
    concept_active = True # bool |  (optional)
    content_scope = ALL_PUBLISHED_CONTENT # str |  (optional) (default to ALL_PUBLISHED_CONTENT)
    offset = 0 # int |  (optional) (default to 0)
    limit = 50 # int |  (optional) (default to 50)
    accept_language = 'en-X-900000000000509007,en-X-900000000000508004,en' # str |  (optional) (default to 'en-X-900000000000509007,en-X-900000000000508004,en')

    try:
        api_response = api_instance.find_descriptions1(term, active=active, module=module, ecl=ecl, language=language, type=type, concept_active=concept_active, content_scope=content_scope, offset=offset, limit=limit, accept_language=accept_language)
        print("The response of MultiSearchApi->find_descriptions1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MultiSearchApi->find_descriptions1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **term** | **str**|  | 
 **active** | **bool**|  | [optional] 
 **module** | [**List[str]**](str.md)|  | [optional] 
 **ecl** | **str**|  | [optional] 
 **language** | [**List[str]**](str.md)| Set of two character language codes to match. The English language code &#39;en&#39; will not be added automatically, in contrast to the Accept-Language header which always includes it. Accept-Language header still controls result FSN and PT language selection. | [optional] 
 **type** | [**List[int]**](int.md)| Set of description types to include. Pick descendants of &#39;900000000000446008 | Description type (core metadata concept) |&#39;. | [optional] 
 **concept_active** | **bool**|  | [optional] 
 **content_scope** | **str**|  | [optional] [default to ALL_PUBLISHED_CONTENT]
 **offset** | **int**|  | [optional] [default to 0]
 **limit** | **int**|  | [optional] [default to 50]
 **accept_language** | **str**|  | [optional] [default to &#39;en-X-900000000000509007,en-X-900000000000508004,en&#39;]

### Return type

[**ItemsPageBrowserDescriptionSearchResultComponent**](ItemsPageBrowserDescriptionSearchResultComponent.md)

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

# **find_descriptions_reference_sets**
> PageBrowserDescriptionSearchResultComponent find_descriptions_reference_sets(term, active=active, module=module, language=language, type=type, concept_active=concept_active, content_scope=content_scope, offset=offset, limit=limit, accept_language=accept_language)

Search descriptions across multiple Code Systems returning reference set membership bucket.

### Example


```python
import snowstorm_client
from snowstorm_client.models.page_browser_description_search_result_component import PageBrowserDescriptionSearchResultComponent
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
    api_instance = snowstorm_client.MultiSearchApi(api_client)
    term = 'term_example' # str | 
    active = True # bool |  (optional)
    module = ['module_example'] # List[str] |  (optional)
    language = ['language_example'] # List[str] | Set of two character language codes to match. The English language code 'en' will not be added automatically, in contrast to the Accept-Language header which always includes it. Accept-Language header still controls result FSN and PT language selection. (optional)
    type = [56] # List[int] | Set of description types to include. Pick descendants of '900000000000446008 | Description type (core metadata concept) |'. (optional)
    concept_active = True # bool |  (optional)
    content_scope = ALL_PUBLISHED_CONTENT # str |  (optional) (default to ALL_PUBLISHED_CONTENT)
    offset = 0 # int |  (optional) (default to 0)
    limit = 50 # int |  (optional) (default to 50)
    accept_language = 'en-X-900000000000509007,en-X-900000000000508004,en' # str |  (optional) (default to 'en-X-900000000000509007,en-X-900000000000508004,en')

    try:
        # Search descriptions across multiple Code Systems returning reference set membership bucket.
        api_response = api_instance.find_descriptions_reference_sets(term, active=active, module=module, language=language, type=type, concept_active=concept_active, content_scope=content_scope, offset=offset, limit=limit, accept_language=accept_language)
        print("The response of MultiSearchApi->find_descriptions_reference_sets:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MultiSearchApi->find_descriptions_reference_sets: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **term** | **str**|  | 
 **active** | **bool**|  | [optional] 
 **module** | [**List[str]**](str.md)|  | [optional] 
 **language** | [**List[str]**](str.md)| Set of two character language codes to match. The English language code &#39;en&#39; will not be added automatically, in contrast to the Accept-Language header which always includes it. Accept-Language header still controls result FSN and PT language selection. | [optional] 
 **type** | [**List[int]**](int.md)| Set of description types to include. Pick descendants of &#39;900000000000446008 | Description type (core metadata concept) |&#39;. | [optional] 
 **concept_active** | **bool**|  | [optional] 
 **content_scope** | **str**|  | [optional] [default to ALL_PUBLISHED_CONTENT]
 **offset** | **int**|  | [optional] [default to 0]
 **limit** | **int**|  | [optional] [default to 50]
 **accept_language** | **str**|  | [optional] [default to &#39;en-X-900000000000509007,en-X-900000000000508004,en&#39;]

### Return type

[**PageBrowserDescriptionSearchResultComponent**](PageBrowserDescriptionSearchResultComponent.md)

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

