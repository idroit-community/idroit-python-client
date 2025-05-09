# CreateUserDto

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | (必須) ユーザーアカウントの名前 | 
**email** | **str** | (必須) ユーザーアカウントのメールアドレス | 
**password** | **str** | (任意) ユーザーアカウントのパスワード(8文字以上20字未満)。\&quot;needActivateFlow\&quot;が\&quot;false\&quot;の場合は必須。 | [optional] 
**role** | **str** | (必須) アカウントのタイプ | 
**need_activate_flow** | **bool** | (任意) アカウントの有効化フローが必要か否か。デフォルト値ではfalse。(true: 必要 /false: 不要) | [optional] 
**group_ids** | **list[str]** | (任意) ユーザーアカウントに紐付けるグループのIDの配列 | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

