# swagger_client.SettingsApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**settings_controller_find_all**](SettingsApi.md#settings_controller_find_all) | **GET** /api/v1/settings | Get all admins
[**settings_controller_find_one**](SettingsApi.md#settings_controller_find_one) | **GET** /api/v1/settings/{key} | Get a specific admin

# **settings_controller_find_all**
> SettingListResponseDto settings_controller_find_all()

Get all admins

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.SettingsApi(swagger_client.ApiClient(configuration))

try:
    # Get all admins
    api_response = api_instance.settings_controller_find_all()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SettingsApi->settings_controller_find_all: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**SettingListResponseDto**](SettingListResponseDto.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **settings_controller_find_one**
> SettingResponseDto settings_controller_find_one(key)

Get a specific admin

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.SettingsApi(swagger_client.ApiClient(configuration))
key = 'key_example' # str | 

try:
    # Get a specific admin
    api_response = api_instance.settings_controller_find_one(key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SettingsApi->settings_controller_find_one: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key** | **str**|  | 

### Return type

[**SettingResponseDto**](SettingResponseDto.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

