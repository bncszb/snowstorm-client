# snowstorm_client.AuthoringStatsApi

All URIs are relative to *https://browser.ihtsdotools.org/snowstorm/snomed-ct*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_changed_fsns**](AuthoringStatsApi.md#get_changed_fsns) | **GET** /{branch}/authoring-stats/changed-fully-specified-names | 
[**get_inactivated_concepts**](AuthoringStatsApi.md#get_inactivated_concepts) | **GET** /{branch}/authoring-stats/inactivated-concepts | 
[**get_inactivated_synonyms**](AuthoringStatsApi.md#get_inactivated_synonyms) | **GET** /{branch}/authoring-stats/inactivated-synonyms | 
[**get_new_concepts**](AuthoringStatsApi.md#get_new_concepts) | **GET** /{branch}/authoring-stats/new-concepts | 
[**get_new_descriptions**](AuthoringStatsApi.md#get_new_descriptions) | **GET** /{branch}/authoring-stats/new-descriptions | 
[**get_new_synonyms_on_existing_concepts**](AuthoringStatsApi.md#get_new_synonyms_on_existing_concepts) | **GET** /{branch}/authoring-stats/new-synonyms-on-existing-concepts | 
[**get_per_module_counts**](AuthoringStatsApi.md#get_per_module_counts) | **GET** /{branch}/authoring-stats/module-counts | Get counts of various components types per module id
[**get_reactivated_concepts**](AuthoringStatsApi.md#get_reactivated_concepts) | **GET** /{branch}/authoring-stats/reactivated-concepts | 
[**get_reactivated_synonyms**](AuthoringStatsApi.md#get_reactivated_synonyms) | **GET** /{branch}/authoring-stats/reactivated-synonyms | 
[**get_stats**](AuthoringStatsApi.md#get_stats) | **GET** /{branch}/authoring-stats | Calculate statistics for unreleased/unversioned content to be used in daily build browser.


# **get_changed_fsns**
> List[ConceptMicro] get_changed_fsns(branch, accept_language=accept_language)

### Example


```python
import snowstorm_client
from snowstorm_client.models.concept_micro import ConceptMicro
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
    api_instance = snowstorm_client.AuthoringStatsApi(api_client)
    branch = 'branch_example' # str | 
    accept_language = 'en-X-900000000000509007,en-X-900000000000508004,en' # str |  (optional) (default to 'en-X-900000000000509007,en-X-900000000000508004,en')

    try:
        api_response = api_instance.get_changed_fsns(branch, accept_language=accept_language)
        print("The response of AuthoringStatsApi->get_changed_fsns:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthoringStatsApi->get_changed_fsns: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **branch** | **str**|  | 
 **accept_language** | **str**|  | [optional] [default to &#39;en-X-900000000000509007,en-X-900000000000508004,en&#39;]

### Return type

[**List[ConceptMicro]**](ConceptMicro.md)

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

# **get_inactivated_concepts**
> List[ConceptMicro] get_inactivated_concepts(branch, accept_language=accept_language)

### Example


```python
import snowstorm_client
from snowstorm_client.models.concept_micro import ConceptMicro
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
    api_instance = snowstorm_client.AuthoringStatsApi(api_client)
    branch = 'branch_example' # str | 
    accept_language = 'en-X-900000000000509007,en-X-900000000000508004,en' # str |  (optional) (default to 'en-X-900000000000509007,en-X-900000000000508004,en')

    try:
        api_response = api_instance.get_inactivated_concepts(branch, accept_language=accept_language)
        print("The response of AuthoringStatsApi->get_inactivated_concepts:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthoringStatsApi->get_inactivated_concepts: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **branch** | **str**|  | 
 **accept_language** | **str**|  | [optional] [default to &#39;en-X-900000000000509007,en-X-900000000000508004,en&#39;]

### Return type

[**List[ConceptMicro]**](ConceptMicro.md)

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

# **get_inactivated_synonyms**
> List[ConceptMicro] get_inactivated_synonyms(branch)

### Example


```python
import snowstorm_client
from snowstorm_client.models.concept_micro import ConceptMicro
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
    api_instance = snowstorm_client.AuthoringStatsApi(api_client)
    branch = 'branch_example' # str | 

    try:
        api_response = api_instance.get_inactivated_synonyms(branch)
        print("The response of AuthoringStatsApi->get_inactivated_synonyms:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthoringStatsApi->get_inactivated_synonyms: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **branch** | **str**|  | 

### Return type

[**List[ConceptMicro]**](ConceptMicro.md)

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

# **get_new_concepts**
> List[ConceptMicro] get_new_concepts(branch, unpromoted_changes_only=unpromoted_changes_only, accept_language=accept_language)

### Example


```python
import snowstorm_client
from snowstorm_client.models.concept_micro import ConceptMicro
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
    api_instance = snowstorm_client.AuthoringStatsApi(api_client)
    branch = 'branch_example' # str | 
    unpromoted_changes_only = False # bool |  (optional) (default to False)
    accept_language = 'en-X-900000000000509007,en-X-900000000000508004,en' # str |  (optional) (default to 'en-X-900000000000509007,en-X-900000000000508004,en')

    try:
        api_response = api_instance.get_new_concepts(branch, unpromoted_changes_only=unpromoted_changes_only, accept_language=accept_language)
        print("The response of AuthoringStatsApi->get_new_concepts:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthoringStatsApi->get_new_concepts: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **branch** | **str**|  | 
 **unpromoted_changes_only** | **bool**|  | [optional] [default to False]
 **accept_language** | **str**|  | [optional] [default to &#39;en-X-900000000000509007,en-X-900000000000508004,en&#39;]

### Return type

[**List[ConceptMicro]**](ConceptMicro.md)

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

# **get_new_descriptions**
> List[DescriptionMicro] get_new_descriptions(branch, unpromoted_changes_only=unpromoted_changes_only, accept_language=accept_language)

### Example


```python
import snowstorm_client
from snowstorm_client.models.description_micro import DescriptionMicro
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
    api_instance = snowstorm_client.AuthoringStatsApi(api_client)
    branch = 'branch_example' # str | 
    unpromoted_changes_only = False # bool |  (optional) (default to False)
    accept_language = 'en-X-900000000000509007,en-X-900000000000508004,en' # str |  (optional) (default to 'en-X-900000000000509007,en-X-900000000000508004,en')

    try:
        api_response = api_instance.get_new_descriptions(branch, unpromoted_changes_only=unpromoted_changes_only, accept_language=accept_language)
        print("The response of AuthoringStatsApi->get_new_descriptions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthoringStatsApi->get_new_descriptions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **branch** | **str**|  | 
 **unpromoted_changes_only** | **bool**|  | [optional] [default to False]
 **accept_language** | **str**|  | [optional] [default to &#39;en-X-900000000000509007,en-X-900000000000508004,en&#39;]

### Return type

[**List[DescriptionMicro]**](DescriptionMicro.md)

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

# **get_new_synonyms_on_existing_concepts**
> List[ConceptMicro] get_new_synonyms_on_existing_concepts(branch)

### Example


```python
import snowstorm_client
from snowstorm_client.models.concept_micro import ConceptMicro
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
    api_instance = snowstorm_client.AuthoringStatsApi(api_client)
    branch = 'branch_example' # str | 

    try:
        api_response = api_instance.get_new_synonyms_on_existing_concepts(branch)
        print("The response of AuthoringStatsApi->get_new_synonyms_on_existing_concepts:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthoringStatsApi->get_new_synonyms_on_existing_concepts: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **branch** | **str**|  | 

### Return type

[**List[ConceptMicro]**](ConceptMicro.md)

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

# **get_per_module_counts**
> Dict[str, Dict[str, int]] get_per_module_counts(branch)

Get counts of various components types per module id

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
    api_instance = snowstorm_client.AuthoringStatsApi(api_client)
    branch = 'branch_example' # str | 

    try:
        # Get counts of various components types per module id
        api_response = api_instance.get_per_module_counts(branch)
        print("The response of AuthoringStatsApi->get_per_module_counts:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthoringStatsApi->get_per_module_counts: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **branch** | **str**|  | 

### Return type

**Dict[str, Dict[str, int]]**

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

# **get_reactivated_concepts**
> List[ConceptMicro] get_reactivated_concepts(branch, accept_language=accept_language)

### Example


```python
import snowstorm_client
from snowstorm_client.models.concept_micro import ConceptMicro
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
    api_instance = snowstorm_client.AuthoringStatsApi(api_client)
    branch = 'branch_example' # str | 
    accept_language = 'en-X-900000000000509007,en-X-900000000000508004,en' # str |  (optional) (default to 'en-X-900000000000509007,en-X-900000000000508004,en')

    try:
        api_response = api_instance.get_reactivated_concepts(branch, accept_language=accept_language)
        print("The response of AuthoringStatsApi->get_reactivated_concepts:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthoringStatsApi->get_reactivated_concepts: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **branch** | **str**|  | 
 **accept_language** | **str**|  | [optional] [default to &#39;en-X-900000000000509007,en-X-900000000000508004,en&#39;]

### Return type

[**List[ConceptMicro]**](ConceptMicro.md)

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

# **get_reactivated_synonyms**
> List[ConceptMicro] get_reactivated_synonyms(branch)

### Example


```python
import snowstorm_client
from snowstorm_client.models.concept_micro import ConceptMicro
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
    api_instance = snowstorm_client.AuthoringStatsApi(api_client)
    branch = 'branch_example' # str | 

    try:
        api_response = api_instance.get_reactivated_synonyms(branch)
        print("The response of AuthoringStatsApi->get_reactivated_synonyms:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthoringStatsApi->get_reactivated_synonyms: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **branch** | **str**|  | 

### Return type

[**List[ConceptMicro]**](ConceptMicro.md)

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

# **get_stats**
> AuthoringStatsSummary get_stats(branch)

Calculate statistics for unreleased/unversioned content to be used in daily build browser.

Does not work on versioned content.

### Example


```python
import snowstorm_client
from snowstorm_client.models.authoring_stats_summary import AuthoringStatsSummary
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
    api_instance = snowstorm_client.AuthoringStatsApi(api_client)
    branch = 'branch_example' # str | 

    try:
        # Calculate statistics for unreleased/unversioned content to be used in daily build browser.
        api_response = api_instance.get_stats(branch)
        print("The response of AuthoringStatsApi->get_stats:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthoringStatsApi->get_stats: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **branch** | **str**|  | 

### Return type

[**AuthoringStatsSummary**](AuthoringStatsSummary.md)

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

