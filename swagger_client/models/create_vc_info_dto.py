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

class CreateVcInfoDto(object):
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
        'issuer': 'str',
        'vc_schema_id': 'str',
        'credential_subject': 'object',
        'label': 'str',
        'description': 'str'
    }

    attribute_map = {
        'issuer': 'issuer',
        'vc_schema_id': 'vcSchemaId',
        'credential_subject': 'credentialSubject',
        'label': 'label',
        'description': 'description'
    }

    def __init__(self, issuer=None, vc_schema_id=None, credential_subject=None, label=None, description=None):  # noqa: E501
        """CreateVcInfoDto - a model defined in Swagger"""  # noqa: E501
        self._issuer = None
        self._vc_schema_id = None
        self._credential_subject = None
        self._label = None
        self._description = None
        self.discriminator = None
        self.issuer = issuer
        self.vc_schema_id = vc_schema_id
        self.credential_subject = credential_subject
        if label is not None:
            self.label = label
        if description is not None:
            self.description = description

    @property
    def issuer(self):
        """Gets the issuer of this CreateVcInfoDto.  # noqa: E501

        (必須) VCの発行者の識別子として用いる文字列の値。現在はDIDのみがサポートされていますが、今後のアップデートでDID以外の文字列をサポートする予定です。  # noqa: E501

        :return: The issuer of this CreateVcInfoDto.  # noqa: E501
        :rtype: str
        """
        return self._issuer

    @issuer.setter
    def issuer(self, issuer):
        """Sets the issuer of this CreateVcInfoDto.

        (必須) VCの発行者の識別子として用いる文字列の値。現在はDIDのみがサポートされていますが、今後のアップデートでDID以外の文字列をサポートする予定です。  # noqa: E501

        :param issuer: The issuer of this CreateVcInfoDto.  # noqa: E501
        :type: str
        """
        if issuer is None:
            raise ValueError("Invalid value for `issuer`, must not be `None`")  # noqa: E501

        self._issuer = issuer

    @property
    def vc_schema_id(self):
        """Gets the vc_schema_id of this CreateVcInfoDto.  # noqa: E501

        (必須) 新規発行するVCの元となるVCスキーマの識別子  # noqa: E501

        :return: The vc_schema_id of this CreateVcInfoDto.  # noqa: E501
        :rtype: str
        """
        return self._vc_schema_id

    @vc_schema_id.setter
    def vc_schema_id(self, vc_schema_id):
        """Sets the vc_schema_id of this CreateVcInfoDto.

        (必須) 新規発行するVCの元となるVCスキーマの識別子  # noqa: E501

        :param vc_schema_id: The vc_schema_id of this CreateVcInfoDto.  # noqa: E501
        :type: str
        """
        if vc_schema_id is None:
            raise ValueError("Invalid value for `vc_schema_id`, must not be `None`")  # noqa: E501

        self._vc_schema_id = vc_schema_id

    @property
    def credential_subject(self):
        """Gets the credential_subject of this CreateVcInfoDto.  # noqa: E501

        (必須) VCの主張内容(クレーム)となる値のオブジェクト型の値  # noqa: E501

        :return: The credential_subject of this CreateVcInfoDto.  # noqa: E501
        :rtype: object
        """
        return self._credential_subject

    @credential_subject.setter
    def credential_subject(self, credential_subject):
        """Sets the credential_subject of this CreateVcInfoDto.

        (必須) VCの主張内容(クレーム)となる値のオブジェクト型の値  # noqa: E501

        :param credential_subject: The credential_subject of this CreateVcInfoDto.  # noqa: E501
        :type: object
        """
        if credential_subject is None:
            raise ValueError("Invalid value for `credential_subject`, must not be `None`")  # noqa: E501

        self._credential_subject = credential_subject

    @property
    def label(self):
        """Gets the label of this CreateVcInfoDto.  # noqa: E501

        (任意) VCの識別や整理などの管理するにあったてメタデータとして任意で設定可能な単語のフレーズ。(例: vc-for-project1)  # noqa: E501

        :return: The label of this CreateVcInfoDto.  # noqa: E501
        :rtype: str
        """
        return self._label

    @label.setter
    def label(self, label):
        """Sets the label of this CreateVcInfoDto.

        (任意) VCの識別や整理などの管理するにあったてメタデータとして任意で設定可能な単語のフレーズ。(例: vc-for-project1)  # noqa: E501

        :param label: The label of this CreateVcInfoDto.  # noqa: E501
        :type: str
        """

        self._label = label

    @property
    def description(self):
        """Gets the description of this CreateVcInfoDto.  # noqa: E501

        (任意) VCの発行目的や用途など任意で設定可能な説明文  # noqa: E501

        :return: The description of this CreateVcInfoDto.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this CreateVcInfoDto.

        (任意) VCの発行目的や用途など任意で設定可能な説明文  # noqa: E501

        :param description: The description of this CreateVcInfoDto.  # noqa: E501
        :type: str
        """

        self._description = description

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
        if issubclass(CreateVcInfoDto, dict):
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
        if not isinstance(other, CreateVcInfoDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
