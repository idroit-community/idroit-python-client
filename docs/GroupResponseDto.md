# GroupResponseDto

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | グループの識別子 | 
**name** | **str** |  グループの名前 | 
**status** | **str** | グループの状態(1: アクティブ, 0: 停止中) | 
**description** | **str** | グループの作成目的や用途など任意で設定可能な説明文 | 
**users** | [**list[User]**](User.md) | グループに紐付いたユーザーアカウントの配列 | 
**created_by** | **AllOfGroupResponseDtoCreatedBy** | グループを作成したユーザーアカウント | 
**did_infos** | [**list[DidInfo]**](DidInfo.md) | グループに紐付いたVC情報の配列 | 
**vc_infos** | [**list[VcInfo]**](VcInfo.md) | グループに紐付いたVC情報の配列 | 
**vp_infos** | [**list[VpInfo]**](VpInfo.md) | グループに紐付いたVP情報の配列 | 
**vc_schemas** | [**list[VcSchema]**](VcSchema.md) | グループに紐付いたVCスキーマの配列 | 
**created_at** | **str** | グループの作成日時 | 
**updated_at** | **str** | グループの最終更新日時 | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

