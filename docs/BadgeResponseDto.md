# BadgeResponseDto

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | バッジの識別子 | 
**label** | **str** | バッジのラベル名 | 
**filename** | **str** | バッジのファイル名 | 
**description** | **str** | バッジの作成目的や用途など任意で設定可能な説明文 | 
**status** | **float** | バッジの状態(1: 利用可, 0: 利用停止中) | 
**vc_schema** | **AllOfBadgeResponseDtoVcSchema** | バッジに紐付いたVCスキーマの配列 | 
**vc_info** | **AllOfBadgeResponseDtoVcInfo** | バッジに紐付いたVC情報の配列 | 
**created_at** | **str** | バッジの作成日時 | 
**updated_at** | **str** | バッジの最終更新日時 | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

