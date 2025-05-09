# VcInfo

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | (必須) VC情報の識別子 | 
**label** | **str** | (任意) VCの識別や整理などの管理するにあったてメタデータとして任意で設定可能な単語のフレーズ。(例: vc-for-project1) | 
**hash** | **str** | (必須) VCのハッシュ値。VCの保管における識別子として用いる。 | 
**description** | **str** | (任意) VCの発行目的や用途など任意で設定可能な説明文。 | 
**created_by** | **AllOfVcInfoCreatedBy** | (任意) VC情報を生成したユーザーアカウント | 
**vc_schema** | **AllOfVcInfoVcSchema** | (任意) 発行したVCの元となるVCスキーマ | [optional] 
**user** | **AllOfVcInfoUser** | (任意) VC情報と紐付いたアカウント | [optional] 
**vp_infos** | [**list[VpInfo]**](VpInfo.md) | (任意) このVCを元に生成したVP情報の配列 | [optional] 
**groups** | [**list[Group]**](Group.md) | (任意) VC情報に紐づいたグループの配列 | [optional] 
**badge** | **AllOfVcInfoBadge** | (任意) VC情報と紐付いたバッジ | [optional] 
**verifications** | [**list[Verification]**](Verification.md) | (任意) このVCの検証結果の配列。 | [optional] 
**created_at** | **str** | (必須) VC情報の作成日時 | 
**updated_at** | **str** | (必須) VC情報の更新日時 | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

