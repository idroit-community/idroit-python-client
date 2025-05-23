# coding: utf-8

"""
    iDroit Dashboard Admin API

         これは[株式会社フォアー](https://www.fore-co.ltd/ja/)が開発するを使ったDecentralizd Identifiers / Verifiable Credentials(DID/VC)に関係する機能を簡単に利用するための REST API です。現在以下のユースケースをサポートしています。これは今後も拡張されていきます。     - DIDの生成:      - グループ管理機能       - (企業/プロジェクトのまとまり)ごとにユーザー、クライアント、証明書(VC)スキーマを紐付けて管理する。          詳細は以下を参照してください。     - [idroit dashboard admin UI](https://admin.idroit-dashboard.com)     - [idroit dashboard公式ホームページ]()     - [idroit dashboard操作マニュアル]()      以下は関連リンクです。     - [Universal Resolver](https://dev.uniresolver.io/)     - [W3C DID Core 1.0](https://www.w3.org/TR/did-core/)     - [Verifiable Credentials Data Model v2.0](https://www.w3.org/TR/vc-data-model-2.0/)     # noqa: E501

    OpenAPI spec version: 0.9.2
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class User(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'id': 'str',
        'name': 'str',
        'email': 'str',
        'password': 'str',
        'need_activate_flow': 'bool',
        'status': 'str',
        'role': 'str',
        'created_by': 'AllOfUserCreatedBy',
        'did_infos': 'list[DidInfo]',
        'vc_infos': 'list[VcInfo]',
        'vp_infos': 'list[VpInfo]',
        'groups': 'list[Group]',
        'user_tokens': 'list[UserToken]',
        'created_users': 'list[User]',
        'created_vc_infos': 'list[VcInfo]',
        'created_vp_infos': 'list[VpInfo]',
        'created_groups': 'list[Group]',
        'created_did_infos': 'list[DidInfo]',
        'created_vc_schemas': 'list[VcSchema]',
        'created_verifications': 'list[Verification]',
        'created_mails': 'list[Mail]',
        'created_files': 'list[File]',
        'created_at': 'str',
        'updated_at': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'email': 'email',
        'password': 'password',
        'need_activate_flow': 'needActivateFlow',
        'status': 'status',
        'role': 'role',
        'created_by': 'createdBy',
        'did_infos': 'didInfos',
        'vc_infos': 'vcInfos',
        'vp_infos': 'vpInfos',
        'groups': 'groups',
        'user_tokens': 'userTokens',
        'created_users': 'createdUsers',
        'created_vc_infos': 'createdVcInfos',
        'created_vp_infos': 'createdVpInfos',
        'created_groups': 'createdGroups',
        'created_did_infos': 'createdDidInfos',
        'created_vc_schemas': 'createdVcSchemas',
        'created_verifications': 'createdVerifications',
        'created_mails': 'createdMails',
        'created_files': 'createdFiles',
        'created_at': 'createdAt',
        'updated_at': 'updatedAt'
    }

    def __init__(self, id=None, name=None, email=None, password=None, need_activate_flow=None, status=None, role=None, created_by=None, did_infos=None, vc_infos=None, vp_infos=None, groups=None, user_tokens=None, created_users=None, created_vc_infos=None, created_vp_infos=None, created_groups=None, created_did_infos=None, created_vc_schemas=None, created_verifications=None, created_mails=None, created_files=None, created_at=None, updated_at=None):  # noqa: E501
        """User - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._name = None
        self._email = None
        self._password = None
        self._need_activate_flow = None
        self._status = None
        self._role = None
        self._created_by = None
        self._did_infos = None
        self._vc_infos = None
        self._vp_infos = None
        self._groups = None
        self._user_tokens = None
        self._created_users = None
        self._created_vc_infos = None
        self._created_vp_infos = None
        self._created_groups = None
        self._created_did_infos = None
        self._created_vc_schemas = None
        self._created_verifications = None
        self._created_mails = None
        self._created_files = None
        self._created_at = None
        self._updated_at = None
        self.discriminator = None
        self.id = id
        self.name = name
        self.email = email
        self.password = password
        self.need_activate_flow = need_activate_flow
        self.status = status
        self.role = role
        if created_by is not None:
            self.created_by = created_by
        if did_infos is not None:
            self.did_infos = did_infos
        if vc_infos is not None:
            self.vc_infos = vc_infos
        if vp_infos is not None:
            self.vp_infos = vp_infos
        if groups is not None:
            self.groups = groups
        self.user_tokens = user_tokens
        if created_users is not None:
            self.created_users = created_users
        if created_vc_infos is not None:
            self.created_vc_infos = created_vc_infos
        if created_vp_infos is not None:
            self.created_vp_infos = created_vp_infos
        if created_groups is not None:
            self.created_groups = created_groups
        if created_did_infos is not None:
            self.created_did_infos = created_did_infos
        self.created_vc_schemas = created_vc_schemas
        self.created_verifications = created_verifications
        if created_mails is not None:
            self.created_mails = created_mails
        self.created_files = created_files
        self.created_at = created_at
        self.updated_at = updated_at

    @property
    def id(self):
        """Gets the id of this User.  # noqa: E501

        アカウントの識別子  # noqa: E501

        :return: The id of this User.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this User.

        アカウントの識別子  # noqa: E501

        :param id: The id of this User.  # noqa: E501
        :type: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def name(self):
        """Gets the name of this User.  # noqa: E501

        アカウントの名前  # noqa: E501

        :return: The name of this User.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this User.

        アカウントの名前  # noqa: E501

        :param name: The name of this User.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def email(self):
        """Gets the email of this User.  # noqa: E501

        アカウントのメールアドレス  # noqa: E501

        :return: The email of this User.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this User.

        アカウントのメールアドレス  # noqa: E501

        :param email: The email of this User.  # noqa: E501
        :type: str
        """
        if email is None:
            raise ValueError("Invalid value for `email`, must not be `None`")  # noqa: E501

        self._email = email

    @property
    def password(self):
        """Gets the password of this User.  # noqa: E501

        アカウントのパスワード(8文字以上20字未満)  # noqa: E501

        :return: The password of this User.  # noqa: E501
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """Sets the password of this User.

        アカウントのパスワード(8文字以上20字未満)  # noqa: E501

        :param password: The password of this User.  # noqa: E501
        :type: str
        """
        if password is None:
            raise ValueError("Invalid value for `password`, must not be `None`")  # noqa: E501

        self._password = password

    @property
    def need_activate_flow(self):
        """Gets the need_activate_flow of this User.  # noqa: E501

        (必須: {default: false}) アカウントの有効化フローが必要か否か(true: 必要 /false: 不要)  # noqa: E501

        :return: The need_activate_flow of this User.  # noqa: E501
        :rtype: bool
        """
        return self._need_activate_flow

    @need_activate_flow.setter
    def need_activate_flow(self, need_activate_flow):
        """Sets the need_activate_flow of this User.

        (必須: {default: false}) アカウントの有効化フローが必要か否か(true: 必要 /false: 不要)  # noqa: E501

        :param need_activate_flow: The need_activate_flow of this User.  # noqa: E501
        :type: bool
        """
        if need_activate_flow is None:
            raise ValueError("Invalid value for `need_activate_flow`, must not be `None`")  # noqa: E501

        self._need_activate_flow = need_activate_flow

    @property
    def status(self):
        """Gets the status of this User.  # noqa: E501

        ユーザーのアカウントステータス  # noqa: E501

        :return: The status of this User.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this User.

        ユーザーのアカウントステータス  # noqa: E501

        :param status: The status of this User.  # noqa: E501
        :type: str
        """
        if status is None:
            raise ValueError("Invalid value for `status`, must not be `None`")  # noqa: E501
        allowed_values = ["inactive", "activating", "active", "deactive"]  # noqa: E501
        if status not in allowed_values:
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"  # noqa: E501
                .format(status, allowed_values)
            )

        self._status = status

    @property
    def role(self):
        """Gets the role of this User.  # noqa: E501

        アカウントのロール(admin/user/clinet)  # noqa: E501

        :return: The role of this User.  # noqa: E501
        :rtype: str
        """
        return self._role

    @role.setter
    def role(self, role):
        """Sets the role of this User.

        アカウントのロール(admin/user/clinet)  # noqa: E501

        :param role: The role of this User.  # noqa: E501
        :type: str
        """
        if role is None:
            raise ValueError("Invalid value for `role`, must not be `None`")  # noqa: E501
        allowed_values = ["admin", "user", "client"]  # noqa: E501
        if role not in allowed_values:
            raise ValueError(
                "Invalid value for `role` ({0}), must be one of {1}"  # noqa: E501
                .format(role, allowed_values)
            )

        self._role = role

    @property
    def created_by(self):
        """Gets the created_by of this User.  # noqa: E501

        (任意) このアカウントを作成したユーザー  # noqa: E501

        :return: The created_by of this User.  # noqa: E501
        :rtype: AllOfUserCreatedBy
        """
        return self._created_by

    @created_by.setter
    def created_by(self, created_by):
        """Sets the created_by of this User.

        (任意) このアカウントを作成したユーザー  # noqa: E501

        :param created_by: The created_by of this User.  # noqa: E501
        :type: AllOfUserCreatedBy
        """

        self._created_by = created_by

    @property
    def did_infos(self):
        """Gets the did_infos of this User.  # noqa: E501

        (任意) アカウントに紐付けされたDID情報の配列  # noqa: E501

        :return: The did_infos of this User.  # noqa: E501
        :rtype: list[DidInfo]
        """
        return self._did_infos

    @did_infos.setter
    def did_infos(self, did_infos):
        """Sets the did_infos of this User.

        (任意) アカウントに紐付けされたDID情報の配列  # noqa: E501

        :param did_infos: The did_infos of this User.  # noqa: E501
        :type: list[DidInfo]
        """

        self._did_infos = did_infos

    @property
    def vc_infos(self):
        """Gets the vc_infos of this User.  # noqa: E501

        (任意) アカウントに紐付けされたVC情報の配列  # noqa: E501

        :return: The vc_infos of this User.  # noqa: E501
        :rtype: list[VcInfo]
        """
        return self._vc_infos

    @vc_infos.setter
    def vc_infos(self, vc_infos):
        """Sets the vc_infos of this User.

        (任意) アカウントに紐付けされたVC情報の配列  # noqa: E501

        :param vc_infos: The vc_infos of this User.  # noqa: E501
        :type: list[VcInfo]
        """

        self._vc_infos = vc_infos

    @property
    def vp_infos(self):
        """Gets the vp_infos of this User.  # noqa: E501

        (任意) アカウントに紐付けされたVP情報の配列  # noqa: E501

        :return: The vp_infos of this User.  # noqa: E501
        :rtype: list[VpInfo]
        """
        return self._vp_infos

    @vp_infos.setter
    def vp_infos(self, vp_infos):
        """Sets the vp_infos of this User.

        (任意) アカウントに紐付けされたVP情報の配列  # noqa: E501

        :param vp_infos: The vp_infos of this User.  # noqa: E501
        :type: list[VpInfo]
        """

        self._vp_infos = vp_infos

    @property
    def groups(self):
        """Gets the groups of this User.  # noqa: E501

        (任意) アカウントに紐付けされたグループの配列  # noqa: E501

        :return: The groups of this User.  # noqa: E501
        :rtype: list[Group]
        """
        return self._groups

    @groups.setter
    def groups(self, groups):
        """Sets the groups of this User.

        (任意) アカウントに紐付けされたグループの配列  # noqa: E501

        :param groups: The groups of this User.  # noqa: E501
        :type: list[Group]
        """

        self._groups = groups

    @property
    def user_tokens(self):
        """Gets the user_tokens of this User.  # noqa: E501

        (任意) ユーザーアカウントがアップロードしたファイルの配列。  # noqa: E501

        :return: The user_tokens of this User.  # noqa: E501
        :rtype: list[UserToken]
        """
        return self._user_tokens

    @user_tokens.setter
    def user_tokens(self, user_tokens):
        """Sets the user_tokens of this User.

        (任意) ユーザーアカウントがアップロードしたファイルの配列。  # noqa: E501

        :param user_tokens: The user_tokens of this User.  # noqa: E501
        :type: list[UserToken]
        """
        if user_tokens is None:
            raise ValueError("Invalid value for `user_tokens`, must not be `None`")  # noqa: E501

        self._user_tokens = user_tokens

    @property
    def created_users(self):
        """Gets the created_users of this User.  # noqa: E501

        (任意) このユーザーによって作成されたアカウントの配列  # noqa: E501

        :return: The created_users of this User.  # noqa: E501
        :rtype: list[User]
        """
        return self._created_users

    @created_users.setter
    def created_users(self, created_users):
        """Sets the created_users of this User.

        (任意) このユーザーによって作成されたアカウントの配列  # noqa: E501

        :param created_users: The created_users of this User.  # noqa: E501
        :type: list[User]
        """

        self._created_users = created_users

    @property
    def created_vc_infos(self):
        """Gets the created_vc_infos of this User.  # noqa: E501

        (任意) アカウントに紐付けされたVC情報の配列  # noqa: E501

        :return: The created_vc_infos of this User.  # noqa: E501
        :rtype: list[VcInfo]
        """
        return self._created_vc_infos

    @created_vc_infos.setter
    def created_vc_infos(self, created_vc_infos):
        """Sets the created_vc_infos of this User.

        (任意) アカウントに紐付けされたVC情報の配列  # noqa: E501

        :param created_vc_infos: The created_vc_infos of this User.  # noqa: E501
        :type: list[VcInfo]
        """

        self._created_vc_infos = created_vc_infos

    @property
    def created_vp_infos(self):
        """Gets the created_vp_infos of this User.  # noqa: E501

        (任意) アカウントに紐付けされたVP情報の配列  # noqa: E501

        :return: The created_vp_infos of this User.  # noqa: E501
        :rtype: list[VpInfo]
        """
        return self._created_vp_infos

    @created_vp_infos.setter
    def created_vp_infos(self, created_vp_infos):
        """Sets the created_vp_infos of this User.

        (任意) アカウントに紐付けされたVP情報の配列  # noqa: E501

        :param created_vp_infos: The created_vp_infos of this User.  # noqa: E501
        :type: list[VpInfo]
        """

        self._created_vp_infos = created_vp_infos

    @property
    def created_groups(self):
        """Gets the created_groups of this User.  # noqa: E501

        (任意) アカウントに作成したグループの配列  # noqa: E501

        :return: The created_groups of this User.  # noqa: E501
        :rtype: list[Group]
        """
        return self._created_groups

    @created_groups.setter
    def created_groups(self, created_groups):
        """Sets the created_groups of this User.

        (任意) アカウントに作成したグループの配列  # noqa: E501

        :param created_groups: The created_groups of this User.  # noqa: E501
        :type: list[Group]
        """

        self._created_groups = created_groups

    @property
    def created_did_infos(self):
        """Gets the created_did_infos of this User.  # noqa: E501

        (任意) アカウントが作成したDID情報の配列  # noqa: E501

        :return: The created_did_infos of this User.  # noqa: E501
        :rtype: list[DidInfo]
        """
        return self._created_did_infos

    @created_did_infos.setter
    def created_did_infos(self, created_did_infos):
        """Sets the created_did_infos of this User.

        (任意) アカウントが作成したDID情報の配列  # noqa: E501

        :param created_did_infos: The created_did_infos of this User.  # noqa: E501
        :type: list[DidInfo]
        """

        self._created_did_infos = created_did_infos

    @property
    def created_vc_schemas(self):
        """Gets the created_vc_schemas of this User.  # noqa: E501

        (任意) ユーザーアカウントが作成したVCスキーマの配列。  # noqa: E501

        :return: The created_vc_schemas of this User.  # noqa: E501
        :rtype: list[VcSchema]
        """
        return self._created_vc_schemas

    @created_vc_schemas.setter
    def created_vc_schemas(self, created_vc_schemas):
        """Sets the created_vc_schemas of this User.

        (任意) ユーザーアカウントが作成したVCスキーマの配列。  # noqa: E501

        :param created_vc_schemas: The created_vc_schemas of this User.  # noqa: E501
        :type: list[VcSchema]
        """
        if created_vc_schemas is None:
            raise ValueError("Invalid value for `created_vc_schemas`, must not be `None`")  # noqa: E501

        self._created_vc_schemas = created_vc_schemas

    @property
    def created_verifications(self):
        """Gets the created_verifications of this User.  # noqa: E501

        (任意) ユーザーアカウントが実行した検証結果の配列。  # noqa: E501

        :return: The created_verifications of this User.  # noqa: E501
        :rtype: list[Verification]
        """
        return self._created_verifications

    @created_verifications.setter
    def created_verifications(self, created_verifications):
        """Sets the created_verifications of this User.

        (任意) ユーザーアカウントが実行した検証結果の配列。  # noqa: E501

        :param created_verifications: The created_verifications of this User.  # noqa: E501
        :type: list[Verification]
        """
        if created_verifications is None:
            raise ValueError("Invalid value for `created_verifications`, must not be `None`")  # noqa: E501

        self._created_verifications = created_verifications

    @property
    def created_mails(self):
        """Gets the created_mails of this User.  # noqa: E501

        (任意) Admin権限アカウントが送信したメールの配列(Adminロール以外の場合、関係のないカラム)  # noqa: E501

        :return: The created_mails of this User.  # noqa: E501
        :rtype: list[Mail]
        """
        return self._created_mails

    @created_mails.setter
    def created_mails(self, created_mails):
        """Sets the created_mails of this User.

        (任意) Admin権限アカウントが送信したメールの配列(Adminロール以外の場合、関係のないカラム)  # noqa: E501

        :param created_mails: The created_mails of this User.  # noqa: E501
        :type: list[Mail]
        """

        self._created_mails = created_mails

    @property
    def created_files(self):
        """Gets the created_files of this User.  # noqa: E501

        (任意) ユーザーアカウントがアップロードしたファイルの配列。  # noqa: E501

        :return: The created_files of this User.  # noqa: E501
        :rtype: list[File]
        """
        return self._created_files

    @created_files.setter
    def created_files(self, created_files):
        """Sets the created_files of this User.

        (任意) ユーザーアカウントがアップロードしたファイルの配列。  # noqa: E501

        :param created_files: The created_files of this User.  # noqa: E501
        :type: list[File]
        """
        if created_files is None:
            raise ValueError("Invalid value for `created_files`, must not be `None`")  # noqa: E501

        self._created_files = created_files

    @property
    def created_at(self):
        """Gets the created_at of this User.  # noqa: E501

        ユーザーアカウントの作成日時  # noqa: E501

        :return: The created_at of this User.  # noqa: E501
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this User.

        ユーザーアカウントの作成日時  # noqa: E501

        :param created_at: The created_at of this User.  # noqa: E501
        :type: str
        """
        if created_at is None:
            raise ValueError("Invalid value for `created_at`, must not be `None`")  # noqa: E501

        self._created_at = created_at

    @property
    def updated_at(self):
        """Gets the updated_at of this User.  # noqa: E501

        ユーザーアカウントの更新日時  # noqa: E501

        :return: The updated_at of this User.  # noqa: E501
        :rtype: str
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this User.

        ユーザーアカウントの更新日時  # noqa: E501

        :param updated_at: The updated_at of this User.  # noqa: E501
        :type: str
        """
        if updated_at is None:
            raise ValueError("Invalid value for `updated_at`, must not be `None`")  # noqa: E501

        self._updated_at = updated_at

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(User, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, User):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
