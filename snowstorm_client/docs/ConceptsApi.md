# snowstorm_client.ConceptsApi

All URIs are relative to *https://browser.ihtsdotools.org/snowstorm/snomed-ct*

Method | HTTP request | Description
------------- | ------------- | -------------
[**find_browser_concept**](ConceptsApi.md#find_browser_concept) | **GET** /browser/{branch}/concepts/{conceptId} | Load a concept in the browser format.
[**find_concept**](ConceptsApi.md#find_concept) | **GET** /{branch}/concepts/{conceptId} | 
[**find_concept_ancestor_paths**](ConceptsApi.md#find_concept_ancestor_paths) | **GET** /browser/{branch}/concepts/ancestor-paths | 
[**find_concept_ancestors**](ConceptsApi.md#find_concept_ancestors) | **GET** /browser/{branch}/concepts/{conceptId}/ancestors | 
[**find_concept_children**](ConceptsApi.md#find_concept_children) | **GET** /browser/{branch}/concepts/{conceptId}/children | 
[**find_concept_descendants**](ConceptsApi.md#find_concept_descendants) | **GET** /{branch}/concepts/{conceptId}/descendants | 
[**find_concept_descriptions**](ConceptsApi.md#find_concept_descriptions) | **GET** /{branch}/concepts/{conceptId}/descriptions | 
[**find_concept_inbound_relationships**](ConceptsApi.md#find_concept_inbound_relationships) | **GET** /{branch}/concepts/{conceptId}/inbound-relationships | 
[**find_concept_or_identifier_referenced_concept**](ConceptsApi.md#find_concept_or_identifier_referenced_concept) | **GET** /browser/{branch}/concepts/{componentId}/concept-or-identifier-ref-concept | 
[**find_concept_parents**](ConceptsApi.md#find_concept_parents) | **GET** /browser/{branch}/concepts/{conceptId}/parents | 
[**find_concept_references**](ConceptsApi.md#find_concept_references) | **GET** /{branch}/concepts/{conceptId}/references | Find concepts which reference this concept in the inferred or stated form (including stated axioms).
[**find_concepts**](ConceptsApi.md#find_concepts) | **GET** /{branch}/concepts | 
[**get_browser_concepts**](ConceptsApi.md#get_browser_concepts) | **GET** /browser/{branch}/concepts | Load concepts in the browser format.
[**get_concept_authoring_form**](ConceptsApi.md#get_concept_authoring_form) | **GET** /{branch}/concepts/{conceptId}/authoring-form | 
[**get_concept_bulk_change**](ConceptsApi.md#get_concept_bulk_change) | **GET** /browser/{branch}/concepts/bulk/{bulkChangeId} | Fetch the status of a bulk concept creation or update.
[**get_concept_normal_form**](ConceptsApi.md#get_concept_normal_form) | **GET** /{branch}/concepts/{conceptId}/normal-form | 
[**view_concept_history**](ConceptsApi.md#view_concept_history) | **GET** /browser/{branch}/concepts/{conceptId}/history | View the history of a Concept.


# **find_browser_concept**
> ConceptViewComponent find_browser_concept(branch, concept_id, descendant_count_form=descendant_count_form, accept_language=accept_language)

Load a concept in the browser format.

During content authoring previous versions of the concept can be loaded from version control.
To do this use the branch path format {branch@yyyy-MM-ddTHH:mm:ss.SSSZ} or {branch@epoch_milliseconds}.
The version of the concept when the branch was created can be loaded using {branch@-}.

### Example


```python
import snowstorm_client
from snowstorm_client.models.concept_view_component import ConceptViewComponent
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
    api_instance = snowstorm_client.ConceptsApi(api_client)
    branch = 'branch_example' # str | 
    concept_id = 'concept_id_example' # str | 
    descendant_count_form = 'descendant_count_form_example' # str | If this parameter is set a descendantCount will be included in the response using stated/inferred as requested. (optional)
    accept_language = 'en-X-900000000000509007,en-X-900000000000508004,en' # str |  (optional) (default to 'en-X-900000000000509007,en-X-900000000000508004,en')

    try:
        # Load a concept in the browser format.
        api_response = api_instance.find_browser_concept(branch, concept_id, descendant_count_form=descendant_count_form, accept_language=accept_language)
        print("The response of ConceptsApi->find_browser_concept:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConceptsApi->find_browser_concept: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **branch** | **str**|  | 
 **concept_id** | **str**|  | 
 **descendant_count_form** | **str**| If this parameter is set a descendantCount will be included in the response using stated/inferred as requested. | [optional] 
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

# **find_concept**
> ConceptMini find_concept(branch, concept_id, accept_language=accept_language)

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
    api_instance = snowstorm_client.ConceptsApi(api_client)
    branch = 'branch_example' # str | 
    concept_id = 'concept_id_example' # str | 
    accept_language = 'en-X-900000000000509007,en-X-900000000000508004,en' # str |  (optional) (default to 'en-X-900000000000509007,en-X-900000000000508004,en')

    try:
        api_response = api_instance.find_concept(branch, concept_id, accept_language=accept_language)
        print("The response of ConceptsApi->find_concept:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConceptsApi->find_concept: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **branch** | **str**|  | 
 **concept_id** | **str**|  | 
 **accept_language** | **str**|  | [optional] [default to &#39;en-X-900000000000509007,en-X-900000000000508004,en&#39;]

### Return type

[**ConceptMini**](ConceptMini.md)

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

# **find_concept_ancestor_paths**
> List[ConceptMiniComponent] find_concept_ancestor_paths(branch, concept_ids=concept_ids, form=form, accept_language=accept_language)

### Example


```python
import snowstorm_client
from snowstorm_client.models.concept_mini_component import ConceptMiniComponent
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
    api_instance = snowstorm_client.ConceptsApi(api_client)
    branch = 'branch_example' # str | 
    concept_ids = [56] # List[int] |  (optional)
    form = inferred # str |  (optional) (default to inferred)
    accept_language = 'en-X-900000000000509007,en-X-900000000000508004,en' # str |  (optional) (default to 'en-X-900000000000509007,en-X-900000000000508004,en')

    try:
        api_response = api_instance.find_concept_ancestor_paths(branch, concept_ids=concept_ids, form=form, accept_language=accept_language)
        print("The response of ConceptsApi->find_concept_ancestor_paths:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConceptsApi->find_concept_ancestor_paths: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **branch** | **str**|  | 
 **concept_ids** | [**List[int]**](int.md)|  | [optional] 
 **form** | **str**|  | [optional] [default to inferred]
 **accept_language** | **str**|  | [optional] [default to &#39;en-X-900000000000509007,en-X-900000000000508004,en&#39;]

### Return type

[**List[ConceptMiniComponent]**](ConceptMiniComponent.md)

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

# **find_concept_ancestors**
> List[object] find_concept_ancestors(branch, concept_id, form=form, accept_language=accept_language)

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
    api_instance = snowstorm_client.ConceptsApi(api_client)
    branch = 'branch_example' # str | 
    concept_id = 'concept_id_example' # str | 
    form = inferred # str |  (optional) (default to inferred)
    accept_language = 'en-X-900000000000509007,en-X-900000000000508004,en' # str |  (optional) (default to 'en-X-900000000000509007,en-X-900000000000508004,en')

    try:
        api_response = api_instance.find_concept_ancestors(branch, concept_id, form=form, accept_language=accept_language)
        print("The response of ConceptsApi->find_concept_ancestors:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConceptsApi->find_concept_ancestors: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **branch** | **str**|  | 
 **concept_id** | **str**|  | 
 **form** | **str**|  | [optional] [default to inferred]
 **accept_language** | **str**|  | [optional] [default to &#39;en-X-900000000000509007,en-X-900000000000508004,en&#39;]

### Return type

**List[object]**

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

# **find_concept_children**
> List[ConceptMiniComponent] find_concept_children(branch, concept_id, form=form, include_descendant_count=include_descendant_count, check_descendants_within_refset_id=check_descendants_within_refset_id, accept_language=accept_language)

### Example


```python
import snowstorm_client
from snowstorm_client.models.concept_mini_component import ConceptMiniComponent
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
    api_instance = snowstorm_client.ConceptsApi(api_client)
    branch = 'branch_example' # str | 
    concept_id = 'concept_id_example' # str | 
    form = inferred # str |  (optional) (default to inferred)
    include_descendant_count = False # bool |  (optional) (default to False)
    check_descendants_within_refset_id = 'check_descendants_within_refset_id_example' # str |  (optional)
    accept_language = 'en-X-900000000000509007,en-X-900000000000508004,en' # str |  (optional) (default to 'en-X-900000000000509007,en-X-900000000000508004,en')

    try:
        api_response = api_instance.find_concept_children(branch, concept_id, form=form, include_descendant_count=include_descendant_count, check_descendants_within_refset_id=check_descendants_within_refset_id, accept_language=accept_language)
        print("The response of ConceptsApi->find_concept_children:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConceptsApi->find_concept_children: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **branch** | **str**|  | 
 **concept_id** | **str**|  | 
 **form** | **str**|  | [optional] [default to inferred]
 **include_descendant_count** | **bool**|  | [optional] [default to False]
 **check_descendants_within_refset_id** | **str**|  | [optional] 
 **accept_language** | **str**|  | [optional] [default to &#39;en-X-900000000000509007,en-X-900000000000508004,en&#39;]

### Return type

[**List[ConceptMiniComponent]**](ConceptMiniComponent.md)

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

# **find_concept_descendants**
> ItemsPageObjectComponent find_concept_descendants(branch, concept_id, stated=stated, offset=offset, limit=limit, accept_language=accept_language)

### Example


```python
import snowstorm_client
from snowstorm_client.models.items_page_object_component import ItemsPageObjectComponent
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
    api_instance = snowstorm_client.ConceptsApi(api_client)
    branch = 'branch_example' # str | 
    concept_id = 'concept_id_example' # str | 
    stated = False # bool |  (optional) (default to False)
    offset = 0 # int |  (optional) (default to 0)
    limit = 50 # int |  (optional) (default to 50)
    accept_language = 'en-X-900000000000509007,en-X-900000000000508004,en' # str |  (optional) (default to 'en-X-900000000000509007,en-X-900000000000508004,en')

    try:
        api_response = api_instance.find_concept_descendants(branch, concept_id, stated=stated, offset=offset, limit=limit, accept_language=accept_language)
        print("The response of ConceptsApi->find_concept_descendants:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConceptsApi->find_concept_descendants: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **branch** | **str**|  | 
 **concept_id** | **str**|  | 
 **stated** | **bool**|  | [optional] [default to False]
 **offset** | **int**|  | [optional] [default to 0]
 **limit** | **int**|  | [optional] [default to 50]
 **accept_language** | **str**|  | [optional] [default to &#39;en-X-900000000000509007,en-X-900000000000508004,en&#39;]

### Return type

[**ItemsPageObjectComponent**](ItemsPageObjectComponent.md)

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

# **find_concept_descriptions**
> ConceptDescriptionsResultComponent find_concept_descriptions(branch, concept_id, accept_language=accept_language)

### Example


```python
import snowstorm_client
from snowstorm_client.models.concept_descriptions_result_component import ConceptDescriptionsResultComponent
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
    api_instance = snowstorm_client.ConceptsApi(api_client)
    branch = 'branch_example' # str | 
    concept_id = 'concept_id_example' # str | 
    accept_language = 'en-X-900000000000509007,en-X-900000000000508004,en' # str |  (optional) (default to 'en-X-900000000000509007,en-X-900000000000508004,en')

    try:
        api_response = api_instance.find_concept_descriptions(branch, concept_id, accept_language=accept_language)
        print("The response of ConceptsApi->find_concept_descriptions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConceptsApi->find_concept_descriptions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **branch** | **str**|  | 
 **concept_id** | **str**|  | 
 **accept_language** | **str**|  | [optional] [default to &#39;en-X-900000000000509007,en-X-900000000000508004,en&#39;]

### Return type

[**ConceptDescriptionsResultComponent**](ConceptDescriptionsResultComponent.md)

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

# **find_concept_inbound_relationships**
> InboundRelationshipsResultComponent find_concept_inbound_relationships(branch, concept_id)

### Example


```python
import snowstorm_client
from snowstorm_client.models.inbound_relationships_result_component import InboundRelationshipsResultComponent
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
    api_instance = snowstorm_client.ConceptsApi(api_client)
    branch = 'branch_example' # str | 
    concept_id = 'concept_id_example' # str | 

    try:
        api_response = api_instance.find_concept_inbound_relationships(branch, concept_id)
        print("The response of ConceptsApi->find_concept_inbound_relationships:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConceptsApi->find_concept_inbound_relationships: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **branch** | **str**|  | 
 **concept_id** | **str**|  | 

### Return type

[**InboundRelationshipsResultComponent**](InboundRelationshipsResultComponent.md)

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

# **find_concept_or_identifier_referenced_concept**
> ItemsPageObjectComponent find_concept_or_identifier_referenced_concept(branch, component_id, identifier_scheme=identifier_scheme, accept_language=accept_language)

### Example


```python
import snowstorm_client
from snowstorm_client.models.items_page_object_component import ItemsPageObjectComponent
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
    api_instance = snowstorm_client.ConceptsApi(api_client)
    branch = 'branch_example' # str | 
    component_id = 'component_id_example' # str | Concept id or alternative identifier.
    identifier_scheme = 'identifier_scheme_example' # str | Identifier scheme id to combine with alternative identifier (optional)
    accept_language = 'en-X-900000000000509007,en-X-900000000000508004,en' # str |  (optional) (default to 'en-X-900000000000509007,en-X-900000000000508004,en')

    try:
        api_response = api_instance.find_concept_or_identifier_referenced_concept(branch, component_id, identifier_scheme=identifier_scheme, accept_language=accept_language)
        print("The response of ConceptsApi->find_concept_or_identifier_referenced_concept:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConceptsApi->find_concept_or_identifier_referenced_concept: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **branch** | **str**|  | 
 **component_id** | **str**| Concept id or alternative identifier. | 
 **identifier_scheme** | **str**| Identifier scheme id to combine with alternative identifier | [optional] 
 **accept_language** | **str**|  | [optional] [default to &#39;en-X-900000000000509007,en-X-900000000000508004,en&#39;]

### Return type

[**ItemsPageObjectComponent**](ItemsPageObjectComponent.md)

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

# **find_concept_parents**
> List[ConceptMiniComponent] find_concept_parents(branch, concept_id, form=form, include_descendant_count=include_descendant_count, accept_language=accept_language)

### Example


```python
import snowstorm_client
from snowstorm_client.models.concept_mini_component import ConceptMiniComponent
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
    api_instance = snowstorm_client.ConceptsApi(api_client)
    branch = 'branch_example' # str | 
    concept_id = 'concept_id_example' # str | 
    form = inferred # str |  (optional) (default to inferred)
    include_descendant_count = False # bool |  (optional) (default to False)
    accept_language = 'en-X-900000000000509007,en-X-900000000000508004,en' # str |  (optional) (default to 'en-X-900000000000509007,en-X-900000000000508004,en')

    try:
        api_response = api_instance.find_concept_parents(branch, concept_id, form=form, include_descendant_count=include_descendant_count, accept_language=accept_language)
        print("The response of ConceptsApi->find_concept_parents:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConceptsApi->find_concept_parents: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **branch** | **str**|  | 
 **concept_id** | **str**|  | 
 **form** | **str**|  | [optional] [default to inferred]
 **include_descendant_count** | **bool**|  | [optional] [default to False]
 **accept_language** | **str**|  | [optional] [default to &#39;en-X-900000000000509007,en-X-900000000000508004,en&#39;]

### Return type

[**List[ConceptMiniComponent]**](ConceptMiniComponent.md)

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

# **find_concept_references**
> ConceptReferencesResult find_concept_references(branch, concept_id, stated=stated, offset=offset, limit=limit, accept_language=accept_language)

Find concepts which reference this concept in the inferred or stated form (including stated axioms).

Pagination works on the referencing concepts. A referencing concept may have one or more references of different types.

### Example


```python
import snowstorm_client
from snowstorm_client.models.concept_references_result import ConceptReferencesResult
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
    api_instance = snowstorm_client.ConceptsApi(api_client)
    branch = 'branch_example' # str | 
    concept_id = 56 # int | 
    stated = False # bool |  (optional) (default to False)
    offset = 0 # int |  (optional) (default to 0)
    limit = 1000 # int |  (optional) (default to 1000)
    accept_language = 'en-X-900000000000509007,en-X-900000000000508004,en' # str |  (optional) (default to 'en-X-900000000000509007,en-X-900000000000508004,en')

    try:
        # Find concepts which reference this concept in the inferred or stated form (including stated axioms).
        api_response = api_instance.find_concept_references(branch, concept_id, stated=stated, offset=offset, limit=limit, accept_language=accept_language)
        print("The response of ConceptsApi->find_concept_references:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConceptsApi->find_concept_references: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **branch** | **str**|  | 
 **concept_id** | **int**|  | 
 **stated** | **bool**|  | [optional] [default to False]
 **offset** | **int**|  | [optional] [default to 0]
 **limit** | **int**|  | [optional] [default to 1000]
 **accept_language** | **str**|  | [optional] [default to &#39;en-X-900000000000509007,en-X-900000000000508004,en&#39;]

### Return type

[**ConceptReferencesResult**](ConceptReferencesResult.md)

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

# **find_concepts**
> ItemsPageObject find_concepts(branch, active_filter=active_filter, definition_status_filter=definition_status_filter, module=module, term=term, term_active=term_active, description_type=description_type, language=language, preferred_in=preferred_in, acceptable_in=acceptable_in, preferred_or_acceptable_in=preferred_or_acceptable_in, ecl=ecl, effective_time=effective_time, is_null_effective_time=is_null_effective_time, is_published=is_published, stated_ecl=stated_ecl, include_leaf_flag=include_leaf_flag, form=form, concept_ids=concept_ids, return_id_only=return_id_only, offset=offset, limit=limit, search_after=search_after, accept_language=accept_language)

### Example


```python
import snowstorm_client
from snowstorm_client.models.items_page_object import ItemsPageObject
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
    api_instance = snowstorm_client.ConceptsApi(api_client)
    branch = 'branch_example' # str | 
    active_filter = True # bool |  (optional)
    definition_status_filter = 'definition_status_filter_example' # str |  (optional)
    module = [56] # List[int] | Set of module ids to filter concepts by. Defaults to any. (optional)
    term = 'term_example' # str | Search term to match against concept descriptions using a case-insensitive multi-prefix matching strategy. (optional)
    term_active = True # bool |  (optional)
    description_type = [56] # List[int] | Set of description type ids to use for the term search. Defaults to any. Pick descendants of '900000000000446008 | Description type (core metadata concept) |'. Examples: 900000000000003001 (FSN), 900000000000013009 (Synonym), 900000000000550004 (Definition) (optional)
    language = ['language_example'] # List[str] | Set of two character language codes to match. The English language code 'en' will not be added automatically, in contrast to the Accept-Language header which always includes it. Accept-Language header still controls result FSN and PT language selection. (optional)
    preferred_in = [56] # List[int] | Set of description language reference sets. The description must be preferred in at least one of these to match. (optional)
    acceptable_in = [56] # List[int] | Set of description language reference sets. The description must be acceptable in at least one of these to match. (optional)
    preferred_or_acceptable_in = [56] # List[int] | Set of description language reference sets. The description must be preferred OR acceptable in at least one of these to match. (optional)
    ecl = 'ecl_example' # str |  (optional)
    effective_time = 56 # int |  (optional)
    is_null_effective_time = True # bool |  (optional)
    is_published = True # bool |  (optional)
    stated_ecl = 'stated_ecl_example' # str |  (optional)
    include_leaf_flag = False # bool |  (optional) (default to False)
    form = inferred # str |  (optional) (default to inferred)
    concept_ids = ['concept_ids_example'] # List[str] |  (optional)
    return_id_only = True # bool |  (optional)
    offset = 0 # int |  (optional) (default to 0)
    limit = 50 # int |  (optional) (default to 50)
    search_after = 'search_after_example' # str |  (optional)
    accept_language = 'en-X-900000000000509007,en-X-900000000000508004,en' # str | Accept-Language header can take the format en-x-900000000000508004 which sets the language reference set to use in the results. (optional) (default to 'en-X-900000000000509007,en-X-900000000000508004,en')

    try:
        api_response = api_instance.find_concepts(branch, active_filter=active_filter, definition_status_filter=definition_status_filter, module=module, term=term, term_active=term_active, description_type=description_type, language=language, preferred_in=preferred_in, acceptable_in=acceptable_in, preferred_or_acceptable_in=preferred_or_acceptable_in, ecl=ecl, effective_time=effective_time, is_null_effective_time=is_null_effective_time, is_published=is_published, stated_ecl=stated_ecl, include_leaf_flag=include_leaf_flag, form=form, concept_ids=concept_ids, return_id_only=return_id_only, offset=offset, limit=limit, search_after=search_after, accept_language=accept_language)
        print("The response of ConceptsApi->find_concepts:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConceptsApi->find_concepts: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **branch** | **str**|  | 
 **active_filter** | **bool**|  | [optional] 
 **definition_status_filter** | **str**|  | [optional] 
 **module** | [**List[int]**](int.md)| Set of module ids to filter concepts by. Defaults to any. | [optional] 
 **term** | **str**| Search term to match against concept descriptions using a case-insensitive multi-prefix matching strategy. | [optional] 
 **term_active** | **bool**|  | [optional] 
 **description_type** | [**List[int]**](int.md)| Set of description type ids to use for the term search. Defaults to any. Pick descendants of &#39;900000000000446008 | Description type (core metadata concept) |&#39;. Examples: 900000000000003001 (FSN), 900000000000013009 (Synonym), 900000000000550004 (Definition) | [optional] 
 **language** | [**List[str]**](str.md)| Set of two character language codes to match. The English language code &#39;en&#39; will not be added automatically, in contrast to the Accept-Language header which always includes it. Accept-Language header still controls result FSN and PT language selection. | [optional] 
 **preferred_in** | [**List[int]**](int.md)| Set of description language reference sets. The description must be preferred in at least one of these to match. | [optional] 
 **acceptable_in** | [**List[int]**](int.md)| Set of description language reference sets. The description must be acceptable in at least one of these to match. | [optional] 
 **preferred_or_acceptable_in** | [**List[int]**](int.md)| Set of description language reference sets. The description must be preferred OR acceptable in at least one of these to match. | [optional] 
 **ecl** | **str**|  | [optional] 
 **effective_time** | **int**|  | [optional] 
 **is_null_effective_time** | **bool**|  | [optional] 
 **is_published** | **bool**|  | [optional] 
 **stated_ecl** | **str**|  | [optional] 
 **include_leaf_flag** | **bool**|  | [optional] [default to False]
 **form** | **str**|  | [optional] [default to inferred]
 **concept_ids** | [**List[str]**](str.md)|  | [optional] 
 **return_id_only** | **bool**|  | [optional] 
 **offset** | **int**|  | [optional] [default to 0]
 **limit** | **int**|  | [optional] [default to 50]
 **search_after** | **str**|  | [optional] 
 **accept_language** | **str**| Accept-Language header can take the format en-x-900000000000508004 which sets the language reference set to use in the results. | [optional] [default to &#39;en-X-900000000000509007,en-X-900000000000508004,en&#39;]

### Return type

[**ItemsPageObject**](ItemsPageObject.md)

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

# **get_browser_concepts**
> ItemsPageConceptComponent get_browser_concepts(branch, concept_ids=concept_ids, number=number, size=size, search_after=search_after, accept_language=accept_language)

Load concepts in the browser format.

When enabled 'searchAfter' can be used for unlimited pagination. Load the first page then take the 'searchAfter' value from the response and use that as a parameter in the next page request instead of 'number'.

### Example


```python
import snowstorm_client
from snowstorm_client.models.items_page_concept_component import ItemsPageConceptComponent
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
    api_instance = snowstorm_client.ConceptsApi(api_client)
    branch = 'branch_example' # str | 
    concept_ids = [56] # List[int] |  (optional)
    number = 0 # int |  (optional) (default to 0)
    size = 100 # int |  (optional) (default to 100)
    search_after = 'search_after_example' # str |  (optional)
    accept_language = 'en-X-900000000000509007,en-X-900000000000508004,en' # str |  (optional) (default to 'en-X-900000000000509007,en-X-900000000000508004,en')

    try:
        # Load concepts in the browser format.
        api_response = api_instance.get_browser_concepts(branch, concept_ids=concept_ids, number=number, size=size, search_after=search_after, accept_language=accept_language)
        print("The response of ConceptsApi->get_browser_concepts:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConceptsApi->get_browser_concepts: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **branch** | **str**|  | 
 **concept_ids** | [**List[int]**](int.md)|  | [optional] 
 **number** | **int**|  | [optional] [default to 0]
 **size** | **int**|  | [optional] [default to 100]
 **search_after** | **str**|  | [optional] 
 **accept_language** | **str**|  | [optional] [default to &#39;en-X-900000000000509007,en-X-900000000000508004,en&#39;]

### Return type

[**ItemsPageConceptComponent**](ItemsPageConceptComponent.md)

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

# **get_concept_authoring_form**
> Expression get_concept_authoring_form(branch, concept_id, accept_language=accept_language)

### Example


```python
import snowstorm_client
from snowstorm_client.models.expression import Expression
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
    api_instance = snowstorm_client.ConceptsApi(api_client)
    branch = 'branch_example' # str | 
    concept_id = 'concept_id_example' # str | 
    accept_language = 'en-X-900000000000509007,en-X-900000000000508004,en' # str |  (optional) (default to 'en-X-900000000000509007,en-X-900000000000508004,en')

    try:
        api_response = api_instance.get_concept_authoring_form(branch, concept_id, accept_language=accept_language)
        print("The response of ConceptsApi->get_concept_authoring_form:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConceptsApi->get_concept_authoring_form: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **branch** | **str**|  | 
 **concept_id** | **str**|  | 
 **accept_language** | **str**|  | [optional] [default to &#39;en-X-900000000000509007,en-X-900000000000508004,en&#39;]

### Return type

[**Expression**](Expression.md)

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

# **get_concept_bulk_change**
> AsyncConceptChangeBatch get_concept_bulk_change(branch, bulk_change_id)

Fetch the status of a bulk concept creation or update.

### Example


```python
import snowstorm_client
from snowstorm_client.models.async_concept_change_batch import AsyncConceptChangeBatch
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
    api_instance = snowstorm_client.ConceptsApi(api_client)
    branch = 'branch_example' # str | 
    bulk_change_id = 'bulk_change_id_example' # str | 

    try:
        # Fetch the status of a bulk concept creation or update.
        api_response = api_instance.get_concept_bulk_change(branch, bulk_change_id)
        print("The response of ConceptsApi->get_concept_bulk_change:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConceptsApi->get_concept_bulk_change: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **branch** | **str**|  | 
 **bulk_change_id** | **str**|  | 

### Return type

[**AsyncConceptChangeBatch**](AsyncConceptChangeBatch.md)

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

# **get_concept_normal_form**
> ExpressionStringPojo get_concept_normal_form(branch, concept_id, stated_view=stated_view, include_terms=include_terms, accept_language=accept_language)

### Example


```python
import snowstorm_client
from snowstorm_client.models.expression_string_pojo import ExpressionStringPojo
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
    api_instance = snowstorm_client.ConceptsApi(api_client)
    branch = 'branch_example' # str | 
    concept_id = 'concept_id_example' # str | 
    stated_view = False # bool |  (optional) (default to False)
    include_terms = False # bool |  (optional) (default to False)
    accept_language = 'en-X-900000000000509007,en-X-900000000000508004,en' # str |  (optional) (default to 'en-X-900000000000509007,en-X-900000000000508004,en')

    try:
        api_response = api_instance.get_concept_normal_form(branch, concept_id, stated_view=stated_view, include_terms=include_terms, accept_language=accept_language)
        print("The response of ConceptsApi->get_concept_normal_form:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConceptsApi->get_concept_normal_form: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **branch** | **str**|  | 
 **concept_id** | **str**|  | 
 **stated_view** | **bool**|  | [optional] [default to False]
 **include_terms** | **bool**|  | [optional] [default to False]
 **accept_language** | **str**|  | [optional] [default to &#39;en-X-900000000000509007,en-X-900000000000508004,en&#39;]

### Return type

[**ExpressionStringPojo**](ExpressionStringPojo.md)

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

# **view_concept_history**
> ConceptHistory view_concept_history(branch, concept_id, show_future_versions=show_future_versions, show_internal_releases=show_internal_releases)

View the history of a Concept.

Response details historical changes for the given Concept.

### Example


```python
import snowstorm_client
from snowstorm_client.models.concept_history import ConceptHistory
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
    api_instance = snowstorm_client.ConceptsApi(api_client)
    branch = 'branch_example' # str | 
    concept_id = 'concept_id_example' # str | 
    show_future_versions = False # bool |  (optional) (default to False)
    show_internal_releases = False # bool |  (optional) (default to False)

    try:
        # View the history of a Concept.
        api_response = api_instance.view_concept_history(branch, concept_id, show_future_versions=show_future_versions, show_internal_releases=show_internal_releases)
        print("The response of ConceptsApi->view_concept_history:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConceptsApi->view_concept_history: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **branch** | **str**|  | 
 **concept_id** | **str**|  | 
 **show_future_versions** | **bool**|  | [optional] [default to False]
 **show_internal_releases** | **bool**|  | [optional] [default to False]

### Return type

[**ConceptHistory**](ConceptHistory.md)

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

