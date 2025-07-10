# snowstorm_client.ClassificationApi

All URIs are relative to *https://snowstorm.snomedtools.org/snowstorm/snomed-ct*

Method | HTTP request | Description
------------- | ------------- | -------------
[**find_classification**](ClassificationApi.md#find_classification) | **GET** /{branch}/classifications/{classificationId} | Retrieve a classification on a branch
[**find_classifications**](ClassificationApi.md#find_classifications) | **GET** /{branch}/classifications | Retrieve classifications on a branch
[**get_concept_preview**](ClassificationApi.md#get_concept_preview) | **GET** /{branch}/classifications/{classificationId}/concept-preview/{conceptId} | Retrieve a preview of a concept with classification changes applied
[**get_equivalent_concepts**](ClassificationApi.md#get_equivalent_concepts) | **GET** /{branch}/classifications/{classificationId}/equivalent-concepts | Retrieve equivalent concepts from a classification run on a branch
[**get_relationship_changes**](ClassificationApi.md#get_relationship_changes) | **GET** /{branch}/classifications/{classificationId}/relationship-changes | Retrieve relationship changes made by a classification run on a branch


# **find_classification**
> Classification find_classification(branch, classification_id)

Retrieve a classification on a branch

### Example


```python
import snowstorm_client
from snowstorm_client.models.classification import Classification
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
    api_instance = snowstorm_client.ClassificationApi(api_client)
    branch = 'branch_example' # str | 
    classification_id = 'classification_id_example' # str | 

    try:
        # Retrieve a classification on a branch
        api_response = api_instance.find_classification(branch, classification_id)
        print("The response of ClassificationApi->find_classification:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClassificationApi->find_classification: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **branch** | **str**|  | 
 **classification_id** | **str**|  | 

### Return type

[**Classification**](Classification.md)

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

# **find_classifications**
> ItemsPageClassification find_classifications(branch)

Retrieve classifications on a branch

### Example


```python
import snowstorm_client
from snowstorm_client.models.items_page_classification import ItemsPageClassification
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
    api_instance = snowstorm_client.ClassificationApi(api_client)
    branch = 'branch_example' # str | 

    try:
        # Retrieve classifications on a branch
        api_response = api_instance.find_classifications(branch)
        print("The response of ClassificationApi->find_classifications:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClassificationApi->find_classifications: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **branch** | **str**|  | 

### Return type

[**ItemsPageClassification**](ItemsPageClassification.md)

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

# **get_concept_preview**
> ConceptViewComponent get_concept_preview(branch, classification_id, concept_id, accept_language=accept_language)

Retrieve a preview of a concept with classification changes applied

### Example


```python
import snowstorm_client
from snowstorm_client.models.concept_view_component import ConceptViewComponent
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
    api_instance = snowstorm_client.ClassificationApi(api_client)
    branch = 'branch_example' # str | 
    classification_id = 'classification_id_example' # str | 
    concept_id = 'concept_id_example' # str | 
    accept_language = 'en-X-900000000000509007,en-X-900000000000508004,en' # str |  (optional) (default to 'en-X-900000000000509007,en-X-900000000000508004,en')

    try:
        # Retrieve a preview of a concept with classification changes applied
        api_response = api_instance.get_concept_preview(branch, classification_id, concept_id, accept_language=accept_language)
        print("The response of ClassificationApi->get_concept_preview:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClassificationApi->get_concept_preview: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **branch** | **str**|  | 
 **classification_id** | **str**|  | 
 **concept_id** | **str**|  | 
 **accept_language** | **str**|  | [optional] [default to &#39;en-X-900000000000509007,en-X-900000000000508004,en&#39;]

### Return type

[**ConceptViewComponent**](ConceptViewComponent.md)

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

# **get_equivalent_concepts**
> ItemsPageEquivalentConceptsResponse get_equivalent_concepts(branch, classification_id, offset=offset, limit=limit, accept_language=accept_language)

Retrieve equivalent concepts from a classification run on a branch

### Example


```python
import snowstorm_client
from snowstorm_client.models.items_page_equivalent_concepts_response import ItemsPageEquivalentConceptsResponse
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
    api_instance = snowstorm_client.ClassificationApi(api_client)
    branch = 'branch_example' # str | 
    classification_id = 'classification_id_example' # str | 
    offset = 0 # int |  (optional) (default to 0)
    limit = 1000 # int |  (optional) (default to 1000)
    accept_language = 'en-X-900000000000509007,en-X-900000000000508004,en' # str |  (optional) (default to 'en-X-900000000000509007,en-X-900000000000508004,en')

    try:
        # Retrieve equivalent concepts from a classification run on a branch
        api_response = api_instance.get_equivalent_concepts(branch, classification_id, offset=offset, limit=limit, accept_language=accept_language)
        print("The response of ClassificationApi->get_equivalent_concepts:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClassificationApi->get_equivalent_concepts: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **branch** | **str**|  | 
 **classification_id** | **str**|  | 
 **offset** | **int**|  | [optional] [default to 0]
 **limit** | **int**|  | [optional] [default to 1000]
 **accept_language** | **str**|  | [optional] [default to &#39;en-X-900000000000509007,en-X-900000000000508004,en&#39;]

### Return type

[**ItemsPageEquivalentConceptsResponse**](ItemsPageEquivalentConceptsResponse.md)

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

# **get_relationship_changes**
> ItemsPageRelationshipChange get_relationship_changes(branch, classification_id, offset=offset, limit=limit, accept_language=accept_language)

Retrieve relationship changes made by a classification run on a branch

### Example


```python
import snowstorm_client
from snowstorm_client.models.items_page_relationship_change import ItemsPageRelationshipChange
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
    api_instance = snowstorm_client.ClassificationApi(api_client)
    branch = 'branch_example' # str | 
    classification_id = 'classification_id_example' # str | 
    offset = 0 # int |  (optional) (default to 0)
    limit = 1000 # int |  (optional) (default to 1000)
    accept_language = 'en-X-900000000000509007,en-X-900000000000508004,en' # str |  (optional) (default to 'en-X-900000000000509007,en-X-900000000000508004,en')

    try:
        # Retrieve relationship changes made by a classification run on a branch
        api_response = api_instance.get_relationship_changes(branch, classification_id, offset=offset, limit=limit, accept_language=accept_language)
        print("The response of ClassificationApi->get_relationship_changes:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClassificationApi->get_relationship_changes: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **branch** | **str**|  | 
 **classification_id** | **str**|  | 
 **offset** | **int**|  | [optional] [default to 0]
 **limit** | **int**|  | [optional] [default to 1000]
 **accept_language** | **str**|  | [optional] [default to &#39;en-X-900000000000509007,en-X-900000000000508004,en&#39;]

### Return type

[**ItemsPageRelationshipChange**](ItemsPageRelationshipChange.md)

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

