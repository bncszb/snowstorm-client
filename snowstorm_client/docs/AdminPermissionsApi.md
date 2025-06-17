# snowstorm_client.AdminPermissionsApi

All URIs are relative to *https://browser.ihtsdotools.org/snowstorm/snomed-ct*

Method | HTTP request | Description
------------- | ------------- | -------------
[**find_all**](AdminPermissionsApi.md#find_all) | **GET** /admin/permissions | Retrieve all permissions
[**find_for_branch**](AdminPermissionsApi.md#find_for_branch) | **GET** /admin/permissions/{branch} | Retrieve all permissions on given branch
[**find_global**](AdminPermissionsApi.md#find_global) | **GET** /admin/permissions/global | Retrieve all global permissions
[**find_user_group_permissions**](AdminPermissionsApi.md#find_user_group_permissions) | **GET** /admin/permissions/user-group/{userGroup} | Retrieve all permissions for a provided user group


# **find_all**
> List[PermissionRecordComponent] find_all()

Retrieve all permissions

List all roles and user groups set at the global level and set against each branch.

### Example


```python
import snowstorm_client
from snowstorm_client.models.permission_record_component import PermissionRecordComponent
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
    api_instance = snowstorm_client.AdminPermissionsApi(api_client)

    try:
        # Retrieve all permissions
        api_response = api_instance.find_all()
        print("The response of AdminPermissionsApi->find_all:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminPermissionsApi->find_all: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[PermissionRecordComponent]**](PermissionRecordComponent.md)

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

# **find_for_branch**
> List[PermissionRecordComponent] find_for_branch(branch)

Retrieve all permissions on given branch

List roles and user groups for a specific branch.

### Example


```python
import snowstorm_client
from snowstorm_client.models.permission_record_component import PermissionRecordComponent
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
    api_instance = snowstorm_client.AdminPermissionsApi(api_client)
    branch = 'branch_example' # str | 

    try:
        # Retrieve all permissions on given branch
        api_response = api_instance.find_for_branch(branch)
        print("The response of AdminPermissionsApi->find_for_branch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminPermissionsApi->find_for_branch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **branch** | **str**|  | 

### Return type

[**List[PermissionRecordComponent]**](PermissionRecordComponent.md)

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

# **find_global**
> List[PermissionRecordComponent] find_global()

Retrieve all global permissions

List roles and user groups set at the global level.

### Example


```python
import snowstorm_client
from snowstorm_client.models.permission_record_component import PermissionRecordComponent
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
    api_instance = snowstorm_client.AdminPermissionsApi(api_client)

    try:
        # Retrieve all global permissions
        api_response = api_instance.find_global()
        print("The response of AdminPermissionsApi->find_global:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminPermissionsApi->find_global: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[PermissionRecordComponent]**](PermissionRecordComponent.md)

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

# **find_user_group_permissions**
> List[PermissionRecordComponent] find_user_group_permissions(user_group)

Retrieve all permissions for a provided user group

List all permissions for a user group.

### Example


```python
import snowstorm_client
from snowstorm_client.models.permission_record_component import PermissionRecordComponent
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
    api_instance = snowstorm_client.AdminPermissionsApi(api_client)
    user_group = 'user_group_example' # str | 

    try:
        # Retrieve all permissions for a provided user group
        api_response = api_instance.find_user_group_permissions(user_group)
        print("The response of AdminPermissionsApi->find_user_group_permissions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminPermissionsApi->find_user_group_permissions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_group** | **str**|  | 

### Return type

[**List[PermissionRecordComponent]**](PermissionRecordComponent.md)

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

