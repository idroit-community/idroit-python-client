# swagger_client.AuthApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**auth_controller_get_profile**](AuthApi.md#auth_controller_get_profile) | **GET** /api/v1/auth/profile | ログイン済みのアカウント情報取得
[**auth_controller_login**](AuthApi.md#auth_controller_login) | **POST** /api/v1/auth/login | アカウントログインを実施

# **auth_controller_get_profile**
> GetProfileResponseDto auth_controller_get_profile()

ログイン済みのアカウント情報取得

ログイン済みの管理者アカウントの情報を返却します。

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.AuthApi(swagger_client.ApiClient(configuration))

try:
    # ログイン済みのアカウント情報取得
    api_response = api_instance.auth_controller_get_profile()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthApi->auth_controller_get_profile: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**GetProfileResponseDto**](GetProfileResponseDto.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **auth_controller_login**
> SignInResponseDto auth_controller_login(body)

アカウントログインを実施

アカウントログインを実行し、認証結果に応じてJSON Web Tokenの値を返します。

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.AuthApi(swagger_client.ApiClient(configuration))
body = swagger_client.SignInDto() # SignInDto | 

try:
    # アカウントログインを実施
    api_response = api_instance.auth_controller_login(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthApi->auth_controller_login: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SignInDto**](SignInDto.md)|  | 

### Return type

[**SignInResponseDto**](SignInResponseDto.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

