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

class VcSchemasResponseDto(object):
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
        'items': 'list[VcSchema]',
        'meta': 'MetaDto',
        'links': 'LinkDto'
    }

    attribute_map = {
        'items': 'items',
        'meta': 'meta',
        'links': 'links'
    }

    def __init__(self, items=None, meta=None, links=None):  # noqa: E501
        """VcSchemasResponseDto - a model defined in Swagger"""  # noqa: E501
        self._items = None
        self._meta = None
        self._links = None
        self.discriminator = None
        self.items = items
        self.meta = meta
        self.links = links

    @property
    def items(self):
        """Gets the items of this VcSchemasResponseDto.  # noqa: E501

        Array of VC schema items  # noqa: E501

        :return: The items of this VcSchemasResponseDto.  # noqa: E501
        :rtype: list[VcSchema]
        """
        return self._items

    @items.setter
    def items(self, items):
        """Sets the items of this VcSchemasResponseDto.

        Array of VC schema items  # noqa: E501

        :param items: The items of this VcSchemasResponseDto.  # noqa: E501
        :type: list[VcSchema]
        """
        if items is None:
            raise ValueError("Invalid value for `items`, must not be `None`")  # noqa: E501

        self._items = items

    @property
    def meta(self):
        """Gets the meta of this VcSchemasResponseDto.  # noqa: E501


        :return: The meta of this VcSchemasResponseDto.  # noqa: E501
        :rtype: MetaDto
        """
        return self._meta

    @meta.setter
    def meta(self, meta):
        """Sets the meta of this VcSchemasResponseDto.


        :param meta: The meta of this VcSchemasResponseDto.  # noqa: E501
        :type: MetaDto
        """
        if meta is None:
            raise ValueError("Invalid value for `meta`, must not be `None`")  # noqa: E501

        self._meta = meta

    @property
    def links(self):
        """Gets the links of this VcSchemasResponseDto.  # noqa: E501


        :return: The links of this VcSchemasResponseDto.  # noqa: E501
        :rtype: LinkDto
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this VcSchemasResponseDto.


        :param links: The links of this VcSchemasResponseDto.  # noqa: E501
        :type: LinkDto
        """
        if links is None:
            raise ValueError("Invalid value for `links`, must not be `None`")  # noqa: E501

        self._links = links

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
        if issubclass(VcSchemasResponseDto, dict):
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
        if not isinstance(other, VcSchemasResponseDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
