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


class ProductVariantAddAttributes(object):
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
        'attribute_name': 'str',
        'attribute_value': 'str',
        'attribute_price': 'float'
    }

    attribute_map = {
        'attribute_name': 'attribute_name',
        'attribute_value': 'attribute_value',
        'attribute_price': 'attribute_price'
    }

    def __init__(self, attribute_name=None, attribute_value=None, attribute_price=None):  # noqa: E501
        """ProductVariantAddAttributes - a model defined in Swagger"""  # noqa: E501

        self._attribute_name = None
        self._attribute_value = None
        self._attribute_price = None
        self.discriminator = None

        if attribute_name is not None:
            self.attribute_name = attribute_name
        if attribute_value is not None:
            self.attribute_value = attribute_value
        if attribute_price is not None:
            self.attribute_price = attribute_price

    @property
    def attribute_name(self):
        """Gets the attribute_name of this ProductVariantAddAttributes.  # noqa: E501


        :return: The attribute_name of this ProductVariantAddAttributes.  # noqa: E501
        :rtype: str
        """
        return self._attribute_name

    @attribute_name.setter
    def attribute_name(self, attribute_name):
        """Sets the attribute_name of this ProductVariantAddAttributes.


        :param attribute_name: The attribute_name of this ProductVariantAddAttributes.  # noqa: E501
        :type: str
        """

        self._attribute_name = attribute_name

    @property
    def attribute_value(self):
        """Gets the attribute_value of this ProductVariantAddAttributes.  # noqa: E501


        :return: The attribute_value of this ProductVariantAddAttributes.  # noqa: E501
        :rtype: str
        """
        return self._attribute_value

    @attribute_value.setter
    def attribute_value(self, attribute_value):
        """Sets the attribute_value of this ProductVariantAddAttributes.


        :param attribute_value: The attribute_value of this ProductVariantAddAttributes.  # noqa: E501
        :type: str
        """

        self._attribute_value = attribute_value

    @property
    def attribute_price(self):
        """Gets the attribute_price of this ProductVariantAddAttributes.  # noqa: E501


        :return: The attribute_price of this ProductVariantAddAttributes.  # noqa: E501
        :rtype: float
        """
        return self._attribute_price

    @attribute_price.setter
    def attribute_price(self, attribute_price):
        """Sets the attribute_price of this ProductVariantAddAttributes.


        :param attribute_price: The attribute_price of this ProductVariantAddAttributes.  # noqa: E501
        :type: float
        """

        self._attribute_price = attribute_price

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
        if issubclass(ProductVariantAddAttributes, dict):
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
        if not isinstance(other, ProductVariantAddAttributes):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
