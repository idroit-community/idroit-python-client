# Verification

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | (必須) 検証結果の識別子 | 
**label** | **str** | (必須) 検証結果の識別や整理などの管理するにあったてメタデータとして任意で設定可能な単語のフレーズ。(例: verify-for-check) | 
**result** | **bool** | (必須) VC/VPの検証結果(true: 検証に成功, false: 検証に失敗) | 
**created_by** | **AllOfVerificationCreatedBy** | (任意) 検証結果を作成したユーザーアカウント | 
**vc_info** | **AllOfVerificationVcInfo** | (任意) 検証を実行したVC情報の識別子 | [optional] 
**vp_info** | **AllOfVerificationVpInfo** | (任意) 検証を実行したVP情報の識別子 | [optional] 
**created_at** | **str** | (必須) 検証実行時の日時 | 
**updated_at** | **str** | (必須) 検証結果の最終更新日 | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

