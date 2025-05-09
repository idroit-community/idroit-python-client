# Group

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | (必須) グループの識別子 | 
**name** | **str** | (必須) グループの名前。(例: プロジェクト名や企業名など) | 
**status** | **str** | (必須) グループの状態(1: アクティブ, 0: 停止中) | 
**description** | **str** | (任意) グループの作成目的や用途など任意で設定可能な説明文 | 
**users** | [**list[User]**](User.md) | (任意) グループに紐付いたアカウントの配列 | [optional] 
**created_by** | **AllOfGroupCreatedBy** | (必須) グループを作成したユーザーアカウント。 | 
**did_infos** | [**list[DidInfo]**](DidInfo.md) | (任意) グループに紐付いたDID情報の配列 | [optional] 
**vc_infos** | [**list[VcInfo]**](VcInfo.md) | (任意) グループに紐付いたVC情報の配列 | [optional] 
**vp_infos** | [**list[VpInfo]**](VpInfo.md) | (任意) グループに紐付いたVP情報の配列 | [optional] 
**vc_schemas** | [**list[VcSchema]**](VcSchema.md) | (任意) グループに紐付いたVCスキーマの配列 | [optional] 
**created_at** | **str** | (必須) グループの作成日時 | 
**updated_at** | **str** | (必須) グループの最終更新日時 | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

