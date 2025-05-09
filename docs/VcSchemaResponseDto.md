# VcSchemaResponseDto

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | VCスキーマの識別子 | 
**title** | **str** | VCスキーマのタイトル | 
**version** | **str** | VCスキーマのバージョン | 
**description** | **str** | VCスキーマの説明文 | 
**is_badge_schema** | **str** | VCスキーマがバッジのスキーマか否か | 
**vc_infos** | [**list[VcInfo]**](VcInfo.md) |  | 
**vc_contexts** | [**list[VcContext]**](VcContext.md) | VCのスキーマのJSONスキーマコンテキスト | 
**vc_schema_properties** | [**list[VcSchemaProperty]**](VcSchemaProperty.md) | VCのスキーマの各項目における項目名と項目型のオブジェクトの配列 | 
**groups** | [**list[Group]**](Group.md) |  | 
**badges** | [**list[Badge]**](Badge.md) | VCスキーマを紐付けたバッジ | 
**file** | **AllOfVcSchemaResponseDtoFile** | VCスキーマに紐付けるバッジ用の画像。&#x60;isBadgeSchema&#x60;プロパティが&#x60;true&#x60;の場合必須。 | 
**created_by** | **AllOfVcSchemaResponseDtoCreatedBy** | VCスキーマを作成したユーザーアカウント | 
**created_at** | **str** | VCスキーマの作成日時 | 
**updated_at** | **str** | VCスキーマの最終更新日時 | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

