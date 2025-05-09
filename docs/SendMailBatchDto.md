# SendMailBatchDto

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** | (必須) メールの件名 | 
**for_every_client** | **bool** | (必須) 全てのクライアントアカウントに対して送信するか (true: 全てのクライアントアカウントに送信, false: 全てのクライアントアカウントに送信しない) | 
**for_every_user** | **bool** | (必須) 全てのユーザーアカウントに対して送信するか (true: 全てのユーザーアカウントに送信, false: 全てのユーザーアカウントに送信しない) | 
**user_ids** | **list[str]** | (任意) メールの送信対象のユーザーアカウント識別子の配列 | [optional] 
**group_ids** | **list[str]** | (任意) 送信対象のグループ識別子の配列。グループを指定した場合グループに紐付くユーザーアカウントとクライアントアカウント全てにメールが送信される | [optional] 
**content** | **str** | (必須) メールの内容 | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

