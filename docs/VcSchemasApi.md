# swagger_client.VcSchemasApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**vc_schemas_controller_create**](VcSchemasApi.md#vc_schemas_controller_create) | **POST** /api/v1/vc-schemas | 新規VCスキーマ作成
[**vc_schemas_controller_find_all**](VcSchemasApi.md#vc_schemas_controller_find_all) | **GET** /api/v1/vc-schemas | VCスキーマ一覧取得
[**vc_schemas_controller_find_one**](VcSchemasApi.md#vc_schemas_controller_find_one) | **GET** /api/v1/vc-schemas/{id} | VCスキーマ情報詳細取得
[**vc_schemas_controller_update**](VcSchemasApi.md#vc_schemas_controller_update) | **PUT** /api/v1/vc-schemas/{id} | VCスキーマへのグループ紐付け

# **vc_schemas_controller_create**
> VcSchemaResponseDto vc_schemas_controller_create(body)

新規VCスキーマ作成

新規VCスキーマを作成します。

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.VcSchemasApi(swagger_client.ApiClient(configuration))
body = swagger_client.CreateVcSchemaDto() # CreateVcSchemaDto | 

try:
    # 新規VCスキーマ作成
    api_response = api_instance.vc_schemas_controller_create(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VcSchemasApi->vc_schemas_controller_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateVcSchemaDto**](CreateVcSchemaDto.md)|  | 

### Return type

[**VcSchemaResponseDto**](VcSchemaResponseDto.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **vc_schemas_controller_find_all**
> VcSchemasResponseDto vc_schemas_controller_find_all(page=page, limit=limit, title=title, version=version, description=description, is_badge_schema=is_badge_schema)

VCスキーマ一覧取得

VCスキーマを一覧として値を返します。

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.VcSchemasApi(swagger_client.ApiClient(configuration))
page = 1.2 # float | (必須) ページネーションを表示する際のページ数に当たるクエリパラメーター。全件取得する際は1を指定。(デフォルト: 1) (optional)
limit = 1.2 # float | (必須) ページネーションを表示する際のページ数あたりに表示する件数を指定するクエリパラメーター。全件取得する際は0を指定。(デフォルト: 10) (optional)
title = 'title_example' # str | (任意) 例: \"Schema Sample\" (optional)
version = 'version_example' # str | (任意) 例: \"1.0.0\" (optional)
description = 'description_example' # str | (任意) 例:  (optional)
is_badge_schema = true # bool | (任意) 例: true (optional)

try:
    # VCスキーマ一覧取得
    api_response = api_instance.vc_schemas_controller_find_all(page=page, limit=limit, title=title, version=version, description=description, is_badge_schema=is_badge_schema)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VcSchemasApi->vc_schemas_controller_find_all: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **float**| (必須) ページネーションを表示する際のページ数に当たるクエリパラメーター。全件取得する際は1を指定。(デフォルト: 1) | [optional] 
 **limit** | **float**| (必須) ページネーションを表示する際のページ数あたりに表示する件数を指定するクエリパラメーター。全件取得する際は0を指定。(デフォルト: 10) | [optional] 
 **title** | **str**| (任意) 例: \&quot;Schema Sample\&quot; | [optional] 
 **version** | **str**| (任意) 例: \&quot;1.0.0\&quot; | [optional] 
 **description** | **str**| (任意) 例:  | [optional] 
 **is_badge_schema** | **bool**| (任意) 例: true | [optional] 

### Return type

[**VcSchemasResponseDto**](VcSchemasResponseDto.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **vc_schemas_controller_find_one**
> VcSchemaResponseDto vc_schemas_controller_find_one(id)

VCスキーマ情報詳細取得

リクエストパラメータのidで指定された単一のVCスキーマの詳細情報の値を返します。

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.VcSchemasApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | 

try:
    # VCスキーマ情報詳細取得
    api_response = api_instance.vc_schemas_controller_find_one(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VcSchemasApi->vc_schemas_controller_find_one: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**VcSchemaResponseDto**](VcSchemaResponseDto.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **vc_schemas_controller_update**
> VcSchemaResponseDto vc_schemas_controller_update(body, id)

VCスキーマへのグループ紐付け

VCスキーマに関連するグループを紐付けます。

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.VcSchemasApi(swagger_client.ApiClient(configuration))
body = swagger_client.UpdateVcSchemaDto() # UpdateVcSchemaDto | 
id = 'id_example' # str | 

try:
    # VCスキーマへのグループ紐付け
    api_response = api_instance.vc_schemas_controller_update(body, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VcSchemasApi->vc_schemas_controller_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UpdateVcSchemaDto**](UpdateVcSchemaDto.md)|  | 
 **id** | **str**|  | 

### Return type

[**VcSchemaResponseDto**](VcSchemaResponseDto.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

