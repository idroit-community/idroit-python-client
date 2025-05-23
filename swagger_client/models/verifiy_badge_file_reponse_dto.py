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

class VerifiyBadgeFileReponseDto(object):
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
        'result': 'bool',
        'filename': 'bool'
    }

    attribute_map = {
        'result': 'result',
        'filename': 'filename'
    }

    def __init__(self, result=False, filename=False):  # noqa: E501
        """VerifiyBadgeFileReponseDto - a model defined in Swagger"""  # noqa: E501
        self._result = None
        self._filename = None
        self.discriminator = None
        self.result = result
        self.filename = filename

    @property
    def result(self):
        """Gets the result of this VerifiyBadgeFileReponseDto.  # noqa: E501

        (任意)   # noqa: E501

        :return: The result of this VerifiyBadgeFileReponseDto.  # noqa: E501
        :rtype: bool
        """
        return self._result

    @result.setter
    def result(self, result):
        """Sets the result of this VerifiyBadgeFileReponseDto.

        (任意)   # noqa: E501

        :param result: The result of this VerifiyBadgeFileReponseDto.  # noqa: E501
        :type: bool
        """
        if result is None:
            raise ValueError("Invalid value for `result`, must not be `None`")  # noqa: E501

        self._result = result

    @property
    def filename(self):
        """Gets the filename of this VerifiyBadgeFileReponseDto.  # noqa: E501

        (任意)   # noqa: E501

        :return: The filename of this VerifiyBadgeFileReponseDto.  # noqa: E501
        :rtype: bool
        """
        return self._filename

    @filename.setter
    def filename(self, filename):
        """Sets the filename of this VerifiyBadgeFileReponseDto.

        (任意)   # noqa: E501

        :param filename: The filename of this VerifiyBadgeFileReponseDto.  # noqa: E501
        :type: bool
        """
        if filename is None:
            raise ValueError("Invalid value for `filename`, must not be `None`")  # noqa: E501

        self._filename = filename

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
        if issubclass(VerifiyBadgeFileReponseDto, dict):
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
        if not isinstance(other, VerifiyBadgeFileReponseDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
