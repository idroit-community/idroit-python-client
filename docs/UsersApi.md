# swagger_client.UsersApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**users_controller_create**](UsersApi.md#users_controller_create) | **POST** /api/v1/users | ユーザーアカウント作成
[**users_controller_export_key**](UsersApi.md#users_controller_export_key) | **POST** /api/v1/users/{id}/keys/{keyId}/mail | アカウントへの鍵のメール送信
[**users_controller_find_all**](UsersApi.md#users_controller_find_all) | **GET** /api/v1/users | ユーザーアカウント一覧取得
[**users_controller_find_one**](UsersApi.md#users_controller_find_one) | **GET** /api/v1/users/{id} | ユーザーアカウント詳細取得
[**users_controller_invite**](UsersApi.md#users_controller_invite) | **POST** /api/v1/users/{id}/invite | ユーザーアカウントへのアカウント有効化メール送信
[**users_controller_register_user_did**](UsersApi.md#users_controller_register_user_did) | **POST** /api/v1/users/{id}/dids | Get the count of clients
[**users_controller_registration**](UsersApi.md#users_controller_registration) | **POST** /api/v1/users/registration | ユーザーアカウントへのアカウント有効化、登録フロー
[**users_controller_remove**](UsersApi.md#users_controller_remove) | **DELETE** /api/v1/users/{id} | ユーザーアカウント停止
[**users_controller_send_did**](UsersApi.md#users_controller_send_did) | **POST** /api/v1/users/{id}/dids/{didInfoId}/mail | アカウントへのDIDのメール送信
[**users_controller_send_key**](UsersApi.md#users_controller_send_key) | **POST** /api/v1/users/{id}/keys/{didInfoId}/mail | アカウントへのDIDのメール送信
[**users_controller_send_vc**](UsersApi.md#users_controller_send_vc) | **POST** /api/v1/users/{id}/vcs/{vcInfoId}/mail | アカウントへのVCのメール送信
[**users_controller_update**](UsersApi.md#users_controller_update) | **PUT** /api/v1/users/{id} | ユーザーアカウント更新

# **users_controller_create**
> UserResponseDto users_controller_create(body)

ユーザーアカウント作成

新規ユーザーアカウントを作成します。

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.UsersApi(swagger_client.ApiClient(configuration))
body = swagger_client.CreateUserDto() # CreateUserDto | 

try:
    # ユーザーアカウント作成
    api_response = api_instance.users_controller_create(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->users_controller_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateUserDto**](CreateUserDto.md)|  | 

### Return type

[**UserResponseDto**](UserResponseDto.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_controller_export_key**
> users_controller_export_key(id, key_id)

アカウントへの鍵のメール送信

クライアントアカウントに紐付いたDIDの鍵情報をメールで送信し、共有します。

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.UsersApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | 
key_id = 'key_id_example' # str | 

try:
    # アカウントへの鍵のメール送信
    api_instance.users_controller_export_key(id, key_id)
except ApiException as e:
    print("Exception when calling UsersApi->users_controller_export_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **key_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_controller_find_all**
> UsersResponseDto users_controller_find_all(page=page, limit=limit, name=name, email=email, status=status, role=role, need_activate_flow=need_activate_flow)

ユーザーアカウント一覧取得

ユーザーアカウントを一覧として値を返します。

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.UsersApi(swagger_client.ApiClient(configuration))
page = 1.2 # float | (必須) ページネーションを表示する際のページ数に当たるクエリパラメーター。全件取得する際は1を指定。(デフォルト: 1) (optional)
limit = 1.2 # float | (必須) ページネーションを表示する際のページ数あたりに表示する件数を指定するクエリパラメーター。全件取得する際は0を指定。(デフォルト: 10) (optional)
name = 'name_example' # str | (任意) 例: \"Jhon Doe\" (optional)
email = 'email_example' # str | (任意) 例: \"client1@email.com\" (optional)
status = 'status_example' # str | (任意) 例: \"active\" (optional)
role = 'role_example' # str | (任意) 例: \"client\" (optional)
need_activate_flow = true # bool | (任意) 例: true, false (optional)

try:
    # ユーザーアカウント一覧取得
    api_response = api_instance.users_controller_find_all(page=page, limit=limit, name=name, email=email, status=status, role=role, need_activate_flow=need_activate_flow)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->users_controller_find_all: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **float**| (必須) ページネーションを表示する際のページ数に当たるクエリパラメーター。全件取得する際は1を指定。(デフォルト: 1) | [optional] 
 **limit** | **float**| (必須) ページネーションを表示する際のページ数あたりに表示する件数を指定するクエリパラメーター。全件取得する際は0を指定。(デフォルト: 10) | [optional] 
 **name** | **str**| (任意) 例: \&quot;Jhon Doe\&quot; | [optional] 
 **email** | **str**| (任意) 例: \&quot;client1@email.com\&quot; | [optional] 
 **status** | **str**| (任意) 例: \&quot;active\&quot; | [optional] 
 **role** | **str**| (任意) 例: \&quot;client\&quot; | [optional] 
 **need_activate_flow** | **bool**| (任意) 例: true, false | [optional] 

### Return type

[**UsersResponseDto**](UsersResponseDto.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_controller_find_one**
> UserResponseDto users_controller_find_one(id)

ユーザーアカウント詳細取得

リクエストパラメータのidで指定された単一の管理者アカウントの詳細情報の値を返します。

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.UsersApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | 

try:
    # ユーザーアカウント詳細取得
    api_response = api_instance.users_controller_find_one(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->users_controller_find_one: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**UserResponseDto**](UserResponseDto.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_controller_invite**
> users_controller_invite(id)

ユーザーアカウントへのアカウント有効化メール送信

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.UsersApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | 

try:
    # ユーザーアカウントへのアカウント有効化メール送信
    api_instance.users_controller_invite(id)
except ApiException as e:
    print("Exception when calling UsersApi->users_controller_invite: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_controller_register_user_did**
> users_controller_register_user_did(body, id)

Get the count of clients

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.UsersApi(swagger_client.ApiClient(configuration))
body = swagger_client.GenerateDidDto() # GenerateDidDto | 
id = 'id_example' # str | 

try:
    # Get the count of clients
    api_instance.users_controller_register_user_did(body, id)
except ApiException as e:
    print("Exception when calling UsersApi->users_controller_register_user_did: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**GenerateDidDto**](GenerateDidDto.md)|  | 
 **id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_controller_registration**
> users_controller_registration(body, token)

ユーザーアカウントへのアカウント有効化、登録フロー

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.UsersApi(swagger_client.ApiClient(configuration))
body = swagger_client.RegistrationProcessDto() # RegistrationProcessDto | 
token = 'token_example' # str | 

try:
    # ユーザーアカウントへのアカウント有効化、登録フロー
    api_instance.users_controller_registration(body, token)
except ApiException as e:
    print("Exception when calling UsersApi->users_controller_registration: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RegistrationProcessDto**](RegistrationProcessDto.md)|  | 
 **token** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_controller_remove**
> users_controller_remove(id)

ユーザーアカウント停止

リクエストパラメータのidで指定された単一のユーザーアカウントを停止します。

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.UsersApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | 

try:
    # ユーザーアカウント停止
    api_instance.users_controller_remove(id)
except ApiException as e:
    print("Exception when calling UsersApi->users_controller_remove: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_controller_send_did**
> users_controller_send_did(id, did_info_id)

アカウントへのDIDのメール送信

アカウントに紐付いたDIDをメールで送信し、共有します。

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.UsersApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | 
did_info_id = 'did_info_id_example' # str | 

try:
    # アカウントへのDIDのメール送信
    api_instance.users_controller_send_did(id, did_info_id)
except ApiException as e:
    print("Exception when calling UsersApi->users_controller_send_did: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **did_info_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_controller_send_key**
> users_controller_send_key(id, did_info_id)

アカウントへのDIDのメール送信

アカウントに紐付いたDIDをメールで送信し、共有します。

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.UsersApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | 
did_info_id = 'did_info_id_example' # str | 

try:
    # アカウントへのDIDのメール送信
    api_instance.users_controller_send_key(id, did_info_id)
except ApiException as e:
    print("Exception when calling UsersApi->users_controller_send_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **did_info_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_controller_send_vc**
> users_controller_send_vc(id, vc_info_id)

アカウントへのVCのメール送信

アカウントに紐付いたVCをメールで送信し、共有します。

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.UsersApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | 
vc_info_id = 'vc_info_id_example' # str | 

try:
    # アカウントへのVCのメール送信
    api_instance.users_controller_send_vc(id, vc_info_id)
except ApiException as e:
    print("Exception when calling UsersApi->users_controller_send_vc: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **vc_info_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_controller_update**
> UserResponseDto users_controller_update(body, id)

ユーザーアカウント更新

リクエストパラメータのidで指定された単一のユーザーアカウント情報を更新します。

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.UsersApi(swagger_client.ApiClient(configuration))
body = swagger_client.CreateUserDto() # CreateUserDto | 
id = 'id_example' # str | 

try:
    # ユーザーアカウント更新
    api_response = api_instance.users_controller_update(body, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->users_controller_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateUserDto**](CreateUserDto.md)|  | 
 **id** | **str**|  | 

### Return type

[**UserResponseDto**](UserResponseDto.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

