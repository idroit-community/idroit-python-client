# swagger_client.HealthApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**app_controller_health**](HealthApi.md#app_controller_health) | **GET** /api/v1/health | ヘルスチェック

# **app_controller_health**
> app_controller_health()

ヘルスチェック

ヘルスチェック

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.HealthApi()

try:
    # ヘルスチェック
    api_instance.app_controller_health()
except ApiException as e:
    print("Exception when calling HealthApi->app_controller_health: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

