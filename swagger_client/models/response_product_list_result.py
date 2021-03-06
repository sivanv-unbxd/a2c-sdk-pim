# coding: utf-8

"""
    Swagger API2Cart

    API2Cart  # noqa: E501

    OpenAPI spec version: 1.1
    Contact: contact@api2cart.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class ResponseProductListResult(object):
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
        'products_count': 'int',
        'product': 'list[Product]',
        'additional_fields': 'object',
        'custom_fields': 'object'
    }

    attribute_map = {
        'products_count': 'products_count',
        'product': 'product',
        'additional_fields': 'additional_fields',
        'custom_fields': 'custom_fields'
    }

    def __init__(self, products_count=None, product=None, additional_fields=None, custom_fields=None):  # noqa: E501
        """ResponseProductListResult - a model defined in Swagger"""  # noqa: E501

        self._products_count = None
        self._product = None
        self._additional_fields = None
        self._custom_fields = None
        self.discriminator = None

        if products_count is not None:
            self.products_count = products_count
        if product is not None:
            self.product = product
        if additional_fields is not None:
            self.additional_fields = additional_fields
        if custom_fields is not None:
            self.custom_fields = custom_fields

    @property
    def products_count(self):
        """Gets the products_count of this ResponseProductListResult.  # noqa: E501


        :return: The products_count of this ResponseProductListResult.  # noqa: E501
        :rtype: int
        """
        return self._products_count

    @products_count.setter
    def products_count(self, products_count):
        """Sets the products_count of this ResponseProductListResult.


        :param products_count: The products_count of this ResponseProductListResult.  # noqa: E501
        :type: int
        """

        self._products_count = products_count

    @property
    def product(self):
        """Gets the product of this ResponseProductListResult.  # noqa: E501


        :return: The product of this ResponseProductListResult.  # noqa: E501
        :rtype: list[Product]
        """
        return self._product

    @product.setter
    def product(self, product):
        """Sets the product of this ResponseProductListResult.


        :param product: The product of this ResponseProductListResult.  # noqa: E501
        :type: list[Product]
        """

        self._product = product

    @property
    def additional_fields(self):
        """Gets the additional_fields of this ResponseProductListResult.  # noqa: E501


        :return: The additional_fields of this ResponseProductListResult.  # noqa: E501
        :rtype: object
        """
        return self._additional_fields

    @additional_fields.setter
    def additional_fields(self, additional_fields):
        """Sets the additional_fields of this ResponseProductListResult.


        :param additional_fields: The additional_fields of this ResponseProductListResult.  # noqa: E501
        :type: object
        """

        self._additional_fields = additional_fields

    @property
    def custom_fields(self):
        """Gets the custom_fields of this ResponseProductListResult.  # noqa: E501


        :return: The custom_fields of this ResponseProductListResult.  # noqa: E501
        :rtype: object
        """
        return self._custom_fields

    @custom_fields.setter
    def custom_fields(self, custom_fields):
        """Sets the custom_fields of this ResponseProductListResult.


        :param custom_fields: The custom_fields of this ResponseProductListResult.  # noqa: E501
        :type: object
        """

        self._custom_fields = custom_fields

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
        if issubclass(ResponseProductListResult, dict):
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
        if not isinstance(other, ResponseProductListResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
