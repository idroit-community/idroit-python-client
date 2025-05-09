# File

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | (必須) ファイルの識別子 | 
**filename** | **str** | (任意) システム内で管理される際にシステムによって名付けられるユニークなファイル名 | 
**originalname** | **str** | (必須) システムへアップロード時の元のファイル名 | 
**type** | **str** | (必須) ファイル形式 | 
**file_data** | **str** | (必須) ファイルのバイナリデータ | 
**executed** | **bool** | (任意) ファイルがCSVの場合、アカウントデータ生成実行に使用されたか。(true: 実行済み, false: 未使用) | 
**status** | **float** | (必須) ファイルのステータス | 
**group** | [**list[Group]**](Group.md) | (任意) ファイルを紐づけたグループの配列 | 
**vc_schema** | **AllOfFileVcSchema** | (任意) ファイルに紐づいたVCスキーマ | [optional] 
**created_by** | **AllOfFileCreatedBy** | (必須) ファイルをアップロードしたユーザーアカウント。 | 
**created_at** | **str** | (必須) ファイルの作成日時 | 
**updated_at** | **str** | (必須) グループの最終更新日時 | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

