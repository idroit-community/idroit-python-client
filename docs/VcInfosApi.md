# swagger_client.VcInfosApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**vc_infos_controller_add_label**](VcInfosApi.md#vc_infos_controller_add_label) | **PUT** /api/v1/vc-infos/{id}/label | VC情報へのラベル追加
[**vc_infos_controller_connect_user**](VcInfosApi.md#vc_infos_controller_connect_user) | **PUT** /api/v1/vc-infos/{id} | VC情報へのクライアントアカウント紐付け
[**vc_infos_controller_create**](VcInfosApi.md#vc_infos_controller_create) | **POST** /api/v1/vc-infos | 新規VC発行
[**vc_infos_controller_disconnect_user**](VcInfosApi.md#vc_infos_controller_disconnect_user) | **DELETE** /api/v1/vc-infos/{id}/user | VC情報のクライアントアカウント紐付け解除
[**vc_infos_controller_find_all**](VcInfosApi.md#vc_infos_controller_find_all) | **GET** /api/v1/vc-infos | VC情報一覧取得
[**vc_infos_controller_find_one**](VcInfosApi.md#vc_infos_controller_find_one) | **GET** /api/v1/vc-infos/{id} | VC情報詳細取得
[**vc_infos_controller_generate_vp**](VcInfosApi.md#vc_infos_controller_generate_vp) | **POST** /api/v1/vc-infos/{id} | 新規VP情報生成
[**vc_infos_controller_issue**](VcInfosApi.md#vc_infos_controller_issue) | **POST** /api/v1/vc-infos/issue | 新規VC発行(スキーマなし)
[**vc_infos_controller_upload**](VcInfosApi.md#vc_infos_controller_upload) | **POST** /api/v1/vc-infos/upload | 新規VCアップロード

# **vc_infos_controller_add_label**
> VcInfoResponseDto vc_infos_controller_add_label(body, id)

VC情報へのラベル追加

リクエストパラメータのidで指定された単一のVC情報に対して、任意の管理用ラベルを追加します。

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.VcInfosApi(swagger_client.ApiClient(configuration))
body = swagger_client.AddLabelToVcInfoDto() # AddLabelToVcInfoDto | 
id = 'id_example' # str | 

try:
    # VC情報へのラベル追加
    api_response = api_instance.vc_infos_controller_add_label(body, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VcInfosApi->vc_infos_controller_add_label: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AddLabelToVcInfoDto**](AddLabelToVcInfoDto.md)|  | 
 **id** | **str**|  | 

### Return type

[**VcInfoResponseDto**](VcInfoResponseDto.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **vc_infos_controller_connect_user**
> vc_infos_controller_connect_user(body, id)

VC情報へのクライアントアカウント紐付け

VC情報の所有者、関係者などの管理者としてクライアントアカウントを紐付けます。

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.VcInfosApi(swagger_client.ApiClient(configuration))
body = swagger_client.UpdateVcInfoDto() # UpdateVcInfoDto | 
id = 'id_example' # str | 

try:
    # VC情報へのクライアントアカウント紐付け
    api_instance.vc_infos_controller_connect_user(body, id)
except ApiException as e:
    print("Exception when calling VcInfosApi->vc_infos_controller_connect_user: %s\n" % e)
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

# **vc_infos_controller_create**
> VcInfoResponseDto vc_infos_controller_create(body)

新規VC発行

新規VCを発行します。

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.VcInfosApi(swagger_client.ApiClient(configuration))
body = swagger_client.CreateVcInfoDto() # CreateVcInfoDto | 

try:
    # 新規VC発行
    api_response = api_instance.vc_infos_controller_create(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VcInfosApi->vc_infos_controller_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateVcInfoDto**](CreateVcInfoDto.md)|  | 

### Return type

[**VcInfoResponseDto**](VcInfoResponseDto.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **vc_infos_controller_disconnect_user**
> vc_infos_controller_disconnect_user(id)

VC情報のクライアントアカウント紐付け解除

VC情報に紐付いたクライアントアカウントの紐付けを解除します。

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.VcInfosApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | 

try:
    # VC情報のクライアントアカウント紐付け解除
    api_instance.vc_infos_controller_disconnect_user(id)
except ApiException as e:
    print("Exception when calling VcInfosApi->vc_infos_controller_disconnect_user: %s\n" % e)
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

# **vc_infos_controller_find_all**
> VcInfosResponseDto vc_infos_controller_find_all(page=page, limit=limit, label=label, description=description)

VC情報一覧取得

アプリケーションが管理するVC情報を一覧として値を返します。

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.VcInfosApi(swagger_client.ApiClient(configuration))
page = 1.2 # float | (必須) ページネーションを表示する際のページ数に当たるクエリパラメーター。全件取得する際は1を指定。(デフォルト: 1) (optional)
limit = 1.2 # float | (必須) ページネーションを表示する際のページ数あたりに表示する件数を指定するクエリパラメーター。全件取得する際は0を指定。(デフォルト: 10) (optional)
label = 'label_example' # str | (任意) 例: \"vc-for-project1\" (optional)
description = 'description_example' # str | (任意)  (optional)

try:
    # VC情報一覧取得
    api_response = api_instance.vc_infos_controller_find_all(page=page, limit=limit, label=label, description=description)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VcInfosApi->vc_infos_controller_find_all: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **float**| (必須) ページネーションを表示する際のページ数に当たるクエリパラメーター。全件取得する際は1を指定。(デフォルト: 1) | [optional] 
 **limit** | **float**| (必須) ページネーションを表示する際のページ数あたりに表示する件数を指定するクエリパラメーター。全件取得する際は0を指定。(デフォルト: 10) | [optional] 
 **label** | **str**| (任意) 例: \&quot;vc-for-project1\&quot; | [optional] 
 **description** | **str**| (任意)  | [optional] 

### Return type

[**VcInfosResponseDto**](VcInfosResponseDto.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **vc_infos_controller_find_one**
> VcInfoResponseDto vc_infos_controller_find_one(id)

VC情報詳細取得

リクエストパラメータのidで指定された単一のVC情報の詳細情報の値を返します。

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.VcInfosApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | 

try:
    # VC情報詳細取得
    api_response = api_instance.vc_infos_controller_find_one(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VcInfosApi->vc_infos_controller_find_one: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**VcInfoResponseDto**](VcInfoResponseDto.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **vc_infos_controller_generate_vp**
> VcInfoResponseDto vc_infos_controller_generate_vp(body, id)

新規VP情報生成

リクエストパラメータのidで指定されたVC情報から新規VPを発行します。

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.VcInfosApi(swagger_client.ApiClient(configuration))
body = swagger_client.GenerateVpDto() # GenerateVpDto | 
id = 'id_example' # str | 

try:
    # 新規VP情報生成
    api_response = api_instance.vc_infos_controller_generate_vp(body, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VcInfosApi->vc_infos_controller_generate_vp: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**GenerateVpDto**](GenerateVpDto.md)|  | 
 **id** | **str**|  | 

### Return type

[**VcInfoResponseDto**](VcInfoResponseDto.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **vc_infos_controller_issue**
> VcInfoResponseDto vc_infos_controller_issue(body)

新規VC発行(スキーマなし)

VCスキーマを指定せず直接新規VCを発行します。

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.VcInfosApi(swagger_client.ApiClient(configuration))
body = swagger_client.IssueVcInfoDto() # IssueVcInfoDto | 

try:
    # 新規VC発行(スキーマなし)
    api_response = api_instance.vc_infos_controller_issue(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VcInfosApi->vc_infos_controller_issue: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**IssueVcInfoDto**](IssueVcInfoDto.md)|  | 

### Return type

[**VcInfoResponseDto**](VcInfoResponseDto.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **vc_infos_controller_upload**
> VcInfoResponseDto vc_infos_controller_upload(credential_object, label, description)

新規VCアップロード

外部で発行された既存VCをアップロードし、本アプリケーションに保存します。。

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.VcInfosApi(swagger_client.ApiClient(configuration))
credential_object = NULL # object | 
label = 'label_example' # str | 
description = 'description_example' # str | 

try:
    # 新規VCアップロード
    api_response = api_instance.vc_infos_controller_upload(credential_object, label, description)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VcInfosApi->vc_infos_controller_upload: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **credential_object** | [**object**](.md)|  | 
 **label** | **str**|  | 
 **description** | **str**|  | 

### Return type

[**VcInfoResponseDto**](VcInfoResponseDto.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

