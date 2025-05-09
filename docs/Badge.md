# Badge

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | (必須) バッジの識別子 | 
**label** | **str** | (任意) バッジのラベル名 | [optional] 
**filename** | **str** | (任意) バッジのファイル名 | [optional] 
**description** | **str** | (任意) バッジの作成目的や用途など任意で設定可能な説明文 | 
**status** | **float** | (必須) バッジの状態(1: アクティブ, 0: 停止中) | 
**vc_schema** | **AllOfBadgeVcSchema** | (任意) バッジに紐付いたVCスキーマ | [optional] 
**vc_info** | **AllOfBadgeVcInfo** | (任意) バッジに紐付き、メタデータとなるVC情報 | [optional] 
**created_at** | **str** | (必須) グループの作成日時 | 
**updated_at** | **str** | (必須) グループの最終更新日時 | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

