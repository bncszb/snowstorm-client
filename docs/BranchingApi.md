# snowstorm_client.BranchingApi

All URIs are relative to *https://snowstorm.snomedtools.org/snowstorm/snomed-ct*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_branch_review**](BranchingApi.md#get_branch_review) | **GET** /reviews/{id} | 
[**get_branch_review_concept_changes**](BranchingApi.md#get_branch_review_concept_changes) | **GET** /reviews/{id}/concept-changes | 
[**get_merge_review**](BranchingApi.md#get_merge_review) | **GET** /merge-reviews/{id} | 
[**get_merge_review_conflicting_concepts**](BranchingApi.md#get_merge_review_conflicting_concepts) | **GET** /merge-reviews/{id}/details | 
[**retrieve_all_branches**](BranchingApi.md#retrieve_all_branches) | **GET** /branches | Retrieve all branches
[**retrieve_branch**](BranchingApi.md#retrieve_branch) | **GET** /branches/{branch} | Retrieve a single branch
[**retrieve_branch_descendants**](BranchingApi.md#retrieve_branch_descendants) | **GET** /branches/{branch}/children | Retrieve branch descendants
[**retrieve_branch_metadata**](BranchingApi.md#retrieve_branch_metadata) | **GET** /branches/{branch}/metadata | Retrieve a single branch metadata
[**retrieve_merge**](BranchingApi.md#retrieve_merge) | **GET** /merges/{mergeId} | 


# **get_branch_review**
> BranchReview get_branch_review(id)

### Example


```python
import snowstorm_client
from snowstorm_client.models.branch_review import BranchReview
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
    api_instance = snowstorm_client.BranchingApi(api_client)
    id = 'id_example' # str | 

    try:
        api_response = api_instance.get_branch_review(id)
        print("The response of BranchingApi->get_branch_review:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BranchingApi->get_branch_review: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**BranchReview**](BranchReview.md)

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

# **get_branch_review_concept_changes**
> BranchReviewConceptChanges get_branch_review_concept_changes(id)

### Example


```python
import snowstorm_client
from snowstorm_client.models.branch_review_concept_changes import BranchReviewConceptChanges
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
    api_instance = snowstorm_client.BranchingApi(api_client)
    id = 'id_example' # str | 

    try:
        api_response = api_instance.get_branch_review_concept_changes(id)
        print("The response of BranchingApi->get_branch_review_concept_changes:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BranchingApi->get_branch_review_concept_changes: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**BranchReviewConceptChanges**](BranchReviewConceptChanges.md)

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

# **get_merge_review**
> MergeReview get_merge_review(id)

### Example


```python
import snowstorm_client
from snowstorm_client.models.merge_review import MergeReview
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
    api_instance = snowstorm_client.BranchingApi(api_client)
    id = 'id_example' # str | 

    try:
        api_response = api_instance.get_merge_review(id)
        print("The response of BranchingApi->get_merge_review:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BranchingApi->get_merge_review: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**MergeReview**](MergeReview.md)

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

# **get_merge_review_conflicting_concepts**
> List[MergeReviewConceptVersions] get_merge_review_conflicting_concepts(id, accept_language=accept_language)

### Example


```python
import snowstorm_client
from snowstorm_client.models.merge_review_concept_versions import MergeReviewConceptVersions
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
    api_instance = snowstorm_client.BranchingApi(api_client)
    id = 'id_example' # str | 
    accept_language = 'en-X-900000000000509007,en-X-900000000000508004,en' # str |  (optional) (default to 'en-X-900000000000509007,en-X-900000000000508004,en')

    try:
        api_response = api_instance.get_merge_review_conflicting_concepts(id, accept_language=accept_language)
        print("The response of BranchingApi->get_merge_review_conflicting_concepts:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BranchingApi->get_merge_review_conflicting_concepts: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **accept_language** | **str**|  | [optional] [default to &#39;en-X-900000000000509007,en-X-900000000000508004,en&#39;]

### Return type

[**List[MergeReviewConceptVersions]**](MergeReviewConceptVersions.md)

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

# **retrieve_all_branches**
> List[Branch] retrieve_all_branches()

Retrieve all branches

### Example


```python
import snowstorm_client
from snowstorm_client.models.branch import Branch
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
    api_instance = snowstorm_client.BranchingApi(api_client)

    try:
        # Retrieve all branches
        api_response = api_instance.retrieve_all_branches()
        print("The response of BranchingApi->retrieve_all_branches:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BranchingApi->retrieve_all_branches: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[Branch]**](Branch.md)

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

# **retrieve_branch**
> BranchPojo retrieve_branch(branch, include_inherited_metadata=include_inherited_metadata)

Retrieve a single branch

### Example


```python
import snowstorm_client
from snowstorm_client.models.branch_pojo import BranchPojo
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
    api_instance = snowstorm_client.BranchingApi(api_client)
    branch = 'branch_example' # str | 
    include_inherited_metadata = False # bool |  (optional) (default to False)

    try:
        # Retrieve a single branch
        api_response = api_instance.retrieve_branch(branch, include_inherited_metadata=include_inherited_metadata)
        print("The response of BranchingApi->retrieve_branch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BranchingApi->retrieve_branch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **branch** | **str**|  | 
 **include_inherited_metadata** | **bool**|  | [optional] [default to False]

### Return type

[**BranchPojo**](BranchPojo.md)

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

# **retrieve_branch_descendants**
> List[Branch] retrieve_branch_descendants(branch, immediate_children=immediate_children, page=page, size=size)

Retrieve branch descendants

### Example


```python
import snowstorm_client
from snowstorm_client.models.branch import Branch
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
    api_instance = snowstorm_client.BranchingApi(api_client)
    branch = 'branch_example' # str | 
    immediate_children = False # bool |  (optional) (default to False)
    page = 0 # int |  (optional) (default to 0)
    size = 100 # int |  (optional) (default to 100)

    try:
        # Retrieve branch descendants
        api_response = api_instance.retrieve_branch_descendants(branch, immediate_children=immediate_children, page=page, size=size)
        print("The response of BranchingApi->retrieve_branch_descendants:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BranchingApi->retrieve_branch_descendants: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **branch** | **str**|  | 
 **immediate_children** | **bool**|  | [optional] [default to False]
 **page** | **int**|  | [optional] [default to 0]
 **size** | **int**|  | [optional] [default to 100]

### Return type

[**List[Branch]**](Branch.md)

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

# **retrieve_branch_metadata**
> Dict[str, object] retrieve_branch_metadata(branch, include_inherited_metadata=include_inherited_metadata)

Retrieve a single branch metadata

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
    api_instance = snowstorm_client.BranchingApi(api_client)
    branch = 'branch_example' # str | 
    include_inherited_metadata = False # bool |  (optional) (default to False)

    try:
        # Retrieve a single branch metadata
        api_response = api_instance.retrieve_branch_metadata(branch, include_inherited_metadata=include_inherited_metadata)
        print("The response of BranchingApi->retrieve_branch_metadata:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BranchingApi->retrieve_branch_metadata: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **branch** | **str**|  | 
 **include_inherited_metadata** | **bool**|  | [optional] [default to False]

### Return type

**Dict[str, object]**

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

# **retrieve_merge**
> BranchMergeJob retrieve_merge(merge_id)

### Example


```python
import snowstorm_client
from snowstorm_client.models.branch_merge_job import BranchMergeJob
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
    api_instance = snowstorm_client.BranchingApi(api_client)
    merge_id = 'merge_id_example' # str | 

    try:
        api_response = api_instance.retrieve_merge(merge_id)
        print("The response of BranchingApi->retrieve_merge:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BranchingApi->retrieve_merge: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **merge_id** | **str**|  | 

### Return type

[**BranchMergeJob**](BranchMergeJob.md)

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

