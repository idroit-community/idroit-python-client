# swagger_client.VpInfosApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**vp_infos_controller_add_label**](VpInfosApi.md#vp_infos_controller_add_label) | **PUT** /api/v1/vp-infos/{id}/label | VP情報へのラベル追加
[**vp_infos_controller_connect_user**](VpInfosApi.md#vp_infos_controller_connect_user) | **PUT** /api/v1/vp-infos/{id} | VP情報へのクライアントアカウント紐付け
[**vp_infos_controller_create**](VpInfosApi.md#vp_infos_controller_create) | **POST** /api/v1/vp-infos | 新規VP生成
[**vp_infos_controller_disconnect_user**](VpInfosApi.md#vp_infos_controller_disconnect_user) | **DELETE** /api/v1/vp-infos/{id}/user | VP情報のクライアントアカウント紐付け解除
[**vp_infos_controller_find_all**](VpInfosApi.md#vp_infos_controller_find_all) | **GET** /api/v1/vp-infos | VP情報一覧取得
[**vp_infos_controller_find_one**](VpInfosApi.md#vp_infos_controller_find_one) | **GET** /api/v1/vp-infos/{id} | VP情報詳細取得
[**vp_infos_controller_upload**](VpInfosApi.md#vp_infos_controller_upload) | **POST** /api/v1/vp-infos/upload | 新規VPアップロード

# **vp_infos_controller_add_label**
> VpInfoResponseDto vp_infos_controller_add_label(body, id)

VP情報へのラベル追加

リクエストパラメータのidで指定された単一のVP情報に対して、任意の管理用ラベルを追加します。

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.VpInfosApi(swagger_client.ApiClient(configuration))
body = swagger_client.AddLabelToVpInfoDto() # AddLabelToVpInfoDto | 
id = 'id_example' # str | 

try:
    # VP情報へのラベル追加
    api_response = api_instance.vp_infos_controller_add_label(body, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VpInfosApi->vp_infos_controller_add_label: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AddLabelToVpInfoDto**](AddLabelToVpInfoDto.md)|  | 
 **id** | **str**|  | 

### Return type

[**VpInfoResponseDto**](VpInfoResponseDto.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **vp_infos_controller_connect_user**
> vp_infos_controller_connect_user(body, id)

VP情報へのクライアントアカウント紐付け

VP情報の所有者、関係者などの管理者としてクライアントアカウントを紐付けます。

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.VpInfosApi(swagger_client.ApiClient(configuration))
body = swagger_client.UpdateVcInfoDto() # UpdateVcInfoDto | 
id = 'id_example' # str | 

try:
    # VP情報へのクライアントアカウント紐付け
    api_instance.vp_infos_controller_connect_user(body, id)
except ApiException as e:
    print("Exception when calling VpInfosApi->vp_infos_controller_connect_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UpdateVcInfoDto**](UpdateVcInfoDto.md)|  | 
 **id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **vp_infos_controller_create**
> vp_infos_controller_create(body)

新規VP生成

新規VPを生成します。

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.VpInfosApi(swagger_client.ApiClient(configuration))
body = swagger_client.CreateVpInfoDto() # CreateVpInfoDto | 

try:
    # 新規VP生成
    api_instance.vp_infos_controller_create(body)
except ApiException as e:
    print("Exception when calling VpInfosApi->vp_infos_controller_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateVpInfoDto**](CreateVpInfoDto.md)|  | 

### Return type

void (empty response body)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **vp_infos_controller_disconnect_user**
> vp_infos_controller_disconnect_user(id)

VP情報のクライアントアカウント紐付け解除

VP情報に紐付いたクライアントアカウントの紐付けを解除します。

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.VpInfosApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | 

try:
    # VP情報のクライアントアカウント紐付け解除
    api_instance.vp_infos_controller_disconnect_user(id)
except ApiException as e:
    print("Exception when calling VpInfosApi->vp_infos_controller_disconnect_user: %s\n" % e)
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

# **vp_infos_controller_find_all**
> VpInfoResponseDto vp_infos_controller_find_all(page=page, limit=limit, label=label, description=description)

VP情報一覧取得

アプリケーションが管理するVP情報を一覧として値を返します。

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.VpInfosApi(swagger_client.ApiClient(configuration))
page = 1.2 # float | (必須) ページネーションを表示する際のページ数に当たるクエリパラメーター。全件取得する際は1を指定。(デフォルト: 1) (optional)
limit = 1.2 # float | (必須) ページネーションを表示する際のページ数あたりに表示する件数を指定するクエリパラメーター。全件取得する際は0を指定。(デフォルト: 10) (optional)
label = 'label_example' # str | (任意) 例: \"vc-for-project1\" (optional)
description = 'description_example' # str | (任意)  (optional)

try:
    # VP情報一覧取得
    api_response = api_instance.vp_infos_controller_find_all(page=page, limit=limit, label=label, description=description)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VpInfosApi->vp_infos_controller_find_all: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **float**| (必須) ページネーションを表示する際のページ数に当たるクエリパラメーター。全件取得する際は1を指定。(デフォルト: 1) | [optional] 
 **limit** | **float**| (必須) ページネーションを表示する際のページ数あたりに表示する件数を指定するクエリパラメーター。全件取得する際は0を指定。(デフォルト: 10) | [optional] 
 **label** | **str**| (任意) 例: \&quot;vc-for-project1\&quot; | [optional] 
 **description** | **str**| (任意)  | [optional] 

### Return type

[**VpInfoResponseDto**](VpInfoResponseDto.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **vp_infos_controller_find_one**
> VpInfoDetailDto vp_infos_controller_find_one(id)

VP情報詳細取得

リクエストパラメータのidで指定された単一のVP情報の詳細情報の値を返します。

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.VpInfosApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | 

try:
    # VP情報詳細取得
    api_response = api_instance.vp_infos_controller_find_one(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VpInfosApi->vp_infos_controller_find_one: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**VpInfoDetailDto**](VpInfoDetailDto.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **vp_infos_controller_upload**
> VpInfoResponseDto vp_infos_controller_upload(credential_object, label, description)

新規VPアップロード

外部で発行された既存VPをアップロードし、本アプリケーションに保存します。。

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.VpInfosApi(swagger_client.ApiClient(configuration))
credential_object = NULL # object | 
label = 'label_example' # str | 
description = 'description_example' # str | 

try:
    # 新規VPアップロード
    api_response = api_instance.vp_infos_controller_upload(credential_object, label, description)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VpInfosApi->vp_infos_controller_upload: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **credential_object** | [**object**](.md)|  | 
 **label** | **str**|  | 
 **description** | **str**|  | 

### Return type

[**VpInfoResponseDto**](VpInfoResponseDto.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

