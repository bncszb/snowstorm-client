# snowstorm_client.RefsetMembersApi

All URIs are relative to *https://browser.ihtsdotools.org/snowstorm/snomed-ct*

Method | HTTP request | Description
------------- | ------------- | -------------
[**fetch_member**](RefsetMembersApi.md#fetch_member) | **GET** /{branch}/members/{uuid} | 
[**find_browser_reference_set_members_with_aggregations**](RefsetMembersApi.md#find_browser_reference_set_members_with_aggregations) | **GET** /browser/{branch}/members | 
[**find_refset_members**](RefsetMembersApi.md#find_refset_members) | **GET** /{branch}/members | Search for reference set members.
[**get_member_bulk_change**](RefsetMembersApi.md#get_member_bulk_change) | **GET** /{branch}/members/bulk/{bulkChangeId} | Fetch the status of a bulk reference set member create/update job.


# **fetch_member**
> ReferenceSetMemberComponent fetch_member(branch, uuid, accept_language=accept_language)

### Example


```python
import snowstorm_client
from snowstorm_client.models.reference_set_member_component import ReferenceSetMemberComponent
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
    api_instance = snowstorm_client.RefsetMembersApi(api_client)
    branch = 'branch_example' # str | 
    uuid = 'uuid_example' # str | 
    accept_language = 'en-X-900000000000509007,en-X-900000000000508004,en' # str |  (optional) (default to 'en-X-900000000000509007,en-X-900000000000508004,en')

    try:
        api_response = api_instance.fetch_member(branch, uuid, accept_language=accept_language)
        print("The response of RefsetMembersApi->fetch_member:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RefsetMembersApi->fetch_member: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **branch** | **str**|  | 
 **uuid** | **str**|  | 
 **accept_language** | **str**|  | [optional] [default to &#39;en-X-900000000000509007,en-X-900000000000508004,en&#39;]

### Return type

[**ReferenceSetMemberComponent**](ReferenceSetMemberComponent.md)

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

# **find_browser_reference_set_members_with_aggregations**
> RefSetMemberPageWithBucketAggregationsReferenceSetMember find_browser_reference_set_members_with_aggregations(branch, reference_set=reference_set, module=module, referenced_component_id=referenced_component_id, active=active, offset=offset, limit=limit, search_after=search_after, accept_language=accept_language)

Search for reference set ids.

### Example


```python
import snowstorm_client
from snowstorm_client.models.ref_set_member_page_with_bucket_aggregations_reference_set_member import RefSetMemberPageWithBucketAggregationsReferenceSetMember
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
    api_instance = snowstorm_client.RefsetMembersApi(api_client)
    branch = 'branch_example' # str | 
    reference_set = 'reference_set_example' # str | A reference set identifier or ECL expression can be used to limit the reference sets searched. Example: <723564002 (optional)
    module = 'module_example' # str | A concept identifier or ECL expression can be used to limit the modules searched. Example: <900000000000445007 (optional)
    referenced_component_id = ['referenced_component_id_example'] # List[str] | Set of referencedComponentId ids to limit search (optional)
    active = True # bool |  (optional)
    offset = 0 # int |  (optional) (default to 0)
    limit = 10 # int |  (optional) (default to 10)
    search_after = 'search_after_example' # str |  (optional)
    accept_language = 'en-X-900000000000509007,en-X-900000000000508004,en' # str |  (optional) (default to 'en-X-900000000000509007,en-X-900000000000508004,en')

    try:
        api_response = api_instance.find_browser_reference_set_members_with_aggregations(branch, reference_set=reference_set, module=module, referenced_component_id=referenced_component_id, active=active, offset=offset, limit=limit, search_after=search_after, accept_language=accept_language)
        print("The response of RefsetMembersApi->find_browser_reference_set_members_with_aggregations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RefsetMembersApi->find_browser_reference_set_members_with_aggregations: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **branch** | **str**|  | 
 **reference_set** | **str**| A reference set identifier or ECL expression can be used to limit the reference sets searched. Example: &lt;723564002 | [optional] 
 **module** | **str**| A concept identifier or ECL expression can be used to limit the modules searched. Example: &lt;900000000000445007 | [optional] 
 **referenced_component_id** | [**List[str]**](str.md)| Set of referencedComponentId ids to limit search | [optional] 
 **active** | **bool**|  | [optional] 
 **offset** | **int**|  | [optional] [default to 0]
 **limit** | **int**|  | [optional] [default to 10]
 **search_after** | **str**|  | [optional] 
 **accept_language** | **str**|  | [optional] [default to &#39;en-X-900000000000509007,en-X-900000000000508004,en&#39;]

### Return type

[**RefSetMemberPageWithBucketAggregationsReferenceSetMember**](RefSetMemberPageWithBucketAggregationsReferenceSetMember.md)

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

# **find_refset_members**
> ItemsPageReferenceSetMemberComponent find_refset_members(branch, reference_set=reference_set, module=module, referenced_component_id=referenced_component_id, active=active, is_null_effective_time=is_null_effective_time, target_component=target_component, map_target=map_target, owl_expression_concept_id=owl_expression_concept_id, owl_expression_gci=owl_expression_gci, offset=offset, limit=limit, search_after=search_after, accept_language=accept_language)

Search for reference set members.

### Example


```python
import snowstorm_client
from snowstorm_client.models.items_page_reference_set_member_component import ItemsPageReferenceSetMemberComponent
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
    api_instance = snowstorm_client.RefsetMembersApi(api_client)
    branch = 'branch_example' # str | 
    reference_set = 'reference_set_example' # str | A reference set identifier or ECL expression can be used to limit the reference sets searched. Example: <723564002 (optional)
    module = 'module_example' # str | A concept identifier or ECL expression can be used to limit the modules searched. Example: <900000000000445007 (optional)
    referenced_component_id = ['referenced_component_id_example'] # List[str] | Set of referencedComponentId ids to limit search (optional)
    active = True # bool |  (optional)
    is_null_effective_time = True # bool |  (optional)
    target_component = ['target_component_example'] # List[str] | Set of target component ids to limit search (optional)
    map_target = 'map_target_example' # str |  (optional)
    owl_expression_concept_id = 'owl_expression_concept_id_example' # str | Search by concept identifiers within an owlExpression. (optional)
    owl_expression_gci = True # bool | Return axiom members with a GCI owlExpression. (optional)
    offset = 0 # int |  (optional) (default to 0)
    limit = 50 # int |  (optional) (default to 50)
    search_after = 'search_after_example' # str |  (optional)
    accept_language = 'en-X-900000000000509007,en-X-900000000000508004,en' # str |  (optional) (default to 'en-X-900000000000509007,en-X-900000000000508004,en')

    try:
        # Search for reference set members.
        api_response = api_instance.find_refset_members(branch, reference_set=reference_set, module=module, referenced_component_id=referenced_component_id, active=active, is_null_effective_time=is_null_effective_time, target_component=target_component, map_target=map_target, owl_expression_concept_id=owl_expression_concept_id, owl_expression_gci=owl_expression_gci, offset=offset, limit=limit, search_after=search_after, accept_language=accept_language)
        print("The response of RefsetMembersApi->find_refset_members:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RefsetMembersApi->find_refset_members: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **branch** | **str**|  | 
 **reference_set** | **str**| A reference set identifier or ECL expression can be used to limit the reference sets searched. Example: &lt;723564002 | [optional] 
 **module** | **str**| A concept identifier or ECL expression can be used to limit the modules searched. Example: &lt;900000000000445007 | [optional] 
 **referenced_component_id** | [**List[str]**](str.md)| Set of referencedComponentId ids to limit search | [optional] 
 **active** | **bool**|  | [optional] 
 **is_null_effective_time** | **bool**|  | [optional] 
 **target_component** | [**List[str]**](str.md)| Set of target component ids to limit search | [optional] 
 **map_target** | **str**|  | [optional] 
 **owl_expression_concept_id** | **str**| Search by concept identifiers within an owlExpression. | [optional] 
 **owl_expression_gci** | **bool**| Return axiom members with a GCI owlExpression. | [optional] 
 **offset** | **int**|  | [optional] [default to 0]
 **limit** | **int**|  | [optional] [default to 50]
 **search_after** | **str**|  | [optional] 
 **accept_language** | **str**|  | [optional] [default to &#39;en-X-900000000000509007,en-X-900000000000508004,en&#39;]

### Return type

[**ItemsPageReferenceSetMemberComponent**](ItemsPageReferenceSetMemberComponent.md)

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

# **get_member_bulk_change**
> AsyncRefsetMemberChangeBatch get_member_bulk_change(branch, bulk_change_id)

Fetch the status of a bulk reference set member create/update job.

### Example


```python
import snowstorm_client
from snowstorm_client.models.async_refset_member_change_batch import AsyncRefsetMemberChangeBatch
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
    api_instance = snowstorm_client.RefsetMembersApi(api_client)
    branch = 'branch_example' # str | 
    bulk_change_id = 'bulk_change_id_example' # str | 

    try:
        # Fetch the status of a bulk reference set member create/update job.
        api_response = api_instance.get_member_bulk_change(branch, bulk_change_id)
        print("The response of RefsetMembersApi->get_member_bulk_change:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RefsetMembersApi->get_member_bulk_change: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **branch** | **str**|  | 
 **bulk_change_id** | **str**|  | 

### Return type

[**AsyncRefsetMemberChangeBatch**](AsyncRefsetMemberChangeBatch.md)

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

