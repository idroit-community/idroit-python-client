# DidInfo

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | (必須) DID情報の識別子 | 
**manage_uuid** | **str** | (必須) DID情報の管理に用いるユニークな識別子 | 
**did** | **str** | (必須) DID | 
**method** | **str** | (必須) DIDメソッド | 
**label** | **str** | (任意) DIDの識別や整理などの管理するにあったてメタデータとして任意で設定可能な単語のフレーズ。(例: did-for-project1) | 
**domain_name** | **str** | (任意) did:webメソッドでDIDを生成する際に必要なドメイン名。DIDによって指定されたドメインがドメインネームシステム(DNS)を通じて解決されるときのホスト名。did:webメソッド以外では必要のないカラムである。 | 
**exist_private_key** | **bool** | (必須) DID情報に紐付いた秘密鍵を本アプリケーションで保管しているか否か | 
**description** | **str** | (任意) DID情報の生成目的や用途など任意で設定可能な説明文 | 
**user** | **AllOfDidInfoUser** | (任意) DID情報に紐付いたアカウントの配列 | [optional] 
**created_by** | **AllOfDidInfoCreatedBy** | (任意) DIDを生成したユーザーアカウント | 
**vp_infos** | **AllOfDidInfoVpInfos** | (任意) 生成時に署名にDIDを用いたVP情報 | [optional] 
**groups** | [**list[Group]**](Group.md) | (任意) DID情報に紐づいたグループの配列 | [optional] 
**created_at** | **str** | (必須) DID情報の作成日時 | 
**updated_at** | **str** | (必須) DID情報の最終更新 | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

