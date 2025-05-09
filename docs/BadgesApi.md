# swagger_client.BadgesApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**badges_controller_add_label**](BadgesApi.md#badges_controller_add_label) | **PUT** /api/v1/badges/{id}/label | Badgeへのラベル追加
[**badges_controller_create**](BadgesApi.md#badges_controller_create) | **POST** /api/v1/badges | 新規バッジ発行
[**badges_controller_download**](BadgesApi.md#badges_controller_download) | **GET** /api/v1/badges/{id}/download | バッジダウンロード
[**badges_controller_file_verify**](BadgesApi.md#badges_controller_file_verify) | **POST** /api/v1/badges/file | バッジファイル検証
[**badges_controller_find_all**](BadgesApi.md#badges_controller_find_all) | **GET** /api/v1/badges | バッジ一覧取得
[**badges_controller_find_one**](BadgesApi.md#badges_controller_find_one) | **GET** /api/v1/badges/{id} | バッジ詳細取得
[**badges_controller_verify**](BadgesApi.md#badges_controller_verify) | **PUT** /api/v1/badges/{id}/verify | バッジ検証

# **badges_controller_add_label**
> BadgeResponseDto badges_controller_add_label(body, id)

Badgeへのラベル追加

リクエストパラメータのidで指定された単一のBadgeに対して、任意の管理用ラベルを追加します。

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.BadgesApi(swagger_client.ApiClient(configuration))
body = swagger_client.AddLabelToBadgeDto() # AddLabelToBadgeDto | 
id = 'id_example' # str | 

try:
    # Badgeへのラベル追加
    api_response = api_instance.badges_controller_add_label(body, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BadgesApi->badges_controller_add_label: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AddLabelToBadgeDto**](AddLabelToBadgeDto.md)|  | 
 **id** | **str**|  | 

### Return type

[**BadgeResponseDto**](BadgeResponseDto.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **badges_controller_create**
> BadgeResponseDto badges_controller_create(body)

新規バッジ発行

新規バッジを発行します。

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.BadgesApi(swagger_client.ApiClient(configuration))
body = swagger_client.CreateBadgeDto() # CreateBadgeDto | 

try:
    # 新規バッジ発行
    api_response = api_instance.badges_controller_create(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BadgesApi->badges_controller_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateBadgeDto**](CreateBadgeDto.md)|  | 

### Return type

[**BadgeResponseDto**](BadgeResponseDto.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **badges_controller_download**
> str badges_controller_download(id, vp_info_id)

バッジダウンロード

リクエストパラメータのidで指定された単一のバッジ画像のバイナリデータを返します。

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.BadgesApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | 
vp_info_id = 'vp_info_id_example' # str | 

try:
    # バッジダウンロード
    api_response = api_instance.badges_controller_download(id, vp_info_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BadgesApi->badges_controller_download: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **vp_info_id** | **str**|  | 

### Return type

**str**

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **badges_controller_file_verify**
> VerifiyBadgeFileReponseDto badges_controller_file_verify(file)

バッジファイル検証

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.BadgesApi(swagger_client.ApiClient(configuration))
file = 'file_example' # str | 

try:
    # バッジファイル検証
    api_response = api_instance.badges_controller_file_verify(file)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BadgesApi->badges_controller_file_verify: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file** | **str**|  | 

### Return type

[**VerifiyBadgeFileReponseDto**](VerifiyBadgeFileReponseDto.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **badges_controller_find_all**
> BadgesResponseDto badges_controller_find_all(page=page, limit=limit, label=label, filename=filename, description=description, status=status)

バッジ一覧取得

アプリケーションが管理するバッジ情報を一覧として値を返します。

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.BadgesApi(swagger_client.ApiClient(configuration))
page = 1.2 # float | (必須) ページネーションを表示する際のページ数に当たるクエリパラメーター。全件取得する際は1を指定。(デフォルト: 1) (optional)
limit = 1.2 # float | (必須) ページネーションを表示する際のページ数あたりに表示する件数を指定するクエリパラメーター。全件取得する際は0を指定。(デフォルト: 10) (optional)
label = 'label_example' # str | (任意) 例: \"sample-badge-1\" (optional)
filename = 'filename_example' # str | (任意) 例: \"badge-12345-12345.png\" (optional)
description = 'description_example' # str | (任意)  (optional)
status = 1.2 # float | (任意) 例: 1 (optional)

try:
    # バッジ一覧取得
    api_response = api_instance.badges_controller_find_all(page=page, limit=limit, label=label, filename=filename, description=description, status=status)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BadgesApi->badges_controller_find_all: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **float**| (必須) ページネーションを表示する際のページ数に当たるクエリパラメーター。全件取得する際は1を指定。(デフォルト: 1) | [optional] 
 **limit** | **float**| (必須) ページネーションを表示する際のページ数あたりに表示する件数を指定するクエリパラメーター。全件取得する際は0を指定。(デフォルト: 10) | [optional] 
 **label** | **str**| (任意) 例: \&quot;sample-badge-1\&quot; | [optional] 
 **filename** | **str**| (任意) 例: \&quot;badge-12345-12345.png\&quot; | [optional] 
 **description** | **str**| (任意)  | [optional] 
 **status** | **float**| (任意) 例: 1 | [optional] 

### Return type

[**BadgesResponseDto**](BadgesResponseDto.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **badges_controller_find_one**
> BadgeResponseDto badges_controller_find_one(id)

バッジ詳細取得

リクエストパラメータのidで指定された単一のバッジ情報の詳細情報の値を返します。

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.BadgesApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | 

try:
    # バッジ詳細取得
    api_response = api_instance.badges_controller_find_one(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BadgesApi->badges_controller_find_one: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**BadgeResponseDto**](BadgeResponseDto.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **badges_controller_verify**
> VerifiyBadgeReponseDto badges_controller_verify(body, id)

バッジ検証

バッジのVC/VPの検証を実行します。

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.BadgesApi(swagger_client.ApiClient(configuration))
body = swagger_client.VerifyBadgeDto() # VerifyBadgeDto | 
id = 'id_example' # str | 

try:
    # バッジ検証
    api_response = api_instance.badges_controller_verify(body, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BadgesApi->badges_controller_verify: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**VerifyBadgeDto**](VerifyBadgeDto.md)|  | 
 **id** | **str**|  | 

### Return type

[**VerifiyBadgeReponseDto**](VerifiyBadgeReponseDto.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

