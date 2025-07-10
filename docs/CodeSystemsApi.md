# snowstorm_client.CodeSystemsApi

All URIs are relative to *https://snowstorm.snomedtools.org/snowstorm/snomed-ct*

Method | HTTP request | Description
------------- | ------------- | -------------
[**find_all_versions**](CodeSystemsApi.md#find_all_versions) | **GET** /codesystems/{shortName}/versions | Retrieve versions of a code system
[**find_code_system**](CodeSystemsApi.md#find_code_system) | **GET** /codesystems/{shortName} | Retrieve a code system
[**get_latest_daily_build**](CodeSystemsApi.md#get_latest_daily_build) | **GET** /codesystems/{shortName}/daily-build/check | Check if daily build import matches today&#39;s date.
[**get_upgrade_job**](CodeSystemsApi.md#get_upgrade_job) | **GET** /codesystems/upgrade/{jobId} | Retrieve an upgrade job.
[**list_code_systems**](CodeSystemsApi.md#list_code_systems) | **GET** /codesystems | List code systems


# **find_all_versions**
> ItemsPageCodeSystemVersion find_all_versions(short_name, show_future_versions=show_future_versions, show_internal_releases=show_internal_releases)

Retrieve versions of a code system

### Example


```python
import snowstorm_client
from snowstorm_client.models.items_page_code_system_version import ItemsPageCodeSystemVersion
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
    api_instance = snowstorm_client.CodeSystemsApi(api_client)
    short_name = 'short_name_example' # str | Code system short name.
    show_future_versions = True # bool | Should versions with a future effective-time be shown. (optional)
    show_internal_releases = True # bool | Should versions marked as 'internalRelease' be shown. (optional)

    try:
        # Retrieve versions of a code system
        api_response = api_instance.find_all_versions(short_name, show_future_versions=show_future_versions, show_internal_releases=show_internal_releases)
        print("The response of CodeSystemsApi->find_all_versions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CodeSystemsApi->find_all_versions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **short_name** | **str**| Code system short name. | 
 **show_future_versions** | **bool**| Should versions with a future effective-time be shown. | [optional] 
 **show_internal_releases** | **bool**| Should versions marked as &#39;internalRelease&#39; be shown. | [optional] 

### Return type

[**ItemsPageCodeSystemVersion**](ItemsPageCodeSystemVersion.md)

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

# **find_code_system**
> CodeSystem find_code_system(short_name)

Retrieve a code system

### Example


```python
import snowstorm_client
from snowstorm_client.models.code_system import CodeSystem
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
    api_instance = snowstorm_client.CodeSystemsApi(api_client)
    short_name = 'short_name_example' # str | 

    try:
        # Retrieve a code system
        api_response = api_instance.find_code_system(short_name)
        print("The response of CodeSystemsApi->find_code_system:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CodeSystemsApi->find_code_system: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **short_name** | **str**|  | 

### Return type

[**CodeSystem**](CodeSystem.md)

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

# **get_latest_daily_build**
> bool get_latest_daily_build(short_name)

Check if daily build import matches today's date.

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
    api_instance = snowstorm_client.CodeSystemsApi(api_client)
    short_name = 'short_name_example' # str | 

    try:
        # Check if daily build import matches today's date.
        api_response = api_instance.get_latest_daily_build(short_name)
        print("The response of CodeSystemsApi->get_latest_daily_build:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CodeSystemsApi->get_latest_daily_build: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **short_name** | **str**|  | 

### Return type

**bool**

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

# **get_upgrade_job**
> CodeSystemUpgradeJob get_upgrade_job(job_id)

Retrieve an upgrade job.

Retrieves the state of an upgrade job. Used to view the upgrade configuration and check its status.

### Example


```python
import snowstorm_client
from snowstorm_client.models.code_system_upgrade_job import CodeSystemUpgradeJob
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
    api_instance = snowstorm_client.CodeSystemsApi(api_client)
    job_id = 'job_id_example' # str | 

    try:
        # Retrieve an upgrade job.
        api_response = api_instance.get_upgrade_job(job_id)
        print("The response of CodeSystemsApi->get_upgrade_job:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CodeSystemsApi->get_upgrade_job: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_id** | **str**|  | 

### Return type

[**CodeSystemUpgradeJob**](CodeSystemUpgradeJob.md)

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

# **list_code_systems**
> ItemsPageCodeSystem list_code_systems(for_branch=for_branch)

List code systems

List all code systems.
forBranch is an optional parameter to find the code system which the specified branch is within.

### Example


```python
import snowstorm_client
from snowstorm_client.models.items_page_code_system import ItemsPageCodeSystem
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
    api_instance = snowstorm_client.CodeSystemsApi(api_client)
    for_branch = 'for_branch_example' # str |  (optional)

    try:
        # List code systems
        api_response = api_instance.list_code_systems(for_branch=for_branch)
        print("The response of CodeSystemsApi->list_code_systems:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CodeSystemsApi->list_code_systems: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **for_branch** | **str**|  | [optional] 

### Return type

[**ItemsPageCodeSystem**](ItemsPageCodeSystem.md)

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

