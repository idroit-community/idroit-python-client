# swagger_client.FilesApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**files_controller_download**](FilesApi.md#files_controller_download) | **GET** /api/v1/files/{id}/download | ファイルダウンロード
[**files_controller_execute_csv**](FilesApi.md#files_controller_execute_csv) | **POST** /api/v1/files/{id} | CSVファイル実行
[**files_controller_find_all**](FilesApi.md#files_controller_find_all) | **GET** /api/v1/files | ファイル一覧取得
[**files_controller_find_one**](FilesApi.md#files_controller_find_one) | **GET** /api/v1/files/{id} | ファイル詳細取得
[**files_controller_remove**](FilesApi.md#files_controller_remove) | **DELETE** /api/v1/files/{id} | ファイル削除
[**files_controller_upload_file**](FilesApi.md#files_controller_upload_file) | **POST** /api/v1/files | ファイルアップロード

# **files_controller_download**
> str files_controller_download(id)

ファイルダウンロード

リクエストパラメータのidで指定された単一のファイルのバイナリデータを返します。

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.FilesApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | 

try:
    # ファイルダウンロード
    api_response = api_instance.files_controller_download(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FilesApi->files_controller_download: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

**str**

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **files_controller_execute_csv**
> files_controller_execute_csv(body, id)

CSVファイル実行

(非推奨) ユーザー、クライアント情報を記載したCSVファイルを実行し、新規アカウントを作成します。

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.FilesApi(swagger_client.ApiClient(configuration))
body = swagger_client.CreateDidDto() # CreateDidDto | 
id = 'id_example' # str | 

try:
    # CSVファイル実行
    api_instance.files_controller_execute_csv(body, id)
except ApiException as e:
    print("Exception when calling FilesApi->files_controller_execute_csv: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateDidDto**](CreateDidDto.md)|  | 
 **id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **files_controller_find_all**
> FilesResponseDto files_controller_find_all(page=page, limit=limit, filename=filename, originalname=originalname, executed=executed, type=type, status=status)

ファイル一覧取得

ファイルを一覧として値を返します。

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.FilesApi(swagger_client.ApiClient(configuration))
page = 1.2 # float | (必須) ページネーションを表示する際のページ数に当たるクエリパラメーター。全件取得する際は1を指定。(デフォルト: 1) (optional)
limit = 1.2 # float | (必須) ページネーションを表示する際のページ数あたりに表示する件数を指定するクエリパラメーター。全件取得する際は0を指定。(デフォルト: 10) (optional)
filename = 'filename_example' # str | (任意) 例: \"file-1732019975229-394515535.png\" (optional)
originalname = 'originalname_example' # str | (任意) 例: \"english-badge.png\" (optional)
executed = true # bool | (任意) 例: true (optional)
type = 'type_example' # str | (任意) 例: \"image/png\" (optional)
status = 1.2 # float | (任意) 例: 0 (optional)

try:
    # ファイル一覧取得
    api_response = api_instance.files_controller_find_all(page=page, limit=limit, filename=filename, originalname=originalname, executed=executed, type=type, status=status)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FilesApi->files_controller_find_all: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **float**| (必須) ページネーションを表示する際のページ数に当たるクエリパラメーター。全件取得する際は1を指定。(デフォルト: 1) | [optional] 
 **limit** | **float**| (必須) ページネーションを表示する際のページ数あたりに表示する件数を指定するクエリパラメーター。全件取得する際は0を指定。(デフォルト: 10) | [optional] 
 **filename** | **str**| (任意) 例: \&quot;file-1732019975229-394515535.png\&quot; | [optional] 
 **originalname** | **str**| (任意) 例: \&quot;english-badge.png\&quot; | [optional] 
 **executed** | **bool**| (任意) 例: true | [optional] 
 **type** | **str**| (任意) 例: \&quot;image/png\&quot; | [optional] 
 **status** | **float**| (任意) 例: 0 | [optional] 

### Return type

[**FilesResponseDto**](FilesResponseDto.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **files_controller_find_one**
> FileResponseDto files_controller_find_one(id)

ファイル詳細取得

リクエストパラメータのidで指定された単一のファイルの詳細情報の値を返します。

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.FilesApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | 

try:
    # ファイル詳細取得
    api_response = api_instance.files_controller_find_one(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FilesApi->files_controller_find_one: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**FileResponseDto**](FileResponseDto.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **files_controller_remove**
> files_controller_remove(id)

ファイル削除

リクエストパラメータのidで指定された単一のファイルを削除します。

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.FilesApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | 

try:
    # ファイル削除
    api_instance.files_controller_remove(id)
except ApiException as e:
    print("Exception when calling FilesApi->files_controller_remove: %s\n" % e)
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

# **files_controller_upload_file**
> FileResponseDto files_controller_upload_file(file)

ファイルアップロード

新規ファイルアップロードを作成します。

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.FilesApi(swagger_client.ApiClient(configuration))
file = 'file_example' # str | 

try:
    # ファイルアップロード
    api_response = api_instance.files_controller_upload_file(file)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FilesApi->files_controller_upload_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file** | **str**|  | 

### Return type

[**FileResponseDto**](FileResponseDto.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

