# snowstorm_client.ValidationApi

All URIs are relative to *https://snowstorm.snomedtools.org/snowstorm/snomed-ct*

Method | HTTP request | Description
------------- | ------------- | -------------
[**find_inactive_concepts_with_no_historical_association_by_inactivation_type**](ValidationApi.md#find_inactive_concepts_with_no_historical_association_by_inactivation_type) | **GET** /{branch}/report/inactive-concepts-without-association | 
[**get_semantict_tags**](ValidationApi.md#get_semantict_tags) | **GET** /validation-maintenance/semantic-tags | 


# **find_inactive_concepts_with_no_historical_association_by_inactivation_type**
> List[InactivationTypeAndConceptIdListComponent] find_inactive_concepts_with_no_historical_association_by_inactivation_type(branch, concept_effective_time=concept_effective_time)

Find inactive concepts with no historical association grouped by inactivation type.

### Example


```python
import snowstorm_client
from snowstorm_client.models.inactivation_type_and_concept_id_list_component import InactivationTypeAndConceptIdListComponent
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
    api_instance = snowstorm_client.ValidationApi(api_client)
    branch = 'branch_example' # str | 
    concept_effective_time = 'concept_effective_time_example' # str |  (optional)

    try:
        api_response = api_instance.find_inactive_concepts_with_no_historical_association_by_inactivation_type(branch, concept_effective_time=concept_effective_time)
        print("The response of ValidationApi->find_inactive_concepts_with_no_historical_association_by_inactivation_type:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ValidationApi->find_inactive_concepts_with_no_historical_association_by_inactivation_type: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **branch** | **str**|  | 
 **concept_effective_time** | **str**|  | [optional] 

### Return type

[**List[InactivationTypeAndConceptIdListComponent]**](InactivationTypeAndConceptIdListComponent.md)

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

# **get_semantict_tags**
> List[str] get_semantict_tags(language=language)

Retrieve all semantic tags.

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
    api_instance = snowstorm_client.ValidationApi(api_client)
    language = 'en' # str |  (optional) (default to 'en')

    try:
        api_response = api_instance.get_semantict_tags(language=language)
        print("The response of ValidationApi->get_semantict_tags:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ValidationApi->get_semantict_tags: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **language** | **str**|  | [optional] [default to &#39;en&#39;]

### Return type

**List[str]**

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

