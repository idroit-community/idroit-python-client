# swagger_client.DidInfosApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**did_infos_controller_add_label**](DidInfosApi.md#did_infos_controller_add_label) | **PUT** /api/v1/did-infos/{id} | DID情報へのラベル追加
[**did_infos_controller_connect_user**](DidInfosApi.md#did_infos_controller_connect_user) | **PUT** /api/v1/did-infos/{id}/user/{user_id} | DID情報へのクライアントアカウント紐付け
[**did_infos_controller_create**](DidInfosApi.md#did_infos_controller_create) | **POST** /api/v1/did-infos | 新規DID生成
[**did_infos_controller_disconnect_user**](DidInfosApi.md#did_infos_controller_disconnect_user) | **DELETE** /api/v1/did-infos/{id}/user | DID情報のクライアントアカウント紐付け解除
[**did_infos_controller_find_all**](DidInfosApi.md#did_infos_controller_find_all) | **GET** /api/v1/did-infos | DID情報一覧取得
[**did_infos_controller_find_one**](DidInfosApi.md#did_infos_controller_find_one) | **GET** /api/v1/did-infos/{id} | DID情報詳細取得
[**did_infos_controller_register**](DidInfosApi.md#did_infos_controller_register) | **POST** /api/v1/did-infos/register | 既存DID登録
[**did_infos_controller_remove**](DidInfosApi.md#did_infos_controller_remove) | **DELETE** /api/v1/did-infos/{id} | DID情報削除
[**did_infos_controller_resolve**](DidInfosApi.md#did_infos_controller_resolve) | **POST** /api/v1/did-infos/resolver | DID解決

# **did_infos_controller_add_label**
> DidInfoResponseDto did_infos_controller_add_label(body, id)

DID情報へのラベル追加

リクエストパラメータのidで指定された単一のDID情報に対して、任意の管理用ラベルを追加します。

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.DidInfosApi(swagger_client.ApiClient(configuration))
body = swagger_client.AddLabelToDidInfoDto() # AddLabelToDidInfoDto | 
id = 'id_example' # str | 

try:
    # DID情報へのラベル追加
    api_response = api_instance.did_infos_controller_add_label(body, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DidInfosApi->did_infos_controller_add_label: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AddLabelToDidInfoDto**](AddLabelToDidInfoDto.md)|  | 
 **id** | **str**|  | 

### Return type

[**DidInfoResponseDto**](DidInfoResponseDto.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **did_infos_controller_connect_user**
> DidInfoResponseDto did_infos_controller_connect_user(id, user_id)

DID情報へのクライアントアカウント紐付け

DID情報の所有者、関係者などの管理者としてクライアントアカウントを紐付けます。

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.DidInfosApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | 
user_id = 'user_id_example' # str | 

try:
    # DID情報へのクライアントアカウント紐付け
    api_response = api_instance.did_infos_controller_connect_user(id, user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DidInfosApi->did_infos_controller_connect_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **user_id** | **str**|  | 

### Return type

[**DidInfoResponseDto**](DidInfoResponseDto.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **did_infos_controller_create**
> did_infos_controller_create(body)

新規DID生成

新規DIDを生成します。

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.DidInfosApi(swagger_client.ApiClient(configuration))
body = swagger_client.CreateDidDto() # CreateDidDto | 

try:
    # 新規DID生成
    api_instance.did_infos_controller_create(body)
except ApiException as e:
    print("Exception when calling DidInfosApi->did_infos_controller_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateDidDto**](CreateDidDto.md)|  | 

### Return type

void (empty response body)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **did_infos_controller_disconnect_user**
> did_infos_controller_disconnect_user(id)

DID情報のクライアントアカウント紐付け解除

DID情報に紐付いたクライアントアカウントの紐付けを解除します。

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.DidInfosApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | 

try:
    # DID情報のクライアントアカウント紐付け解除
    api_instance.did_infos_controller_disconnect_user(id)
except ApiException as e:
    print("Exception when calling DidInfosApi->did_infos_controller_disconnect_user: %s\n" % e)
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
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **did_infos_controller_find_all**
> DidInfosResponseDto did_infos_controller_find_all(page=page, limit=limit, did=did, manage_uuid=manage_uuid, label=label, method=method, exist_private_key=exist_private_key, description=description, domain_name=domain_name)

DID情報一覧取得

アプリケーションが管理するDID情報を一覧として値を返します。

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.DidInfosApi(swagger_client.ApiClient(configuration))
page = 1.2 # float | (必須) ページネーションを表示する際のページ数に当たるクエリパラメーター。全件取得する際は1を指定。(デフォルト: 1) (optional)
limit = 1.2 # float | (必須) ページネーションを表示する際のページ数あたりに表示する件数を指定するクエリパラメーター。全件取得する際は0を指定。(デフォルト: 10) (optional)
did = 'did_example' # str | (任意) 例: \"did:key:z6MkhGeGj7u5htkCYjE4PaQ8HUqjYyTmxpDb6Q1MqUpUDsN7\" (optional)
manage_uuid = 'manage_uuid_example' # str | (任意) 例: \"32bad62a-4186-4d04-a26a-fcee79d5824b\" (optional)
label = 'label_example' # str | (任意) 例: \"did-for-project1\" (optional)
method = 'method_example' # str | (任意) 例: \"did:key (optional)
exist_private_key = true # bool | (任意) 例: true (optional)
description = 'description_example' # str | (任意)  (optional)
domain_name = 'domain_name_example' # str | (任意) 例: \"did:web:idroit-dashboard.com\" (optional)

try:
    # DID情報一覧取得
    api_response = api_instance.did_infos_controller_find_all(page=page, limit=limit, did=did, manage_uuid=manage_uuid, label=label, method=method, exist_private_key=exist_private_key, description=description, domain_name=domain_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DidInfosApi->did_infos_controller_find_all: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **float**| (必須) ページネーションを表示する際のページ数に当たるクエリパラメーター。全件取得する際は1を指定。(デフォルト: 1) | [optional] 
 **limit** | **float**| (必須) ページネーションを表示する際のページ数あたりに表示する件数を指定するクエリパラメーター。全件取得する際は0を指定。(デフォルト: 10) | [optional] 
 **did** | **str**| (任意) 例: \&quot;did:key:z6MkhGeGj7u5htkCYjE4PaQ8HUqjYyTmxpDb6Q1MqUpUDsN7\&quot; | [optional] 
 **manage_uuid** | **str**| (任意) 例: \&quot;32bad62a-4186-4d04-a26a-fcee79d5824b\&quot; | [optional] 
 **label** | **str**| (任意) 例: \&quot;did-for-project1\&quot; | [optional] 
 **method** | **str**| (任意) 例: \&quot;did:key | [optional] 
 **exist_private_key** | **bool**| (任意) 例: true | [optional] 
 **description** | **str**| (任意)  | [optional] 
 **domain_name** | **str**| (任意) 例: \&quot;did:web:idroit-dashboard.com\&quot; | [optional] 

### Return type

[**DidInfosResponseDto**](DidInfosResponseDto.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **did_infos_controller_find_one**
> DidInfoResponseDto did_infos_controller_find_one(id)

DID情報詳細取得

リクエストパラメータのidで指定された単一のDID情報の詳細情報の値を返します。

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.DidInfosApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | 

try:
    # DID情報詳細取得
    api_response = api_instance.did_infos_controller_find_one(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DidInfosApi->did_infos_controller_find_one: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**DidInfoResponseDto**](DidInfoResponseDto.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **did_infos_controller_register**
> did_infos_controller_register(body)

既存DID登録

外部で生成されたDIDを本アプリケーションに取り込みます。

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.DidInfosApi(swagger_client.ApiClient(configuration))
body = swagger_client.RegisterDidDto() # RegisterDidDto | 

try:
    # 既存DID登録
    api_instance.did_infos_controller_register(body)
except ApiException as e:
    print("Exception when calling DidInfosApi->did_infos_controller_register: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RegisterDidDto**](RegisterDidDto.md)|  | 

### Return type

void (empty response body)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **did_infos_controller_remove**
> did_infos_controller_remove(id)

DID情報削除

リクエストパラメータのidで指定された単一のDID情報を削除します。

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.DidInfosApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | 

try:
    # DID情報削除
    api_instance.did_infos_controller_remove(id)
except ApiException as e:
    print("Exception when calling DidInfosApi->did_infos_controller_remove: %s\n" % e)
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
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **did_infos_controller_resolve**
> ResolveDidResponseDto did_infos_controller_resolve(body)

DID解決

DIDを解決した結果であるDID Documentの値を返します。このAPIでは保存などの処理を行いません。生成済みのDIDを保存したい場合、既存DID登録API(/did-infos/register)にリクエストを送信してください。

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.DidInfosApi(swagger_client.ApiClient(configuration))
body = swagger_client.ResolveDidDto() # ResolveDidDto | 

try:
    # DID解決
    api_response = api_instance.did_infos_controller_resolve(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DidInfosApi->did_infos_controller_resolve: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ResolveDidDto**](ResolveDidDto.md)|  | 

### Return type

[**ResolveDidResponseDto**](ResolveDidResponseDto.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

