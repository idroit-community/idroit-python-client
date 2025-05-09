# UserResponseDto

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | ユーザーアカウントの識別子 | 
**name** | **str** | ユーザーアカウントの名前 | 
**email** | **str** | ユーザーアカウントのメールアドレス | 
**need_activate_flow** | **bool** | ユーザーアクティベーション(true: アクティブ /false: 停止中) | 
**status** | **str** | ユーザーのアカウントステータス(\&quot;inactive\&quot;: アクティブ未完了, \&quot;acrivating\&quot;: アクティブ作業途中, \&quot;active\&quot;: アクティブ中, \&quot;deactive\&quot;: 論理削除済) | 
**role** | **str** | ユーザーのアカウントロール(\&quot;admin\&quot;, \&quot;user\&quot;, \&quot;client\&quot;) | 
**user_tokens** | [**list[UserToken]**](UserToken.md) | (任意) ユーザーアカウントがアップロードしたファイルの配列。 | 
**created_by** | **AllOfUserResponseDtoCreatedBy** | ユーザーアカウントを作成したユーザーアカウント | 
**did_infos** | [**list[DidInfo]**](DidInfo.md) | ユーザーアカウントに紐付けられたDID情報の配列 | [optional] 
**vc_infos** | [**list[VcInfo]**](VcInfo.md) | ユーザーアカウントに紐付けられたVC情報の配列 | [optional] 
**vp_infos** | [**list[VpInfo]**](VpInfo.md) | ユーザーアカウントに紐付けられたVP情報の配列 | [optional] 
**groups** | [**list[Group]**](Group.md) | ユーザーアカウントが作成したグループの配列 | [optional] 
**created_users** | [**list[User]**](User.md) | ユーザーアカウントに紐付けされたVP情報の配列 | [optional] 
**created_vc_infos** | [**list[VcInfo]**](VcInfo.md) | ユーザーが作成したVC情報の配列 | [optional] 
**created_vp_infos** | [**list[VpInfo]**](VpInfo.md) | ユーザーが作成したVP情報の配列 | [optional] 
**created_groups** | [**list[Group]**](Group.md) | ユーザーアカウントが作成したグループの配列 | [optional] 
**created_did_infos** | [**list[DidInfo]**](DidInfo.md) | ユーザーが作成したDID情報の配列 | [optional] 
**created_vc_schemas** | [**list[VcSchema]**](VcSchema.md) | ユーザーが作成したVCスキーマの配列 | [optional] 
**created_verifications** | [**list[Verification]**](Verification.md) | ユーザーアカウントが実行した検証結果の配列 | [optional] 
**created_mails** | [**list[Mail]**](Mail.md) | Admin権限アカウントが送信したメールの配列 | [optional] 
**created_files** | [**list[File]**](File.md) | ユーザーアカウントに紐付けされたファイルの配列 | [optional] 
**created_at** | **str** | ユーザーアカウントの作成日時 | 
**updated_at** | **str** | ユーザーアカウントの更新日時 | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

