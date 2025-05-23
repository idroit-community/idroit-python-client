# coding: utf-8

"""
    iDroit Dashboard Admin API

         これは[株式会社フォアー](https://www.fore-co.ltd/ja/)が開発するを使ったDecentralizd Identifiers / Verifiable Credentials(DID/VC)に関係する機能を簡単に利用するための REST API です。現在以下のユースケースをサポートしています。これは今後も拡張されていきます。     - DIDの生成:      - グループ管理機能       - (企業/プロジェクトのまとまり)ごとにユーザー、クライアント、証明書(VC)スキーマを紐付けて管理する。          詳細は以下を参照してください。     - [idroit dashboard admin UI](https://admin.idroit-dashboard.com)     - [idroit dashboard公式ホームページ]()     - [idroit dashboard操作マニュアル]()      以下は関連リンクです。     - [Universal Resolver](https://dev.uniresolver.io/)     - [W3C DID Core 1.0](https://www.w3.org/TR/did-core/)     - [Verifiable Credentials Data Model v2.0](https://www.w3.org/TR/vc-data-model-2.0/)     # noqa: E501

    OpenAPI spec version: 0.9.2
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from swagger_client.api_client import ApiClient


class VpInfosApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def vp_infos_controller_add_label(self, body, id, **kwargs):  # noqa: E501
        """VP情報へのラベル追加  # noqa: E501

        リクエストパラメータのidで指定された単一のVP情報に対して、任意の管理用ラベルを追加します。  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.vp_infos_controller_add_label(body, id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param AddLabelToVpInfoDto body: (required)
        :param str id: (required)
        :return: VpInfoResponseDto
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.vp_infos_controller_add_label_with_http_info(body, id, **kwargs)  # noqa: E501
        else:
            (data) = self.vp_infos_controller_add_label_with_http_info(body, id, **kwargs)  # noqa: E501
            return data

    def vp_infos_controller_add_label_with_http_info(self, body, id, **kwargs):  # noqa: E501
        """VP情報へのラベル追加  # noqa: E501

        リクエストパラメータのidで指定された単一のVP情報に対して、任意の管理用ラベルを追加します。  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.vp_infos_controller_add_label_with_http_info(body, id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param AddLabelToVpInfoDto body: (required)
        :param str id: (required)
        :return: VpInfoResponseDto
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method vp_infos_controller_add_label" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `vp_infos_controller_add_label`")  # noqa: E501
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `vp_infos_controller_add_label`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['bearer']  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/vp-infos/{id}/label', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='VpInfoResponseDto',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def vp_infos_controller_connect_user(self, body, id, **kwargs):  # noqa: E501
        """VP情報へのクライアントアカウント紐付け  # noqa: E501

        VP情報の所有者、関係者などの管理者としてクライアントアカウントを紐付けます。  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.vp_infos_controller_connect_user(body, id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param UpdateVcInfoDto body: (required)
        :param str id: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.vp_infos_controller_connect_user_with_http_info(body, id, **kwargs)  # noqa: E501
        else:
            (data) = self.vp_infos_controller_connect_user_with_http_info(body, id, **kwargs)  # noqa: E501
            return data

    def vp_infos_controller_connect_user_with_http_info(self, body, id, **kwargs):  # noqa: E501
        """VP情報へのクライアントアカウント紐付け  # noqa: E501

        VP情報の所有者、関係者などの管理者としてクライアントアカウントを紐付けます。  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.vp_infos_controller_connect_user_with_http_info(body, id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param UpdateVcInfoDto body: (required)
        :param str id: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method vp_infos_controller_connect_user" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `vp_infos_controller_connect_user`")  # noqa: E501
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `vp_infos_controller_connect_user`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['bearer']  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/vp-infos/{id}', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def vp_infos_controller_create(self, body, **kwargs):  # noqa: E501
        """新規VP生成  # noqa: E501

        新規VPを生成します。  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.vp_infos_controller_create(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param CreateVpInfoDto body: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.vp_infos_controller_create_with_http_info(body, **kwargs)  # noqa: E501
        else:
            (data) = self.vp_infos_controller_create_with_http_info(body, **kwargs)  # noqa: E501
            return data

    def vp_infos_controller_create_with_http_info(self, body, **kwargs):  # noqa: E501
        """新規VP生成  # noqa: E501

        新規VPを生成します。  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.vp_infos_controller_create_with_http_info(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param CreateVpInfoDto body: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method vp_infos_controller_create" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `vp_infos_controller_create`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['bearer']  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/vp-infos', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def vp_infos_controller_disconnect_user(self, id, **kwargs):  # noqa: E501
        """VP情報のクライアントアカウント紐付け解除  # noqa: E501

        VP情報に紐付いたクライアントアカウントの紐付けを解除します。  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.vp_infos_controller_disconnect_user(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.vp_infos_controller_disconnect_user_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.vp_infos_controller_disconnect_user_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def vp_infos_controller_disconnect_user_with_http_info(self, id, **kwargs):  # noqa: E501
        """VP情報のクライアントアカウント紐付け解除  # noqa: E501

        VP情報に紐付いたクライアントアカウントの紐付けを解除します。  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.vp_infos_controller_disconnect_user_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method vp_infos_controller_disconnect_user" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `vp_infos_controller_disconnect_user`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = ['bearer']  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/vp-infos/{id}/user', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def vp_infos_controller_find_all(self, **kwargs):  # noqa: E501
        """VP情報一覧取得  # noqa: E501

        アプリケーションが管理するVP情報を一覧として値を返します。  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.vp_infos_controller_find_all(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param float page: (必須) ページネーションを表示する際のページ数に当たるクエリパラメーター。全件取得する際は1を指定。(デフォルト: 1)
        :param float limit: (必須) ページネーションを表示する際のページ数あたりに表示する件数を指定するクエリパラメーター。全件取得する際は0を指定。(デフォルト: 10)
        :param str label: (任意) 例: \"vc-for-project1\"
        :param str description: (任意) 
        :return: VpInfoResponseDto
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.vp_infos_controller_find_all_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.vp_infos_controller_find_all_with_http_info(**kwargs)  # noqa: E501
            return data

    def vp_infos_controller_find_all_with_http_info(self, **kwargs):  # noqa: E501
        """VP情報一覧取得  # noqa: E501

        アプリケーションが管理するVP情報を一覧として値を返します。  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.vp_infos_controller_find_all_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param float page: (必須) ページネーションを表示する際のページ数に当たるクエリパラメーター。全件取得する際は1を指定。(デフォルト: 1)
        :param float limit: (必須) ページネーションを表示する際のページ数あたりに表示する件数を指定するクエリパラメーター。全件取得する際は0を指定。(デフォルト: 10)
        :param str label: (任意) 例: \"vc-for-project1\"
        :param str description: (任意) 
        :return: VpInfoResponseDto
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['page', 'limit', 'label', 'description']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method vp_infos_controller_find_all" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'page' in params:
            query_params.append(('page', params['page']))  # noqa: E501
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501
        if 'label' in params:
            query_params.append(('label', params['label']))  # noqa: E501
        if 'description' in params:
            query_params.append(('description', params['description']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['bearer']  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/vp-infos', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='VpInfoResponseDto',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def vp_infos_controller_find_one(self, id, **kwargs):  # noqa: E501
        """VP情報詳細取得  # noqa: E501

        リクエストパラメータのidで指定された単一のVP情報の詳細情報の値を返します。  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.vp_infos_controller_find_one(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: (required)
        :return: VpInfoDetailDto
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.vp_infos_controller_find_one_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.vp_infos_controller_find_one_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def vp_infos_controller_find_one_with_http_info(self, id, **kwargs):  # noqa: E501
        """VP情報詳細取得  # noqa: E501

        リクエストパラメータのidで指定された単一のVP情報の詳細情報の値を返します。  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.vp_infos_controller_find_one_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: (required)
        :return: VpInfoDetailDto
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method vp_infos_controller_find_one" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `vp_infos_controller_find_one`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['bearer']  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/vp-infos/{id}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='VpInfoDetailDto',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def vp_infos_controller_upload(self, credential_object, label, description, **kwargs):  # noqa: E501
        """新規VPアップロード  # noqa: E501

        外部で発行された既存VPをアップロードし、本アプリケーションに保存します。。  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.vp_infos_controller_upload(credential_object, label, description, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object credential_object: (required)
        :param str label: (required)
        :param str description: (required)
        :return: VpInfoResponseDto
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.vp_infos_controller_upload_with_http_info(credential_object, label, description, **kwargs)  # noqa: E501
        else:
            (data) = self.vp_infos_controller_upload_with_http_info(credential_object, label, description, **kwargs)  # noqa: E501
            return data

    def vp_infos_controller_upload_with_http_info(self, credential_object, label, description, **kwargs):  # noqa: E501
        """新規VPアップロード  # noqa: E501

        外部で発行された既存VPをアップロードし、本アプリケーションに保存します。。  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.vp_infos_controller_upload_with_http_info(credential_object, label, description, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object credential_object: (required)
        :param str label: (required)
        :param str description: (required)
        :return: VpInfoResponseDto
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['credential_object', 'label', 'description']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method vp_infos_controller_upload" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'credential_object' is set
        if ('credential_object' not in params or
                params['credential_object'] is None):
            raise ValueError("Missing the required parameter `credential_object` when calling `vp_infos_controller_upload`")  # noqa: E501
        # verify the required parameter 'label' is set
        if ('label' not in params or
                params['label'] is None):
            raise ValueError("Missing the required parameter `label` when calling `vp_infos_controller_upload`")  # noqa: E501
        # verify the required parameter 'description' is set
        if ('description' not in params or
                params['description'] is None):
            raise ValueError("Missing the required parameter `description` when calling `vp_infos_controller_upload`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}
        if 'credential_object' in params:
            form_params.append(('credentialObject', params['credential_object']))  # noqa: E501
        if 'label' in params:
            form_params.append(('label', params['label']))  # noqa: E501
        if 'description' in params:
            form_params.append(('description', params['description']))  # noqa: E501

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['multipart/form-data'])  # noqa: E501

        # Authentication setting
        auth_settings = ['bearer']  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/vp-infos/upload', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='VpInfoResponseDto',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
