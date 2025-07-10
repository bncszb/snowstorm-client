# snowstorm_client.RelationshipsApi

All URIs are relative to *https://snowstorm.snomedtools.org/snowstorm/snomed-ct*

Method | HTTP request | Description
------------- | ------------- | -------------
[**fetch_relationship**](RelationshipsApi.md#fetch_relationship) | **GET** /{branch}/relationships/{relationshipId} | 
[**find_relationships**](RelationshipsApi.md#find_relationships) | **GET** /{branch}/relationships | 


# **fetch_relationship**
> RelationshipComponent fetch_relationship(branch, relationship_id, accept_language=accept_language)

### Example


```python
import snowstorm_client
from snowstorm_client.models.relationship_component import RelationshipComponent
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
    api_instance = snowstorm_client.RelationshipsApi(api_client)
    branch = 'branch_example' # str | 
    relationship_id = 'relationship_id_example' # str | 
    accept_language = 'en-X-900000000000509007,en-X-900000000000508004,en' # str |  (optional) (default to 'en-X-900000000000509007,en-X-900000000000508004,en')

    try:
        api_response = api_instance.fetch_relationship(branch, relationship_id, accept_language=accept_language)
        print("The response of RelationshipsApi->fetch_relationship:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RelationshipsApi->fetch_relationship: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **branch** | **str**|  | 
 **relationship_id** | **str**|  | 
 **accept_language** | **str**|  | [optional] [default to &#39;en-X-900000000000509007,en-X-900000000000508004,en&#39;]

### Return type

[**RelationshipComponent**](RelationshipComponent.md)

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

# **find_relationships**
> ItemsPageRelationshipComponent find_relationships(branch, active=active, module=module, effective_time=effective_time, source=source, type=type, destination=destination, characteristic_type=characteristic_type, group=group, offset=offset, limit=limit, accept_language=accept_language)

### Example


```python
import snowstorm_client
from snowstorm_client.models.items_page_relationship_component import ItemsPageRelationshipComponent
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
    api_instance = snowstorm_client.RelationshipsApi(api_client)
    branch = 'branch_example' # str | 
    active = True # bool |  (optional)
    module = 'module_example' # str |  (optional)
    effective_time = 'effective_time_example' # str |  (optional)
    source = 'source_example' # str |  (optional)
    type = 'type_example' # str |  (optional)
    destination = 'destination_example' # str |  (optional)
    characteristic_type = 'characteristic_type_example' # str |  (optional)
    group = 56 # int |  (optional)
    offset = 0 # int |  (optional) (default to 0)
    limit = 50 # int |  (optional) (default to 50)
    accept_language = 'en-X-900000000000509007,en-X-900000000000508004,en' # str |  (optional) (default to 'en-X-900000000000509007,en-X-900000000000508004,en')

    try:
        api_response = api_instance.find_relationships(branch, active=active, module=module, effective_time=effective_time, source=source, type=type, destination=destination, characteristic_type=characteristic_type, group=group, offset=offset, limit=limit, accept_language=accept_language)
        print("The response of RelationshipsApi->find_relationships:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RelationshipsApi->find_relationships: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **branch** | **str**|  | 
 **active** | **bool**|  | [optional] 
 **module** | **str**|  | [optional] 
 **effective_time** | **str**|  | [optional] 
 **source** | **str**|  | [optional] 
 **type** | **str**|  | [optional] 
 **destination** | **str**|  | [optional] 
 **characteristic_type** | **str**|  | [optional] 
 **group** | **int**|  | [optional] 
 **offset** | **int**|  | [optional] [default to 0]
 **limit** | **int**|  | [optional] [default to 50]
 **accept_language** | **str**|  | [optional] [default to &#39;en-X-900000000000509007,en-X-900000000000508004,en&#39;]

### Return type

[**ItemsPageRelationshipComponent**](ItemsPageRelationshipComponent.md)

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

