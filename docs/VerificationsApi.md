# swagger_client.VerificationsApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**verifications_controller_create**](VerificationsApi.md#verifications_controller_create) | **POST** /api/v1/verifications | VC/VP検証
[**verifications_controller_find_all**](VerificationsApi.md#verifications_controller_find_all) | **GET** /api/v1/verifications | VC/VP検証結果一覧取得
[**verifications_controller_find_one**](VerificationsApi.md#verifications_controller_find_one) | **GET** /api/v1/verifications/{id} | VC/VP検証結果詳細取得

# **verifications_controller_create**
> VerificationResponseDto verifications_controller_create(body)

VC/VP検証

VC/VPの検証を実行します。

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.VerificationsApi(swagger_client.ApiClient(configuration))
body = swagger_client.VerificationDto() # VerificationDto | 

try:
    # VC/VP検証
    api_response = api_instance.verifications_controller_create(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VerificationsApi->verifications_controller_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**VerificationDto**](VerificationDto.md)|  | 

### Return type

[**VerificationResponseDto**](VerificationResponseDto.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **verifications_controller_find_all**
> VerificationsResponseDto verifications_controller_find_all(page=page, limit=limit, label=label, result=result)

VC/VP検証結果一覧取得

アプリケーションが管理するVC/VP検証結果を一覧として値を返します。

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.VerificationsApi(swagger_client.ApiClient(configuration))
page = 1.2 # float | (必須) ページネーションを表示する際のページ数に当たるクエリパラメーター。全件取得する際は1を指定。(デフォルト: 1) (optional)
limit = 1.2 # float | (必須) ページネーションを表示する際のページ数あたりに表示する件数を指定するクエリパラメーター。全件取得する際は0を指定。(デフォルト: 10) (optional)
label = 'label_example' # str | (任意) 例: \"verification-for-project1\" (optional)
result = true # bool | (任意) 例: true (optional)

try:
    # VC/VP検証結果一覧取得
    api_response = api_instance.verifications_controller_find_all(page=page, limit=limit, label=label, result=result)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VerificationsApi->verifications_controller_find_all: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **float**| (必須) ページネーションを表示する際のページ数に当たるクエリパラメーター。全件取得する際は1を指定。(デフォルト: 1) | [optional] 
 **limit** | **float**| (必須) ページネーションを表示する際のページ数あたりに表示する件数を指定するクエリパラメーター。全件取得する際は0を指定。(デフォルト: 10) | [optional] 
 **label** | **str**| (任意) 例: \&quot;verification-for-project1\&quot; | [optional] 
 **result** | **bool**| (任意) 例: true | [optional] 

### Return type

[**VerificationsResponseDto**](VerificationsResponseDto.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **verifications_controller_find_one**
> VerificationResponseDto verifications_controller_find_one(id)

VC/VP検証結果詳細取得

リクエストパラメータのidで指定された単一のVC/VP検証結果の詳細情報の値を返します。

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.VerificationsApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | 

try:
    # VC/VP検証結果詳細取得
    api_response = api_instance.verifications_controller_find_one(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VerificationsApi->verifications_controller_find_one: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**VerificationResponseDto**](VerificationResponseDto.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

