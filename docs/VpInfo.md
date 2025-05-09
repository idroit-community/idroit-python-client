# VpInfo

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | (必須) VP情報の識別子 | 
**label** | **str** | (任意) VPの識別や整理などの管理するにあったてメタデータとして任意で設定可能な単語のフレーズ | [optional] 
**hash** | **str** | (必須) VPのハッシュ値。VPの保管における識別子として用いる。 | [optional] 
**description** | **str** | (任意) VCの発行目的や用途など任意で設定可能な説明文。 | [optional] 
**raw** | **str** | (必須) VPのバイナリデータ | 
**created_by** | **AllOfVpInfoCreatedBy** | (任意) VP情報を生成したユーザーアカウント | 
**user** | **AllOfVpInfoUser** | (任意) VP情報と紐付いたアカウント | [optional] 
**vc_infos** | [**list[VcInfo]**](VcInfo.md) | (任意) VPを生成する元となるVC情報 | [optional] 
**groups** | [**list[Group]**](Group.md) | (任意) VP情報に紐づいたグループの配列 | [optional] 
**did_info** | **AllOfVpInfoDidInfo** | (任意) VP生成時の署名に用いるDID情報の識別子 | [optional] 
**verifications** | [**list[Verification]**](Verification.md) | (任意) VPの検証結果 | [optional] 
**created_at** | **str** | (必須) VP情報の作成日時 | 
**updated_at** | **str** | (必須) VP情報の更新日時 | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

