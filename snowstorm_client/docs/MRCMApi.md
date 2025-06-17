# snowstorm_client.MRCMApi

All URIs are relative to *https://browser.ihtsdotools.org/snowstorm/snomed-ct*

Method | HTTP request | Description
------------- | ------------- | -------------
[**retrieve_attribute_values**](MRCMApi.md#retrieve_attribute_values) | **GET** /mrcm/{branch}/attribute-values/{attributeId} | Retrieve valid values for the given attribute and term prefix.
[**retrieve_concept_model_attribute_hierarchy**](MRCMApi.md#retrieve_concept_model_attribute_hierarchy) | **GET** /mrcm/{branch}/concept-model-attribute-hierarchy | Retrieve all active concept model attributes in a hierarchical structure.
[**retrieve_domain_attributes**](MRCMApi.md#retrieve_domain_attributes) | **GET** /mrcm/{branch}/domain-attributes | Retrieve MRCM domain attributes applicable for the given stated parents.


# **retrieve_attribute_values**
> ItemsPageConceptMini retrieve_attribute_values(branch, attribute_id, term_prefix, content_type=content_type, accept_language=accept_language)

Retrieve valid values for the given attribute and term prefix.

### Example


```python
import snowstorm_client
from snowstorm_client.models.items_page_concept_mini import ItemsPageConceptMini
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
    api_instance = snowstorm_client.MRCMApi(api_client)
    branch = 'branch_example' # str | 
    attribute_id = 'attribute_id_example' # str | 
    term_prefix = 'term_prefix_example' # str | 
    content_type = NEW_PRECOORDINATED # str |  (optional) (default to NEW_PRECOORDINATED)
    accept_language = 'en-X-900000000000509007,en-X-900000000000508004,en' # str |  (optional) (default to 'en-X-900000000000509007,en-X-900000000000508004,en')

    try:
        # Retrieve valid values for the given attribute and term prefix.
        api_response = api_instance.retrieve_attribute_values(branch, attribute_id, term_prefix, content_type=content_type, accept_language=accept_language)
        print("The response of MRCMApi->retrieve_attribute_values:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MRCMApi->retrieve_attribute_values: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **branch** | **str**|  | 
 **attribute_id** | **str**|  | 
 **term_prefix** | **str**|  | 
 **content_type** | **str**|  | [optional] [default to NEW_PRECOORDINATED]
 **accept_language** | **str**|  | [optional] [default to &#39;en-X-900000000000509007,en-X-900000000000508004,en&#39;]

### Return type

[**ItemsPageConceptMini**](ItemsPageConceptMini.md)

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

# **retrieve_concept_model_attribute_hierarchy**
> ConceptMini retrieve_concept_model_attribute_hierarchy(branch, accept_language=accept_language)

Retrieve all active concept model attributes in a hierarchical structure.

### Example


```python
import snowstorm_client
from snowstorm_client.models.concept_mini import ConceptMini
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
    api_instance = snowstorm_client.MRCMApi(api_client)
    branch = 'branch_example' # str | 
    accept_language = 'en-X-900000000000509007,en-X-900000000000508004,en' # str |  (optional) (default to 'en-X-900000000000509007,en-X-900000000000508004,en')

    try:
        # Retrieve all active concept model attributes in a hierarchical structure.
        api_response = api_instance.retrieve_concept_model_attribute_hierarchy(branch, accept_language=accept_language)
        print("The response of MRCMApi->retrieve_concept_model_attribute_hierarchy:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MRCMApi->retrieve_concept_model_attribute_hierarchy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **branch** | **str**|  | 
 **accept_language** | **str**|  | [optional] [default to &#39;en-X-900000000000509007,en-X-900000000000508004,en&#39;]

### Return type

[**ConceptMini**](ConceptMini.md)

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

# **retrieve_domain_attributes**
> ItemsPageConceptMini retrieve_domain_attributes(branch, parent_ids=parent_ids, proximal_primitive_modeling=proximal_primitive_modeling, content_type=content_type, accept_language=accept_language)

Retrieve MRCM domain attributes applicable for the given stated parents.

The parentIds must be the set ids of stated parents. If creating post-coordinated expressions be sure to set the content type to POSTCOORDINATED.

### Example


```python
import snowstorm_client
from snowstorm_client.models.items_page_concept_mini import ItemsPageConceptMini
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
    api_instance = snowstorm_client.MRCMApi(api_client)
    branch = 'branch_example' # str | 
    parent_ids = [56] # List[int] |  (optional)
    proximal_primitive_modeling = True # bool |  (optional) (default to True)
    content_type = NEW_PRECOORDINATED # str |  (optional) (default to NEW_PRECOORDINATED)
    accept_language = 'en-X-900000000000509007,en-X-900000000000508004,en' # str |  (optional) (default to 'en-X-900000000000509007,en-X-900000000000508004,en')

    try:
        # Retrieve MRCM domain attributes applicable for the given stated parents.
        api_response = api_instance.retrieve_domain_attributes(branch, parent_ids=parent_ids, proximal_primitive_modeling=proximal_primitive_modeling, content_type=content_type, accept_language=accept_language)
        print("The response of MRCMApi->retrieve_domain_attributes:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MRCMApi->retrieve_domain_attributes: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **branch** | **str**|  | 
 **parent_ids** | [**List[int]**](int.md)|  | [optional] 
 **proximal_primitive_modeling** | **bool**|  | [optional] [default to True]
 **content_type** | **str**|  | [optional] [default to NEW_PRECOORDINATED]
 **accept_language** | **str**|  | [optional] [default to &#39;en-X-900000000000509007,en-X-900000000000508004,en&#39;]

### Return type

[**ItemsPageConceptMini**](ItemsPageConceptMini.md)

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

