# swagger-client
     これは[株式会社フォアー](https://www.fore-co.ltd/ja/)が開発するを使ったDecentralizd Identifiers / Verifiable Credentials(DID/VC)に関係する機能を簡単に利用するための REST API です。現在以下のユースケースをサポートしています。これは今後も拡張されていきます。     - DIDの生成:      - グループ管理機能       - (企業/プロジェクトのまとまり)ごとにユーザー、クライアント、証明書(VC)スキーマを紐付けて管理する。          詳細は以下を参照してください。     - [idroit dashboard admin UI](https://admin.idroit-dashboard.com)     - [idroit dashboard公式ホームページ]()     - [idroit dashboard操作マニュアル]()      以下は関連リンクです。     - [Universal Resolver](https://dev.uniresolver.io/)     - [W3C DID Core 1.0](https://www.w3.org/TR/did-core/)     - [Verifiable Credentials Data Model v2.0](https://www.w3.org/TR/vc-data-model-2.0/)   

This Python package is automatically generated by the [Swagger Codegen](https://github.com/swagger-api/swagger-codegen) project:

- API version: 0.9.2
- Package version: 1.0.0
- Build package: io.swagger.codegen.v3.generators.python.PythonClientCodegen

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

If the python package is hosted on Github, you can install directly from Github

```sh
pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

Then import the package:
```python
import swagger_client 
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import swagger_client
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.AuthApi(swagger_client.ApiClient(configuration))

try:
    # ログイン済みのアカウント情報取得
    api_response = api_instance.auth_controller_get_profile()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthApi->auth_controller_get_profile: %s\n" % e)


# create an instance of the API class
api_instance = swagger_client.AuthApi(swagger_client.ApiClient(configuration))
body = swagger_client.SignInDto() # SignInDto | 

try:
    # アカウントログインを実施
    api_response = api_instance.auth_controller_login(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthApi->auth_controller_login: %s\n" % e)
```

## Documentation for API Endpoints

All URIs are relative to */*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*AuthApi* | [**auth_controller_get_profile**](docs/AuthApi.md#auth_controller_get_profile) | **GET** /api/v1/auth/profile | ログイン済みのアカウント情報取得
*AuthApi* | [**auth_controller_login**](docs/AuthApi.md#auth_controller_login) | **POST** /api/v1/auth/login | アカウントログインを実施
*BadgesApi* | [**badges_controller_add_label**](docs/BadgesApi.md#badges_controller_add_label) | **PUT** /api/v1/badges/{id}/label | Badgeへのラベル追加
*BadgesApi* | [**badges_controller_create**](docs/BadgesApi.md#badges_controller_create) | **POST** /api/v1/badges | 新規バッジ発行
*BadgesApi* | [**badges_controller_download**](docs/BadgesApi.md#badges_controller_download) | **GET** /api/v1/badges/{id}/download | バッジダウンロード
*BadgesApi* | [**badges_controller_file_verify**](docs/BadgesApi.md#badges_controller_file_verify) | **POST** /api/v1/badges/file | バッジファイル検証
*BadgesApi* | [**badges_controller_find_all**](docs/BadgesApi.md#badges_controller_find_all) | **GET** /api/v1/badges | バッジ一覧取得
*BadgesApi* | [**badges_controller_find_one**](docs/BadgesApi.md#badges_controller_find_one) | **GET** /api/v1/badges/{id} | バッジ詳細取得
*BadgesApi* | [**badges_controller_verify**](docs/BadgesApi.md#badges_controller_verify) | **PUT** /api/v1/badges/{id}/verify | バッジ検証
*DidInfosApi* | [**did_infos_controller_add_label**](docs/DidInfosApi.md#did_infos_controller_add_label) | **PUT** /api/v1/did-infos/{id} | DID情報へのラベル追加
*DidInfosApi* | [**did_infos_controller_connect_user**](docs/DidInfosApi.md#did_infos_controller_connect_user) | **PUT** /api/v1/did-infos/{id}/user/{user_id} | DID情報へのクライアントアカウント紐付け
*DidInfosApi* | [**did_infos_controller_create**](docs/DidInfosApi.md#did_infos_controller_create) | **POST** /api/v1/did-infos | 新規DID生成
*DidInfosApi* | [**did_infos_controller_disconnect_user**](docs/DidInfosApi.md#did_infos_controller_disconnect_user) | **DELETE** /api/v1/did-infos/{id}/user | DID情報のクライアントアカウント紐付け解除
*DidInfosApi* | [**did_infos_controller_find_all**](docs/DidInfosApi.md#did_infos_controller_find_all) | **GET** /api/v1/did-infos | DID情報一覧取得
*DidInfosApi* | [**did_infos_controller_find_one**](docs/DidInfosApi.md#did_infos_controller_find_one) | **GET** /api/v1/did-infos/{id} | DID情報詳細取得
*DidInfosApi* | [**did_infos_controller_register**](docs/DidInfosApi.md#did_infos_controller_register) | **POST** /api/v1/did-infos/register | 既存DID登録
*DidInfosApi* | [**did_infos_controller_remove**](docs/DidInfosApi.md#did_infos_controller_remove) | **DELETE** /api/v1/did-infos/{id} | DID情報削除
*DidInfosApi* | [**did_infos_controller_resolve**](docs/DidInfosApi.md#did_infos_controller_resolve) | **POST** /api/v1/did-infos/resolver | DID解決
*FilesApi* | [**files_controller_download**](docs/FilesApi.md#files_controller_download) | **GET** /api/v1/files/{id}/download | ファイルダウンロード
*FilesApi* | [**files_controller_execute_csv**](docs/FilesApi.md#files_controller_execute_csv) | **POST** /api/v1/files/{id} | CSVファイル実行
*FilesApi* | [**files_controller_find_all**](docs/FilesApi.md#files_controller_find_all) | **GET** /api/v1/files | ファイル一覧取得
*FilesApi* | [**files_controller_find_one**](docs/FilesApi.md#files_controller_find_one) | **GET** /api/v1/files/{id} | ファイル詳細取得
*FilesApi* | [**files_controller_remove**](docs/FilesApi.md#files_controller_remove) | **DELETE** /api/v1/files/{id} | ファイル削除
*FilesApi* | [**files_controller_upload_file**](docs/FilesApi.md#files_controller_upload_file) | **POST** /api/v1/files | ファイルアップロード
*GroupsApi* | [**groups_controller_connect_did_infos**](docs/GroupsApi.md#groups_controller_connect_did_infos) | **PUT** /api/v1/groups/{id}/did-infos | グループへのDID情報紐付け
*GroupsApi* | [**groups_controller_connect_users**](docs/GroupsApi.md#groups_controller_connect_users) | **PUT** /api/v1/groups/{id}/users | グループへのユーザーアカウント紐付け
*GroupsApi* | [**groups_controller_connect_vc_infos**](docs/GroupsApi.md#groups_controller_connect_vc_infos) | **PUT** /api/v1/groups/{id}/vc-infos | グループへのVC情報紐付け
*GroupsApi* | [**groups_controller_connect_vc_schema**](docs/GroupsApi.md#groups_controller_connect_vc_schema) | **PUT** /api/v1/groups/{id}/vc-schemas | グループへのVCスキーマ紐付け
*GroupsApi* | [**groups_controller_connect_vp_infos**](docs/GroupsApi.md#groups_controller_connect_vp_infos) | **PUT** /api/v1/groups/{id}/vp-infos | グループへのVP情報紐付け
*GroupsApi* | [**groups_controller_create**](docs/GroupsApi.md#groups_controller_create) | **POST** /api/v1/groups | グループ作成
*GroupsApi* | [**groups_controller_disconnect_did_info**](docs/GroupsApi.md#groups_controller_disconnect_did_info) | **DELETE** /api/v1/groups/{id}/did-info/{did_info_id} | グループのDID情報紐付け解除
*GroupsApi* | [**groups_controller_disconnect_user**](docs/GroupsApi.md#groups_controller_disconnect_user) | **DELETE** /api/v1/groups/{id}/user/{user_id} | グループのユーザーアカウント紐付け解除
*GroupsApi* | [**groups_controller_disconnect_vc_info**](docs/GroupsApi.md#groups_controller_disconnect_vc_info) | **DELETE** /api/v1/groups/{id}/vc-info/{vc_info_id} | グループのVC情報紐付け解除
*GroupsApi* | [**groups_controller_disconnect_vc_schema**](docs/GroupsApi.md#groups_controller_disconnect_vc_schema) | **DELETE** /api/v1/groups/{id}/vc-schema/{vc_schema_id} | グループのVCスキーマ紐付け解除
*GroupsApi* | [**groups_controller_disconnect_vp_info**](docs/GroupsApi.md#groups_controller_disconnect_vp_info) | **DELETE** /api/v1/groups/{id}/vp-info/{vp_info_id} | グループのVP情報紐付け解除
*GroupsApi* | [**groups_controller_find_all**](docs/GroupsApi.md#groups_controller_find_all) | **GET** /api/v1/groups | グループ一覧取得
*GroupsApi* | [**groups_controller_find_one**](docs/GroupsApi.md#groups_controller_find_one) | **GET** /api/v1/groups/{id} | グループ詳細取得
*GroupsApi* | [**groups_controller_remove**](docs/GroupsApi.md#groups_controller_remove) | **DELETE** /api/v1/groups/{id} | グループ停止
*GroupsApi* | [**groups_controller_update**](docs/GroupsApi.md#groups_controller_update) | **PUT** /api/v1/groups/{id} | グループ更新
*HealthApi* | [**app_controller_health**](docs/HealthApi.md#app_controller_health) | **GET** /api/v1/health | ヘルスチェック
*MailsApi* | [**mails_controller_find_all**](docs/MailsApi.md#mails_controller_find_all) | **GET** /api/v1/mails | 送信済みメール一覧取得
*MailsApi* | [**mails_controller_find_one**](docs/MailsApi.md#mails_controller_find_one) | **GET** /api/v1/mails/{id} | 送信済みメール詳細取得
*MailsApi* | [**mails_controller_send**](docs/MailsApi.md#mails_controller_send) | **POST** /api/v1/mails | 新規単一メール送信
*MailsApi* | [**mails_controller_send_batch**](docs/MailsApi.md#mails_controller_send_batch) | **POST** /api/v1/mails/batch | 新規複数メールバッチ送信
*SettingsApi* | [**settings_controller_find_all**](docs/SettingsApi.md#settings_controller_find_all) | **GET** /api/v1/settings | Get all admins
*SettingsApi* | [**settings_controller_find_one**](docs/SettingsApi.md#settings_controller_find_one) | **GET** /api/v1/settings/{key} | Get a specific admin
*UsersApi* | [**users_controller_create**](docs/UsersApi.md#users_controller_create) | **POST** /api/v1/users | ユーザーアカウント作成
*UsersApi* | [**users_controller_export_key**](docs/UsersApi.md#users_controller_export_key) | **POST** /api/v1/users/{id}/keys/{keyId}/mail | アカウントへの鍵のメール送信
*UsersApi* | [**users_controller_find_all**](docs/UsersApi.md#users_controller_find_all) | **GET** /api/v1/users | ユーザーアカウント一覧取得
*UsersApi* | [**users_controller_find_one**](docs/UsersApi.md#users_controller_find_one) | **GET** /api/v1/users/{id} | ユーザーアカウント詳細取得
*UsersApi* | [**users_controller_invite**](docs/UsersApi.md#users_controller_invite) | **POST** /api/v1/users/{id}/invite | ユーザーアカウントへのアカウント有効化メール送信
*UsersApi* | [**users_controller_register_user_did**](docs/UsersApi.md#users_controller_register_user_did) | **POST** /api/v1/users/{id}/dids | Get the count of clients
*UsersApi* | [**users_controller_registration**](docs/UsersApi.md#users_controller_registration) | **POST** /api/v1/users/registration | ユーザーアカウントへのアカウント有効化、登録フロー
*UsersApi* | [**users_controller_remove**](docs/UsersApi.md#users_controller_remove) | **DELETE** /api/v1/users/{id} | ユーザーアカウント停止
*UsersApi* | [**users_controller_send_did**](docs/UsersApi.md#users_controller_send_did) | **POST** /api/v1/users/{id}/dids/{didInfoId}/mail | アカウントへのDIDのメール送信
*UsersApi* | [**users_controller_send_key**](docs/UsersApi.md#users_controller_send_key) | **POST** /api/v1/users/{id}/keys/{didInfoId}/mail | アカウントへのDIDのメール送信
*UsersApi* | [**users_controller_send_vc**](docs/UsersApi.md#users_controller_send_vc) | **POST** /api/v1/users/{id}/vcs/{vcInfoId}/mail | アカウントへのVCのメール送信
*UsersApi* | [**users_controller_update**](docs/UsersApi.md#users_controller_update) | **PUT** /api/v1/users/{id} | ユーザーアカウント更新
*VcInfosApi* | [**vc_infos_controller_add_label**](docs/VcInfosApi.md#vc_infos_controller_add_label) | **PUT** /api/v1/vc-infos/{id}/label | VC情報へのラベル追加
*VcInfosApi* | [**vc_infos_controller_connect_user**](docs/VcInfosApi.md#vc_infos_controller_connect_user) | **PUT** /api/v1/vc-infos/{id} | VC情報へのクライアントアカウント紐付け
*VcInfosApi* | [**vc_infos_controller_create**](docs/VcInfosApi.md#vc_infos_controller_create) | **POST** /api/v1/vc-infos | 新規VC発行
*VcInfosApi* | [**vc_infos_controller_disconnect_user**](docs/VcInfosApi.md#vc_infos_controller_disconnect_user) | **DELETE** /api/v1/vc-infos/{id}/user | VC情報のクライアントアカウント紐付け解除
*VcInfosApi* | [**vc_infos_controller_find_all**](docs/VcInfosApi.md#vc_infos_controller_find_all) | **GET** /api/v1/vc-infos | VC情報一覧取得
*VcInfosApi* | [**vc_infos_controller_find_one**](docs/VcInfosApi.md#vc_infos_controller_find_one) | **GET** /api/v1/vc-infos/{id} | VC情報詳細取得
*VcInfosApi* | [**vc_infos_controller_generate_vp**](docs/VcInfosApi.md#vc_infos_controller_generate_vp) | **POST** /api/v1/vc-infos/{id} | 新規VP情報生成
*VcInfosApi* | [**vc_infos_controller_issue**](docs/VcInfosApi.md#vc_infos_controller_issue) | **POST** /api/v1/vc-infos/issue | 新規VC発行(スキーマなし)
*VcInfosApi* | [**vc_infos_controller_upload**](docs/VcInfosApi.md#vc_infos_controller_upload) | **POST** /api/v1/vc-infos/upload | 新規VCアップロード
*VcSchemasApi* | [**vc_schemas_controller_create**](docs/VcSchemasApi.md#vc_schemas_controller_create) | **POST** /api/v1/vc-schemas | 新規VCスキーマ作成
*VcSchemasApi* | [**vc_schemas_controller_find_all**](docs/VcSchemasApi.md#vc_schemas_controller_find_all) | **GET** /api/v1/vc-schemas | VCスキーマ一覧取得
*VcSchemasApi* | [**vc_schemas_controller_find_one**](docs/VcSchemasApi.md#vc_schemas_controller_find_one) | **GET** /api/v1/vc-schemas/{id} | VCスキーマ情報詳細取得
*VcSchemasApi* | [**vc_schemas_controller_update**](docs/VcSchemasApi.md#vc_schemas_controller_update) | **PUT** /api/v1/vc-schemas/{id} | VCスキーマへのグループ紐付け
*VerificationsApi* | [**verifications_controller_create**](docs/VerificationsApi.md#verifications_controller_create) | **POST** /api/v1/verifications | VC/VP検証
*VerificationsApi* | [**verifications_controller_find_all**](docs/VerificationsApi.md#verifications_controller_find_all) | **GET** /api/v1/verifications | VC/VP検証結果一覧取得
*VerificationsApi* | [**verifications_controller_find_one**](docs/VerificationsApi.md#verifications_controller_find_one) | **GET** /api/v1/verifications/{id} | VC/VP検証結果詳細取得
*VpInfosApi* | [**vp_infos_controller_add_label**](docs/VpInfosApi.md#vp_infos_controller_add_label) | **PUT** /api/v1/vp-infos/{id}/label | VP情報へのラベル追加
*VpInfosApi* | [**vp_infos_controller_connect_user**](docs/VpInfosApi.md#vp_infos_controller_connect_user) | **PUT** /api/v1/vp-infos/{id} | VP情報へのクライアントアカウント紐付け
*VpInfosApi* | [**vp_infos_controller_create**](docs/VpInfosApi.md#vp_infos_controller_create) | **POST** /api/v1/vp-infos | 新規VP生成
*VpInfosApi* | [**vp_infos_controller_disconnect_user**](docs/VpInfosApi.md#vp_infos_controller_disconnect_user) | **DELETE** /api/v1/vp-infos/{id}/user | VP情報のクライアントアカウント紐付け解除
*VpInfosApi* | [**vp_infos_controller_find_all**](docs/VpInfosApi.md#vp_infos_controller_find_all) | **GET** /api/v1/vp-infos | VP情報一覧取得
*VpInfosApi* | [**vp_infos_controller_find_one**](docs/VpInfosApi.md#vp_infos_controller_find_one) | **GET** /api/v1/vp-infos/{id} | VP情報詳細取得
*VpInfosApi* | [**vp_infos_controller_upload**](docs/VpInfosApi.md#vp_infos_controller_upload) | **POST** /api/v1/vp-infos/upload | 新規VPアップロード

## Documentation For Models

 - [AddLabelToBadgeDto](docs/AddLabelToBadgeDto.md)
 - [AddLabelToDidInfoDto](docs/AddLabelToDidInfoDto.md)
 - [AddLabelToVcInfoDto](docs/AddLabelToVcInfoDto.md)
 - [AddLabelToVpInfoDto](docs/AddLabelToVpInfoDto.md)
 - [AllOfBadgeResponseDtoVcInfo](docs/AllOfBadgeResponseDtoVcInfo.md)
 - [AllOfBadgeResponseDtoVcSchema](docs/AllOfBadgeResponseDtoVcSchema.md)
 - [AllOfBadgeVcInfo](docs/AllOfBadgeVcInfo.md)
 - [AllOfBadgeVcSchema](docs/AllOfBadgeVcSchema.md)
 - [AllOfDidInfoCreatedBy](docs/AllOfDidInfoCreatedBy.md)
 - [AllOfDidInfoResponseDtoDidInfo](docs/AllOfDidInfoResponseDtoDidInfo.md)
 - [AllOfDidInfoUser](docs/AllOfDidInfoUser.md)
 - [AllOfDidInfoVpInfos](docs/AllOfDidInfoVpInfos.md)
 - [AllOfFileCreatedBy](docs/AllOfFileCreatedBy.md)
 - [AllOfFileResponseDtoCreatedBy](docs/AllOfFileResponseDtoCreatedBy.md)
 - [AllOfFileVcSchema](docs/AllOfFileVcSchema.md)
 - [AllOfGroupCreatedBy](docs/AllOfGroupCreatedBy.md)
 - [AllOfGroupResponseDtoCreatedBy](docs/AllOfGroupResponseDtoCreatedBy.md)
 - [AllOfUserCreatedBy](docs/AllOfUserCreatedBy.md)
 - [AllOfUserResponseDtoCreatedBy](docs/AllOfUserResponseDtoCreatedBy.md)
 - [AllOfVcContextVcSchema](docs/AllOfVcContextVcSchema.md)
 - [AllOfVcInfoBadge](docs/AllOfVcInfoBadge.md)
 - [AllOfVcInfoCreatedBy](docs/AllOfVcInfoCreatedBy.md)
 - [AllOfVcInfoResponseDtoVcInfo](docs/AllOfVcInfoResponseDtoVcInfo.md)
 - [AllOfVcInfoUser](docs/AllOfVcInfoUser.md)
 - [AllOfVcInfoVcSchema](docs/AllOfVcInfoVcSchema.md)
 - [AllOfVcSchemaCreatedBy](docs/AllOfVcSchemaCreatedBy.md)
 - [AllOfVcSchemaFile](docs/AllOfVcSchemaFile.md)
 - [AllOfVcSchemaPropertyVcSchema](docs/AllOfVcSchemaPropertyVcSchema.md)
 - [AllOfVcSchemaResponseDtoCreatedBy](docs/AllOfVcSchemaResponseDtoCreatedBy.md)
 - [AllOfVcSchemaResponseDtoFile](docs/AllOfVcSchemaResponseDtoFile.md)
 - [AllOfVerificationCreatedBy](docs/AllOfVerificationCreatedBy.md)
 - [AllOfVerificationResponseDtoCreatedBy](docs/AllOfVerificationResponseDtoCreatedBy.md)
 - [AllOfVerificationResponseDtoVcInfo](docs/AllOfVerificationResponseDtoVcInfo.md)
 - [AllOfVerificationResponseDtoVpInfo](docs/AllOfVerificationResponseDtoVpInfo.md)
 - [AllOfVerificationVcInfo](docs/AllOfVerificationVcInfo.md)
 - [AllOfVerificationVpInfo](docs/AllOfVerificationVpInfo.md)
 - [AllOfVerificationsResponseDtoLinks](docs/AllOfVerificationsResponseDtoLinks.md)
 - [AllOfVerificationsResponseDtoMeta](docs/AllOfVerificationsResponseDtoMeta.md)
 - [AllOfVpInfoCreatedBy](docs/AllOfVpInfoCreatedBy.md)
 - [AllOfVpInfoDetailDtoVpInfo](docs/AllOfVpInfoDetailDtoVpInfo.md)
 - [AllOfVpInfoDidInfo](docs/AllOfVpInfoDidInfo.md)
 - [AllOfVpInfoUser](docs/AllOfVpInfoUser.md)
 - [Badge](docs/Badge.md)
 - [BadgeResponseDto](docs/BadgeResponseDto.md)
 - [BadgesFileBody](docs/BadgesFileBody.md)
 - [BadgesResponseDto](docs/BadgesResponseDto.md)
 - [ConnectDidInfosDto](docs/ConnectDidInfosDto.md)
 - [ConnectUsersDto](docs/ConnectUsersDto.md)
 - [ConnectVcInfosDto](docs/ConnectVcInfosDto.md)
 - [ConnectVcSchemasDto](docs/ConnectVcSchemasDto.md)
 - [ConnectVpInfosDto](docs/ConnectVpInfosDto.md)
 - [CreateBadgeDto](docs/CreateBadgeDto.md)
 - [CreateDidDto](docs/CreateDidDto.md)
 - [CreateGroupDto](docs/CreateGroupDto.md)
 - [CreateUserDto](docs/CreateUserDto.md)
 - [CreateVcInfoDto](docs/CreateVcInfoDto.md)
 - [CreateVcSchemaDto](docs/CreateVcSchemaDto.md)
 - [CreateVpInfoDto](docs/CreateVpInfoDto.md)
 - [DidInfo](docs/DidInfo.md)
 - [DidInfoResponseDto](docs/DidInfoResponseDto.md)
 - [DidInfosResponseDto](docs/DidInfosResponseDto.md)
 - [File](docs/File.md)
 - [FileResponseDto](docs/FileResponseDto.md)
 - [FilesResponseDto](docs/FilesResponseDto.md)
 - [GenerateDidDto](docs/GenerateDidDto.md)
 - [GenerateVpDto](docs/GenerateVpDto.md)
 - [GetProfileResponseDto](docs/GetProfileResponseDto.md)
 - [Group](docs/Group.md)
 - [GroupResponseDto](docs/GroupResponseDto.md)
 - [GroupsResponseDto](docs/GroupsResponseDto.md)
 - [IssueVcInfoDto](docs/IssueVcInfoDto.md)
 - [LinkDto](docs/LinkDto.md)
 - [Mail](docs/Mail.md)
 - [MailsResponseDto](docs/MailsResponseDto.md)
 - [MetaDto](docs/MetaDto.md)
 - [RegisterDidDto](docs/RegisterDidDto.md)
 - [RegistrationProcessDto](docs/RegistrationProcessDto.md)
 - [ResolveDidDto](docs/ResolveDidDto.md)
 - [ResolveDidResponseDto](docs/ResolveDidResponseDto.md)
 - [SendMailBatchDto](docs/SendMailBatchDto.md)
 - [SendMailDto](docs/SendMailDto.md)
 - [Setting](docs/Setting.md)
 - [SettingListResponseDto](docs/SettingListResponseDto.md)
 - [SettingResponseDto](docs/SettingResponseDto.md)
 - [SignInDto](docs/SignInDto.md)
 - [SignInResponseDto](docs/SignInResponseDto.md)
 - [UpdateVcInfoDto](docs/UpdateVcInfoDto.md)
 - [UpdateVcSchemaDto](docs/UpdateVcSchemaDto.md)
 - [UploadVCDto](docs/UploadVCDto.md)
 - [UploadVPDto](docs/UploadVPDto.md)
 - [User](docs/User.md)
 - [UserResponseDto](docs/UserResponseDto.md)
 - [UserToken](docs/UserToken.md)
 - [UsersResponseDto](docs/UsersResponseDto.md)
 - [V1FilesBody](docs/V1FilesBody.md)
 - [VcContext](docs/VcContext.md)
 - [VcInfo](docs/VcInfo.md)
 - [VcInfoResponseDto](docs/VcInfoResponseDto.md)
 - [VcInfosResponseDto](docs/VcInfosResponseDto.md)
 - [VcSchema](docs/VcSchema.md)
 - [VcSchemaProperty](docs/VcSchemaProperty.md)
 - [VcSchemaResponseDto](docs/VcSchemaResponseDto.md)
 - [VcSchemasResponseDto](docs/VcSchemasResponseDto.md)
 - [Verification](docs/Verification.md)
 - [VerificationDto](docs/VerificationDto.md)
 - [VerificationResponseDto](docs/VerificationResponseDto.md)
 - [VerificationsResponseDto](docs/VerificationsResponseDto.md)
 - [VerifiyBadgeFileReponseDto](docs/VerifiyBadgeFileReponseDto.md)
 - [VerifiyBadgeReponseDto](docs/VerifiyBadgeReponseDto.md)
 - [VerifyBadgeDto](docs/VerifyBadgeDto.md)
 - [VpInfo](docs/VpInfo.md)
 - [VpInfoDetailDto](docs/VpInfoDetailDto.md)
 - [VpInfoResponseDto](docs/VpInfoResponseDto.md)

## Documentation For Authorization


## bearer



## Author


