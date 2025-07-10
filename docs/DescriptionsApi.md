# snowstorm_client.DescriptionsApi

All URIs are relative to *https://snowstorm.snomedtools.org/snowstorm/snomed-ct*

Method | HTTP request | Description
------------- | ------------- | -------------
[**count_semantic_tags**](DescriptionsApi.md#count_semantic_tags) | **GET** /{branch}/descriptions/semantictags | List semantic tags of all active concepts together with a count of concepts using each.
[**fetch_description**](DescriptionsApi.md#fetch_description) | **GET** /{branch}/descriptions/{descriptionId} | 
[**find_browser_descriptions**](DescriptionsApi.md#find_browser_descriptions) | **GET** /browser/{branch}/descriptions | Search for concept descriptions.
[**find_descriptions**](DescriptionsApi.md#find_descriptions) | **GET** /{branch}/descriptions | 


# **count_semantic_tags**
> Dict[str, int] count_semantic_tags(branch)

List semantic tags of all active concepts together with a count of concepts using each.

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
    api_instance = snowstorm_client.DescriptionsApi(api_client)
    branch = 'branch_example' # str | 

    try:
        # List semantic tags of all active concepts together with a count of concepts using each.
        api_response = api_instance.count_semantic_tags(branch)
        print("The response of DescriptionsApi->count_semantic_tags:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DescriptionsApi->count_semantic_tags: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **branch** | **str**|  | 

### Return type

**Dict[str, int]**

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

# **fetch_description**
> DescriptionComponent fetch_description(branch, description_id)

### Example


```python
import snowstorm_client
from snowstorm_client.models.description_component import DescriptionComponent
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
    api_instance = snowstorm_client.DescriptionsApi(api_client)
    branch = 'branch_example' # str | 
    description_id = 'description_id_example' # str | 

    try:
        api_response = api_instance.fetch_description(branch, description_id)
        print("The response of DescriptionsApi->fetch_description:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DescriptionsApi->fetch_description: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **branch** | **str**|  | 
 **description_id** | **str**|  | 

### Return type

[**DescriptionComponent**](DescriptionComponent.md)

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

# **find_browser_descriptions**
> PageBrowserDescriptionSearchResultComponent find_browser_descriptions(branch, term=term, active=active, module=module, language=language, type=type, semantic_tag=semantic_tag, semantic_tags=semantic_tags, preferred_in=preferred_in, acceptable_in=acceptable_in, preferred_or_acceptable_in=preferred_or_acceptable_in, concept_active=concept_active, concept_refset=concept_refset, group_by_concept=group_by_concept, search_mode=search_mode, offset=offset, limit=limit, accept_language=accept_language)

Search for concept descriptions.

The Accept-Language header is used to specify the user's preferred language, 'en' is always added as a fallback if not already included in the list. Each language is used as an optional clause for matching and will include the correct character folding behaviour for that language. The Accept-Language header list is also used to chose the best translated FSN and PT values in the response.

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
    api_instance = snowstorm_client.DescriptionsApi(api_client)
    branch = 'branch_example' # str | 
    term = 'term_example' # str |  (optional)
    active = True # bool |  (optional)
    module = ['module_example'] # List[str] |  (optional)
    language = ['language_example'] # List[str] | Set of two character language codes to match. The English language code 'en' will not be added automatically, in contrast to the Accept-Language header which always includes it. Accept-Language header still controls result FSN and PT language selection. (optional)
    type = [56] # List[int] | Set of description type ids to use include. Defaults to any. Pick descendants of '900000000000446008 | Description type (core metadata concept) |'. Examples: 900000000000003001 (FSN), 900000000000013009 (Synonym), 900000000000550004 (Definition) (optional)
    semantic_tag = 'semantic_tag_example' # str |  (optional)
    semantic_tags = ['semantic_tags_example'] # List[str] | Set of semantic tags. (optional)
    preferred_in = [56] # List[int] | Set of description language reference sets. The description must be preferred in at least one of these to match. (optional)
    acceptable_in = [56] # List[int] | Set of description language reference sets. The description must be acceptable in at least one of these to match. (optional)
    preferred_or_acceptable_in = [56] # List[int] | Set of description language reference sets. The description must be preferred OR acceptable in at least one of these to match. (optional)
    concept_active = True # bool |  (optional)
    concept_refset = 'concept_refset_example' # str |  (optional)
    group_by_concept = False # bool |  (optional) (default to False)
    search_mode = STANDARD # str |  (optional) (default to STANDARD)
    offset = 0 # int |  (optional) (default to 0)
    limit = 50 # int |  (optional) (default to 50)
    accept_language = 'en-X-900000000000509007,en-X-900000000000508004,en' # str |  (optional) (default to 'en-X-900000000000509007,en-X-900000000000508004,en')

    try:
        # Search for concept descriptions.
        api_response = api_instance.find_browser_descriptions(branch, term=term, active=active, module=module, language=language, type=type, semantic_tag=semantic_tag, semantic_tags=semantic_tags, preferred_in=preferred_in, acceptable_in=acceptable_in, preferred_or_acceptable_in=preferred_or_acceptable_in, concept_active=concept_active, concept_refset=concept_refset, group_by_concept=group_by_concept, search_mode=search_mode, offset=offset, limit=limit, accept_language=accept_language)
        print("The response of DescriptionsApi->find_browser_descriptions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DescriptionsApi->find_browser_descriptions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **branch** | **str**|  | 
 **term** | **str**|  | [optional] 
 **active** | **bool**|  | [optional] 
 **module** | [**List[str]**](str.md)|  | [optional] 
 **language** | [**List[str]**](str.md)| Set of two character language codes to match. The English language code &#39;en&#39; will not be added automatically, in contrast to the Accept-Language header which always includes it. Accept-Language header still controls result FSN and PT language selection. | [optional] 
 **type** | [**List[int]**](int.md)| Set of description type ids to use include. Defaults to any. Pick descendants of &#39;900000000000446008 | Description type (core metadata concept) |&#39;. Examples: 900000000000003001 (FSN), 900000000000013009 (Synonym), 900000000000550004 (Definition) | [optional] 
 **semantic_tag** | **str**|  | [optional] 
 **semantic_tags** | [**List[str]**](str.md)| Set of semantic tags. | [optional] 
 **preferred_in** | [**List[int]**](int.md)| Set of description language reference sets. The description must be preferred in at least one of these to match. | [optional] 
 **acceptable_in** | [**List[int]**](int.md)| Set of description language reference sets. The description must be acceptable in at least one of these to match. | [optional] 
 **preferred_or_acceptable_in** | [**List[int]**](int.md)| Set of description language reference sets. The description must be preferred OR acceptable in at least one of these to match. | [optional] 
 **concept_active** | **bool**|  | [optional] 
 **concept_refset** | **str**|  | [optional] 
 **group_by_concept** | **bool**|  | [optional] [default to False]
 **search_mode** | **str**|  | [optional] [default to STANDARD]
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

# **find_descriptions**
> ItemsPageDescriptionComponent find_descriptions(branch, description_ids=description_ids, concept_id=concept_id, concept_ids=concept_ids, offset=offset, limit=limit)

### Example


```python
import snowstorm_client
from snowstorm_client.models.items_page_description_component import ItemsPageDescriptionComponent
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
    api_instance = snowstorm_client.DescriptionsApi(api_client)
    branch = 'branch_example' # str | 
    description_ids = ['description_ids_example'] # List[str] | Set of description ids to match (optional)
    concept_id = 'concept_id_example' # str | The concept id to match (optional)
    concept_ids = ['concept_ids_example'] # List[str] | Set of concept ids to match (optional)
    offset = 0 # int |  (optional) (default to 0)
    limit = 50 # int |  (optional) (default to 50)

    try:
        api_response = api_instance.find_descriptions(branch, description_ids=description_ids, concept_id=concept_id, concept_ids=concept_ids, offset=offset, limit=limit)
        print("The response of DescriptionsApi->find_descriptions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DescriptionsApi->find_descriptions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **branch** | **str**|  | 
 **description_ids** | [**List[str]**](str.md)| Set of description ids to match | [optional] 
 **concept_id** | **str**| The concept id to match | [optional] 
 **concept_ids** | [**List[str]**](str.md)| Set of concept ids to match | [optional] 
 **offset** | **int**|  | [optional] [default to 0]
 **limit** | **int**|  | [optional] [default to 50]

### Return type

[**ItemsPageDescriptionComponent**](ItemsPageDescriptionComponent.md)

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

