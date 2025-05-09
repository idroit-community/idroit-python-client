# Mail

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | (必須) 送信済みメールの識別子 | 
**title** | **str** | (必須) 送信済みメールの件名 | 
**content** | **str** | (必須) 送信済みメールの内容 | 
**for_every_user** | **bool** | (必須) 全てのuser権限アカウントに対して送信するか。(true: 全てのuser権限アカウントに送信, false: 全てのuser権限アカウントに送信しない) | 
**for_every_client** | **bool** | (必須) 全てのclient権限アカウントに対して送信するか。(true: 全てのclient権限アカウントに送信, false: 全てのclient権限アカウントに送信しない) | 
**users** | [**list[User]**](User.md) | (任意) メールの送信先となるユーザーアカウントの配列 | [optional] 
**groups** | [**list[Group]**](Group.md) | (任意) メールの送信先となるグループの配列 | [optional] 
**created_by** | [**list[User]**](User.md) | (必須) メール送信操作を行ったAdmin権限アカウント | [optional] 
**created_at** | **str** | (必須) メールの送信日時 | 
**updated_at** | **str** | (必須) メールの送信日時 | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

