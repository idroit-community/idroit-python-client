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

class VcInfo(object):
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
        'label': 'str',
        'hash': 'str',
        'description': 'str',
        'created_by': 'AllOfVcInfoCreatedBy',
        'vc_schema': 'AllOfVcInfoVcSchema',
        'user': 'AllOfVcInfoUser',
        'vp_infos': 'list[VpInfo]',
        'groups': 'list[Group]',
        'badge': 'AllOfVcInfoBadge',
        'verifications': 'list[Verification]',
        'created_at': 'str',
        'updated_at': 'str'
    }

    attribute_map = {
        'id': 'id',
        'label': 'label',
        'hash': 'hash',
        'description': 'description',
        'created_by': 'createdBy',
        'vc_schema': 'vcSchema',
        'user': 'user',
        'vp_infos': 'vpInfos',
        'groups': 'groups',
        'badge': 'badge',
        'verifications': 'verifications',
        'created_at': 'createdAt',
        'updated_at': 'updatedAt'
    }

    def __init__(self, id=None, label=None, hash=None, description=None, created_by=None, vc_schema=None, user=None, vp_infos=None, groups=None, badge=None, verifications=None, created_at=None, updated_at=None):  # noqa: E501
        """VcInfo - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._label = None
        self._hash = None
        self._description = None
        self._created_by = None
        self._vc_schema = None
        self._user = None
        self._vp_infos = None
        self._groups = None
        self._badge = None
        self._verifications = None
        self._created_at = None
        self._updated_at = None
        self.discriminator = None
        self.id = id
        self.label = label
        self.hash = hash
        self.description = description
        self.created_by = created_by
        if vc_schema is not None:
            self.vc_schema = vc_schema
        if user is not None:
            self.user = user
        if vp_infos is not None:
            self.vp_infos = vp_infos
        if groups is not None:
            self.groups = groups
        if badge is not None:
            self.badge = badge
        if verifications is not None:
            self.verifications = verifications
        self.created_at = created_at
        self.updated_at = updated_at

    @property
    def id(self):
        """Gets the id of this VcInfo.  # noqa: E501

        (必須) VC情報の識別子  # noqa: E501

        :return: The id of this VcInfo.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this VcInfo.

        (必須) VC情報の識別子  # noqa: E501

        :param id: The id of this VcInfo.  # noqa: E501
        :type: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def label(self):
        """Gets the label of this VcInfo.  # noqa: E501

        (任意) VCの識別や整理などの管理するにあったてメタデータとして任意で設定可能な単語のフレーズ。(例: vc-for-project1)  # noqa: E501

        :return: The label of this VcInfo.  # noqa: E501
        :rtype: str
        """
        return self._label

    @label.setter
    def label(self, label):
        """Sets the label of this VcInfo.

        (任意) VCの識別や整理などの管理するにあったてメタデータとして任意で設定可能な単語のフレーズ。(例: vc-for-project1)  # noqa: E501

        :param label: The label of this VcInfo.  # noqa: E501
        :type: str
        """
        if label is None:
            raise ValueError("Invalid value for `label`, must not be `None`")  # noqa: E501

        self._label = label

    @property
    def hash(self):
        """Gets the hash of this VcInfo.  # noqa: E501

        (必須) VCのハッシュ値。VCの保管における識別子として用いる。  # noqa: E501

        :return: The hash of this VcInfo.  # noqa: E501
        :rtype: str
        """
        return self._hash

    @hash.setter
    def hash(self, hash):
        """Sets the hash of this VcInfo.

        (必須) VCのハッシュ値。VCの保管における識別子として用いる。  # noqa: E501

        :param hash: The hash of this VcInfo.  # noqa: E501
        :type: str
        """
        if hash is None:
            raise ValueError("Invalid value for `hash`, must not be `None`")  # noqa: E501

        self._hash = hash

    @property
    def description(self):
        """Gets the description of this VcInfo.  # noqa: E501

        (任意) VCの発行目的や用途など任意で設定可能な説明文。  # noqa: E501

        :return: The description of this VcInfo.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this VcInfo.

        (任意) VCの発行目的や用途など任意で設定可能な説明文。  # noqa: E501

        :param description: The description of this VcInfo.  # noqa: E501
        :type: str
        """
        if description is None:
            raise ValueError("Invalid value for `description`, must not be `None`")  # noqa: E501

        self._description = description

    @property
    def created_by(self):
        """Gets the created_by of this VcInfo.  # noqa: E501

        (任意) VC情報を生成したユーザーアカウント  # noqa: E501

        :return: The created_by of this VcInfo.  # noqa: E501
        :rtype: AllOfVcInfoCreatedBy
        """
        return self._created_by

    @created_by.setter
    def created_by(self, created_by):
        """Sets the created_by of this VcInfo.

        (任意) VC情報を生成したユーザーアカウント  # noqa: E501

        :param created_by: The created_by of this VcInfo.  # noqa: E501
        :type: AllOfVcInfoCreatedBy
        """
        if created_by is None:
            raise ValueError("Invalid value for `created_by`, must not be `None`")  # noqa: E501

        self._created_by = created_by

    @property
    def vc_schema(self):
        """Gets the vc_schema of this VcInfo.  # noqa: E501

        (任意) 発行したVCの元となるVCスキーマ  # noqa: E501

        :return: The vc_schema of this VcInfo.  # noqa: E501
        :rtype: AllOfVcInfoVcSchema
        """
        return self._vc_schema

    @vc_schema.setter
    def vc_schema(self, vc_schema):
        """Sets the vc_schema of this VcInfo.

        (任意) 発行したVCの元となるVCスキーマ  # noqa: E501

        :param vc_schema: The vc_schema of this VcInfo.  # noqa: E501
        :type: AllOfVcInfoVcSchema
        """

        self._vc_schema = vc_schema

    @property
    def user(self):
        """Gets the user of this VcInfo.  # noqa: E501

        (任意) VC情報と紐付いたアカウント  # noqa: E501

        :return: The user of this VcInfo.  # noqa: E501
        :rtype: AllOfVcInfoUser
        """
        return self._user

    @user.setter
    def user(self, user):
        """Sets the user of this VcInfo.

        (任意) VC情報と紐付いたアカウント  # noqa: E501

        :param user: The user of this VcInfo.  # noqa: E501
        :type: AllOfVcInfoUser
        """

        self._user = user

    @property
    def vp_infos(self):
        """Gets the vp_infos of this VcInfo.  # noqa: E501

        (任意) このVCを元に生成したVP情報の配列  # noqa: E501

        :return: The vp_infos of this VcInfo.  # noqa: E501
        :rtype: list[VpInfo]
        """
        return self._vp_infos

    @vp_infos.setter
    def vp_infos(self, vp_infos):
        """Sets the vp_infos of this VcInfo.

        (任意) このVCを元に生成したVP情報の配列  # noqa: E501

        :param vp_infos: The vp_infos of this VcInfo.  # noqa: E501
        :type: list[VpInfo]
        """

        self._vp_infos = vp_infos

    @property
    def groups(self):
        """Gets the groups of this VcInfo.  # noqa: E501

        (任意) VC情報に紐づいたグループの配列  # noqa: E501

        :return: The groups of this VcInfo.  # noqa: E501
        :rtype: list[Group]
        """
        return self._groups

    @groups.setter
    def groups(self, groups):
        """Sets the groups of this VcInfo.

        (任意) VC情報に紐づいたグループの配列  # noqa: E501

        :param groups: The groups of this VcInfo.  # noqa: E501
        :type: list[Group]
        """

        self._groups = groups

    @property
    def badge(self):
        """Gets the badge of this VcInfo.  # noqa: E501

        (任意) VC情報と紐付いたバッジ  # noqa: E501

        :return: The badge of this VcInfo.  # noqa: E501
        :rtype: AllOfVcInfoBadge
        """
        return self._badge

    @badge.setter
    def badge(self, badge):
        """Sets the badge of this VcInfo.

        (任意) VC情報と紐付いたバッジ  # noqa: E501

        :param badge: The badge of this VcInfo.  # noqa: E501
        :type: AllOfVcInfoBadge
        """

        self._badge = badge

    @property
    def verifications(self):
        """Gets the verifications of this VcInfo.  # noqa: E501

        (任意) このVCの検証結果の配列。  # noqa: E501

        :return: The verifications of this VcInfo.  # noqa: E501
        :rtype: list[Verification]
        """
        return self._verifications

    @verifications.setter
    def verifications(self, verifications):
        """Sets the verifications of this VcInfo.

        (任意) このVCの検証結果の配列。  # noqa: E501

        :param verifications: The verifications of this VcInfo.  # noqa: E501
        :type: list[Verification]
        """

        self._verifications = verifications

    @property
    def created_at(self):
        """Gets the created_at of this VcInfo.  # noqa: E501

        (必須) VC情報の作成日時  # noqa: E501

        :return: The created_at of this VcInfo.  # noqa: E501
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this VcInfo.

        (必須) VC情報の作成日時  # noqa: E501

        :param created_at: The created_at of this VcInfo.  # noqa: E501
        :type: str
        """
        if created_at is None:
            raise ValueError("Invalid value for `created_at`, must not be `None`")  # noqa: E501

        self._created_at = created_at

    @property
    def updated_at(self):
        """Gets the updated_at of this VcInfo.  # noqa: E501

        (必須) VC情報の更新日時  # noqa: E501

        :return: The updated_at of this VcInfo.  # noqa: E501
        :rtype: str
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this VcInfo.

        (必須) VC情報の更新日時  # noqa: E501

        :param updated_at: The updated_at of this VcInfo.  # noqa: E501
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
        if issubclass(VcInfo, dict):
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
        if not isinstance(other, VcInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
