# VcSchema

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | (必須) VCスキーマの識別子 | 
**title** | **str** | (必須) VCスキーマのタイトル | 
**version** | **str** | (必須) VCスキーマのバージョン | 
**description** | **str** | (任意) VCスキーマの説明文 | 
**is_badge_schema** | **str** | (必須) VCスキーマがバッジのスキーマか否か | [optional] [default to 'false']
**vc_infos** | [**list[VcInfo]**](VcInfo.md) | (任意) このVCスキーマを用いて生成したVC情報の配列。 | [optional] 
**vc_contexts** | [**list[VcContext]**](VcContext.md) | (任意) VCスキーマに設定したcontext項目の配列 | [optional] 
**vc_schema_properties** | [**list[VcSchemaProperty]**](VcSchemaProperty.md) | (必須) VCスキーマの項目情報の配列 | [optional] 
**groups** | [**list[Group]**](Group.md) | (任意) VCスキーマを紐付けたグループの配列 | [optional] 
**badges** | [**list[Badge]**](Badge.md) | (任意) VCスキーマを紐付けたバッジ | [optional] 
**file** | **AllOfVcSchemaFile** | (任意) VCスキーマに紐付けるバッジ用の画像。&#x60;isBadgeSchema&#x60;プロパティが&#x60;true&#x60;の場合必須。 | [optional] 
**created_by** | **AllOfVcSchemaCreatedBy** | (必須) VCスキーマを作成したユーザーアカウント。 | 
**created_at** | **str** | (必須) VCスキーマの作成日時 | 
**updated_at** | **str** | (必須) VCスキーマの更新日時 | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

