# swagger_client.GroupsApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**groups_controller_connect_did_infos**](GroupsApi.md#groups_controller_connect_did_infos) | **PUT** /api/v1/groups/{id}/did-infos | グループへのDID情報紐付け
[**groups_controller_connect_users**](GroupsApi.md#groups_controller_connect_users) | **PUT** /api/v1/groups/{id}/users | グループへのユーザーアカウント紐付け
[**groups_controller_connect_vc_infos**](GroupsApi.md#groups_controller_connect_vc_infos) | **PUT** /api/v1/groups/{id}/vc-infos | グループへのVC情報紐付け
[**groups_controller_connect_vc_schema**](GroupsApi.md#groups_controller_connect_vc_schema) | **PUT** /api/v1/groups/{id}/vc-schemas | グループへのVCスキーマ紐付け
[**groups_controller_connect_vp_infos**](GroupsApi.md#groups_controller_connect_vp_infos) | **PUT** /api/v1/groups/{id}/vp-infos | グループへのVP情報紐付け
[**groups_controller_create**](GroupsApi.md#groups_controller_create) | **POST** /api/v1/groups | グループ作成
[**groups_controller_disconnect_did_info**](GroupsApi.md#groups_controller_disconnect_did_info) | **DELETE** /api/v1/groups/{id}/did-info/{did_info_id} | グループのDID情報紐付け解除
[**groups_controller_disconnect_user**](GroupsApi.md#groups_controller_disconnect_user) | **DELETE** /api/v1/groups/{id}/user/{user_id} | グループのユーザーアカウント紐付け解除
[**groups_controller_disconnect_vc_info**](GroupsApi.md#groups_controller_disconnect_vc_info) | **DELETE** /api/v1/groups/{id}/vc-info/{vc_info_id} | グループのVC情報紐付け解除
[**groups_controller_disconnect_vc_schema**](GroupsApi.md#groups_controller_disconnect_vc_schema) | **DELETE** /api/v1/groups/{id}/vc-schema/{vc_schema_id} | グループのVCスキーマ紐付け解除
[**groups_controller_disconnect_vp_info**](GroupsApi.md#groups_controller_disconnect_vp_info) | **DELETE** /api/v1/groups/{id}/vp-info/{vp_info_id} | グループのVP情報紐付け解除
[**groups_controller_find_all**](GroupsApi.md#groups_controller_find_all) | **GET** /api/v1/groups | グループ一覧取得
[**groups_controller_find_one**](GroupsApi.md#groups_controller_find_one) | **GET** /api/v1/groups/{id} | グループ詳細取得
[**groups_controller_remove**](GroupsApi.md#groups_controller_remove) | **DELETE** /api/v1/groups/{id} | グループ停止
[**groups_controller_update**](GroupsApi.md#groups_controller_update) | **PUT** /api/v1/groups/{id} | グループ更新

# **groups_controller_connect_did_infos**
> GroupResponseDto groups_controller_connect_did_infos(body, id)

グループへのDID情報紐付け

グループにDID情報を紐付けます。

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.GroupsApi(swagger_client.ApiClient(configuration))
body = swagger_client.ConnectDidInfosDto() # ConnectDidInfosDto | 
id = 'id_example' # str | 

try:
    # グループへのDID情報紐付け
    api_response = api_instance.groups_controller_connect_did_infos(body, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GroupsApi->groups_controller_connect_did_infos: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ConnectDidInfosDto**](ConnectDidInfosDto.md)|  | 
 **id** | **str**|  | 

### Return type

[**GroupResponseDto**](GroupResponseDto.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **groups_controller_connect_users**
> GroupResponseDto groups_controller_connect_users(body, id)

グループへのユーザーアカウント紐付け

グループの所有者、関係者などの管理者としてユーザーアカウントを紐付けます。

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.GroupsApi(swagger_client.ApiClient(configuration))
body = swagger_client.ConnectUsersDto() # ConnectUsersDto | 
id = 'id_example' # str | 

try:
    # グループへのユーザーアカウント紐付け
    api_response = api_instance.groups_controller_connect_users(body, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GroupsApi->groups_controller_connect_users: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ConnectUsersDto**](ConnectUsersDto.md)|  | 
 **id** | **str**|  | 

### Return type

[**GroupResponseDto**](GroupResponseDto.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **groups_controller_connect_vc_infos**
> GroupResponseDto groups_controller_connect_vc_infos(body, id)

グループへのVC情報紐付け

グループにVC情報を紐付けます。

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.GroupsApi(swagger_client.ApiClient(configuration))
body = swagger_client.ConnectVcInfosDto() # ConnectVcInfosDto | 
id = 'id_example' # str | 

try:
    # グループへのVC情報紐付け
    api_response = api_instance.groups_controller_connect_vc_infos(body, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GroupsApi->groups_controller_connect_vc_infos: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ConnectVcInfosDto**](ConnectVcInfosDto.md)|  | 
 **id** | **str**|  | 

### Return type

[**GroupResponseDto**](GroupResponseDto.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **groups_controller_connect_vc_schema**
> GroupResponseDto groups_controller_connect_vc_schema(body, id)

グループへのVCスキーマ紐付け

グループにVCスキーマを紐付けます。

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.GroupsApi(swagger_client.ApiClient(configuration))
body = swagger_client.ConnectVcSchemasDto() # ConnectVcSchemasDto | 
id = 'id_example' # str | 

try:
    # グループへのVCスキーマ紐付け
    api_response = api_instance.groups_controller_connect_vc_schema(body, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GroupsApi->groups_controller_connect_vc_schema: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ConnectVcSchemasDto**](ConnectVcSchemasDto.md)|  | 
 **id** | **str**|  | 

### Return type

[**GroupResponseDto**](GroupResponseDto.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **groups_controller_connect_vp_infos**
> GroupResponseDto groups_controller_connect_vp_infos(body, id)

グループへのVP情報紐付け

グループにVP情報を紐付けます。

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.GroupsApi(swagger_client.ApiClient(configuration))
body = swagger_client.ConnectVpInfosDto() # ConnectVpInfosDto | 
id = 'id_example' # str | 

try:
    # グループへのVP情報紐付け
    api_response = api_instance.groups_controller_connect_vp_infos(body, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GroupsApi->groups_controller_connect_vp_infos: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ConnectVpInfosDto**](ConnectVpInfosDto.md)|  | 
 **id** | **str**|  | 

### Return type

[**GroupResponseDto**](GroupResponseDto.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **groups_controller_create**
> GroupResponseDto groups_controller_create(body)

グループ作成

グループ作成に成功しました。

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.GroupsApi(swagger_client.ApiClient(configuration))
body = swagger_client.CreateGroupDto() # CreateGroupDto | 

try:
    # グループ作成
    api_response = api_instance.groups_controller_create(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GroupsApi->groups_controller_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateGroupDto**](CreateGroupDto.md)|  | 

### Return type

[**GroupResponseDto**](GroupResponseDto.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **groups_controller_disconnect_did_info**
> GroupResponseDto groups_controller_disconnect_did_info(id, did_info_id)

グループのDID情報紐付け解除

グループに紐付いたDID情報の紐付けを解除します。

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.GroupsApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | 
did_info_id = 'did_info_id_example' # str | 

try:
    # グループのDID情報紐付け解除
    api_response = api_instance.groups_controller_disconnect_did_info(id, did_info_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GroupsApi->groups_controller_disconnect_did_info: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **did_info_id** | **str**|  | 

### Return type

[**GroupResponseDto**](GroupResponseDto.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **groups_controller_disconnect_user**
> GroupResponseDto groups_controller_disconnect_user(id, user_id)

グループのユーザーアカウント紐付け解除

グループに紐付いたユーザーアカウントの紐付けを解除します。

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.GroupsApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | 
user_id = 'user_id_example' # str | 

try:
    # グループのユーザーアカウント紐付け解除
    api_response = api_instance.groups_controller_disconnect_user(id, user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GroupsApi->groups_controller_disconnect_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **user_id** | **str**|  | 

### Return type

[**GroupResponseDto**](GroupResponseDto.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **groups_controller_disconnect_vc_info**
> GroupResponseDto groups_controller_disconnect_vc_info(id, vc_info_id)

グループのVC情報紐付け解除

グループに紐付いたVC情報の紐付けを解除します。

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.GroupsApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | 
vc_info_id = 'vc_info_id_example' # str | 

try:
    # グループのVC情報紐付け解除
    api_response = api_instance.groups_controller_disconnect_vc_info(id, vc_info_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GroupsApi->groups_controller_disconnect_vc_info: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **vc_info_id** | **str**|  | 

### Return type

[**GroupResponseDto**](GroupResponseDto.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **groups_controller_disconnect_vc_schema**
> GroupResponseDto groups_controller_disconnect_vc_schema(id, vc_schema_id)

グループのVCスキーマ紐付け解除

グループに紐付いたVCスキーマの紐付けを解除します。

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.GroupsApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | 
vc_schema_id = 'vc_schema_id_example' # str | 

try:
    # グループのVCスキーマ紐付け解除
    api_response = api_instance.groups_controller_disconnect_vc_schema(id, vc_schema_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GroupsApi->groups_controller_disconnect_vc_schema: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **vc_schema_id** | **str**|  | 

### Return type

[**GroupResponseDto**](GroupResponseDto.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **groups_controller_disconnect_vp_info**
> GroupResponseDto groups_controller_disconnect_vp_info(id, vp_info_id)

グループのVP情報紐付け解除

グループに紐付いたVP情報の紐付けを解除します。

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.GroupsApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | 
vp_info_id = 'vp_info_id_example' # str | 

try:
    # グループのVP情報紐付け解除
    api_response = api_instance.groups_controller_disconnect_vp_info(id, vp_info_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GroupsApi->groups_controller_disconnect_vp_info: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **vp_info_id** | **str**|  | 

### Return type

[**GroupResponseDto**](GroupResponseDto.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **groups_controller_find_all**
> GroupsResponseDto groups_controller_find_all(page=page, limit=limit, name=name, status=status)

グループ一覧取得

グループを一覧として値を返します。

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.GroupsApi(swagger_client.ApiClient(configuration))
page = 1.2 # float | (必須) ページネーションを表示する際のページ数に当たるクエリパラメーター。全件取得する際は1を指定。(デフォルト: 1) (optional)
limit = 1.2 # float | (必須) ページネーションを表示する際のページ数あたりに表示する件数を指定するクエリパラメーター。全件取得する際は0を指定。(デフォルト: 10) (optional)
name = 'name_example' # str | (任意)グループの名前。 例: \"Group Project1\" (optional)
status = 'status_example' # str | (任意)グループのステータス。 例: \"active\" (optional)

try:
    # グループ一覧取得
    api_response = api_instance.groups_controller_find_all(page=page, limit=limit, name=name, status=status)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GroupsApi->groups_controller_find_all: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **float**| (必須) ページネーションを表示する際のページ数に当たるクエリパラメーター。全件取得する際は1を指定。(デフォルト: 1) | [optional] 
 **limit** | **float**| (必須) ページネーションを表示する際のページ数あたりに表示する件数を指定するクエリパラメーター。全件取得する際は0を指定。(デフォルト: 10) | [optional] 
 **name** | **str**| (任意)グループの名前。 例: \&quot;Group Project1\&quot; | [optional] 
 **status** | **str**| (任意)グループのステータス。 例: \&quot;active\&quot; | [optional] 

### Return type

[**GroupsResponseDto**](GroupsResponseDto.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **groups_controller_find_one**
> GroupResponseDto groups_controller_find_one(id)

グループ詳細取得

リクエストパラメータのidで指定された単一の管理者アカウントの詳細情報の値を返します。

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.GroupsApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | 

try:
    # グループ詳細取得
    api_response = api_instance.groups_controller_find_one(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GroupsApi->groups_controller_find_one: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**GroupResponseDto**](GroupResponseDto.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **groups_controller_remove**
> groups_controller_remove(id)

グループ停止

リクエストパラメータのidで指定された単一のグループを停止します。

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.GroupsApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | 

try:
    # グループ停止
    api_instance.groups_controller_remove(id)
except ApiException as e:
    print("Exception when calling GroupsApi->groups_controller_remove: %s\n" % e)
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

# **groups_controller_update**
> GroupResponseDto groups_controller_update(id)

グループ更新

リクエストパラメータのidで指定された単一のグループ情報を更新します。

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.GroupsApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | 

try:
    # グループ更新
    api_response = api_instance.groups_controller_update(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GroupsApi->groups_controller_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**GroupResponseDto**](GroupResponseDto.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

