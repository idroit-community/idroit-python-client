# swagger_client.MailsApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**mails_controller_find_all**](MailsApi.md#mails_controller_find_all) | **GET** /api/v1/mails | 送信済みメール一覧取得
[**mails_controller_find_one**](MailsApi.md#mails_controller_find_one) | **GET** /api/v1/mails/{id} | 送信済みメール詳細取得
[**mails_controller_send**](MailsApi.md#mails_controller_send) | **POST** /api/v1/mails | 新規単一メール送信
[**mails_controller_send_batch**](MailsApi.md#mails_controller_send_batch) | **POST** /api/v1/mails/batch | 新規複数メールバッチ送信

# **mails_controller_find_all**
> MailsResponseDto mails_controller_find_all(page=page, limit=limit)

送信済みメール一覧取得

送信済みメールを一覧として値を返します。

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.MailsApi(swagger_client.ApiClient(configuration))
page = 1.2 # float | (必須) ページネーションを表示する際のページ数に当たるクエリパラメーター。全件取得する際は1を指定。(デフォルト: 1) (optional)
limit = 1.2 # float | (必須) ページネーションを表示する際のページ数あたりに表示する件数を指定するクエリパラメーター。全件取得する際は0を指定。(デフォルト: 10) (optional)

try:
    # 送信済みメール一覧取得
    api_response = api_instance.mails_controller_find_all(page=page, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MailsApi->mails_controller_find_all: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **float**| (必須) ページネーションを表示する際のページ数に当たるクエリパラメーター。全件取得する際は1を指定。(デフォルト: 1) | [optional] 
 **limit** | **float**| (必須) ページネーションを表示する際のページ数あたりに表示する件数を指定するクエリパラメーター。全件取得する際は0を指定。(デフォルト: 10) | [optional] 

### Return type

[**MailsResponseDto**](MailsResponseDto.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **mails_controller_find_one**
> Mail mails_controller_find_one(id)

送信済みメール詳細取得

リクエストパラメータのidで指定された単一の送信済みメールの詳細情報の値を返します。

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.MailsApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | 

try:
    # 送信済みメール詳細取得
    api_response = api_instance.mails_controller_find_one(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MailsApi->mails_controller_find_one: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**Mail**](Mail.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **mails_controller_send**
> mails_controller_send(body)

新規単一メール送信

新規単一メールを作成し、送信します。

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.MailsApi(swagger_client.ApiClient(configuration))
body = swagger_client.SendMailDto() # SendMailDto | 

try:
    # 新規単一メール送信
    api_instance.mails_controller_send(body)
except ApiException as e:
    print("Exception when calling MailsApi->mails_controller_send: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SendMailDto**](SendMailDto.md)|  | 

### Return type

void (empty response body)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **mails_controller_send_batch**
> mails_controller_send_batch(body)

新規複数メールバッチ送信

新規メールを複数作成し、送信します。

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.MailsApi(swagger_client.ApiClient(configuration))
body = swagger_client.SendMailBatchDto() # SendMailBatchDto | 

try:
    # 新規複数メールバッチ送信
    api_instance.mails_controller_send_batch(body)
except ApiException as e:
    print("Exception when calling MailsApi->mails_controller_send_batch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SendMailBatchDto**](SendMailBatchDto.md)|  | 

### Return type

void (empty response body)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

