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

class VerificationDto(object):
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
        'label': 'str',
        'vc_info_id': 'str',
        'vp_info_id': 'str',
        'vc_object': 'object',
        'vp_object': 'object'
    }

    attribute_map = {
        'label': 'label',
        'vc_info_id': 'vcInfoId',
        'vp_info_id': 'vpInfoId',
        'vc_object': 'vcObject',
        'vp_object': 'vpObject'
    }

    def __init__(self, label=None, vc_info_id=None, vp_info_id=None, vc_object=None, vp_object=None):  # noqa: E501
        """VerificationDto - a model defined in Swagger"""  # noqa: E501
        self._label = None
        self._vc_info_id = None
        self._vp_info_id = None
        self._vc_object = None
        self._vp_object = None
        self.discriminator = None
        if label is not None:
            self.label = label
        if vc_info_id is not None:
            self.vc_info_id = vc_info_id
        if vp_info_id is not None:
            self.vp_info_id = vp_info_id
        if vc_object is not None:
            self.vc_object = vc_object
        if vp_object is not None:
            self.vp_object = vp_object

    @property
    def label(self):
        """Gets the label of this VerificationDto.  # noqa: E501

        (必須) 検証結果の識別や整理などの管理するにあったてメタデータとして任意で設定可能な単語のフレーズ。(例: verify-for-check)  # noqa: E501

        :return: The label of this VerificationDto.  # noqa: E501
        :rtype: str
        """
        return self._label

    @label.setter
    def label(self, label):
        """Sets the label of this VerificationDto.

        (必須) 検証結果の識別や整理などの管理するにあったてメタデータとして任意で設定可能な単語のフレーズ。(例: verify-for-check)  # noqa: E501

        :param label: The label of this VerificationDto.  # noqa: E501
        :type: str
        """

        self._label = label

    @property
    def vc_info_id(self):
        """Gets the vc_info_id of this VerificationDto.  # noqa: E501

        (任意) 検証を実行するVC情報の識別子。VC情報の識別子を指定して検証を実行する場合は必須。  # noqa: E501

        :return: The vc_info_id of this VerificationDto.  # noqa: E501
        :rtype: str
        """
        return self._vc_info_id

    @vc_info_id.setter
    def vc_info_id(self, vc_info_id):
        """Sets the vc_info_id of this VerificationDto.

        (任意) 検証を実行するVC情報の識別子。VC情報の識別子を指定して検証を実行する場合は必須。  # noqa: E501

        :param vc_info_id: The vc_info_id of this VerificationDto.  # noqa: E501
        :type: str
        """

        self._vc_info_id = vc_info_id

    @property
    def vp_info_id(self):
        """Gets the vp_info_id of this VerificationDto.  # noqa: E501

        (任意) 検証を実行するVP情報の識別子。VP情報の識別子を指定して検証を実行する場合は必須。  # noqa: E501

        :return: The vp_info_id of this VerificationDto.  # noqa: E501
        :rtype: str
        """
        return self._vp_info_id

    @vp_info_id.setter
    def vp_info_id(self, vp_info_id):
        """Sets the vp_info_id of this VerificationDto.

        (任意) 検証を実行するVP情報の識別子。VP情報の識別子を指定して検証を実行する場合は必須。  # noqa: E501

        :param vp_info_id: The vp_info_id of this VerificationDto.  # noqa: E501
        :type: str
        """

        self._vp_info_id = vp_info_id

    @property
    def vc_object(self):
        """Gets the vc_object of this VerificationDto.  # noqa: E501

        (任意) 検証を実行するVCのJSONテキストデータ。VCのJSONテキストデータを入力して検証を実行する場合は必須。  # noqa: E501

        :return: The vc_object of this VerificationDto.  # noqa: E501
        :rtype: object
        """
        return self._vc_object

    @vc_object.setter
    def vc_object(self, vc_object):
        """Sets the vc_object of this VerificationDto.

        (任意) 検証を実行するVCのJSONテキストデータ。VCのJSONテキストデータを入力して検証を実行する場合は必須。  # noqa: E501

        :param vc_object: The vc_object of this VerificationDto.  # noqa: E501
        :type: object
        """

        self._vc_object = vc_object

    @property
    def vp_object(self):
        """Gets the vp_object of this VerificationDto.  # noqa: E501

        (任意) 検証を実行するVPのJSONテキストデータ。VPのJSONテキストデータを入力して検証を実行する場合は必須。  # noqa: E501

        :return: The vp_object of this VerificationDto.  # noqa: E501
        :rtype: object
        """
        return self._vp_object

    @vp_object.setter
    def vp_object(self, vp_object):
        """Sets the vp_object of this VerificationDto.

        (任意) 検証を実行するVPのJSONテキストデータ。VPのJSONテキストデータを入力して検証を実行する場合は必須。  # noqa: E501

        :param vp_object: The vp_object of this VerificationDto.  # noqa: E501
        :type: object
        """

        self._vp_object = vp_object

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
        if issubclass(VerificationDto, dict):
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
        if not isinstance(other, VerificationDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
