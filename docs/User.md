# User

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | アカウントの識別子 | 
**name** | **str** | アカウントの名前 | 
**email** | **str** | アカウントのメールアドレス | 
**password** | **str** | アカウントのパスワード(8文字以上20字未満) | 
**need_activate_flow** | **bool** | (必須: {default: false}) アカウントの有効化フローが必要か否か(true: 必要 /false: 不要) | 
**status** | **str** | ユーザーのアカウントステータス | 
**role** | **str** | アカウントのロール(admin/user/clinet) | 
**created_by** | **AllOfUserCreatedBy** | (任意) このアカウントを作成したユーザー | [optional] 
**did_infos** | [**list[DidInfo]**](DidInfo.md) | (任意) アカウントに紐付けされたDID情報の配列 | [optional] 
**vc_infos** | [**list[VcInfo]**](VcInfo.md) | (任意) アカウントに紐付けされたVC情報の配列 | [optional] 
**vp_infos** | [**list[VpInfo]**](VpInfo.md) | (任意) アカウントに紐付けされたVP情報の配列 | [optional] 
**groups** | [**list[Group]**](Group.md) | (任意) アカウントに紐付けされたグループの配列 | [optional] 
**user_tokens** | [**list[UserToken]**](UserToken.md) | (任意) ユーザーアカウントがアップロードしたファイルの配列。 | 
**created_users** | [**list[User]**](User.md) | (任意) このユーザーによって作成されたアカウントの配列 | [optional] 
**created_vc_infos** | [**list[VcInfo]**](VcInfo.md) | (任意) アカウントに紐付けされたVC情報の配列 | [optional] 
**created_vp_infos** | [**list[VpInfo]**](VpInfo.md) | (任意) アカウントに紐付けされたVP情報の配列 | [optional] 
**created_groups** | [**list[Group]**](Group.md) | (任意) アカウントに作成したグループの配列 | [optional] 
**created_did_infos** | [**list[DidInfo]**](DidInfo.md) | (任意) アカウントが作成したDID情報の配列 | [optional] 
**created_vc_schemas** | [**list[VcSchema]**](VcSchema.md) | (任意) ユーザーアカウントが作成したVCスキーマの配列。 | 
**created_verifications** | [**list[Verification]**](Verification.md) | (任意) ユーザーアカウントが実行した検証結果の配列。 | 
**created_mails** | [**list[Mail]**](Mail.md) | (任意) Admin権限アカウントが送信したメールの配列(Adminロール以外の場合、関係のないカラム) | [optional] 
**created_files** | [**list[File]**](File.md) | (任意) ユーザーアカウントがアップロードしたファイルの配列。 | 
**created_at** | **str** | ユーザーアカウントの作成日時 | 
**updated_at** | **str** | ユーザーアカウントの更新日時 | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

