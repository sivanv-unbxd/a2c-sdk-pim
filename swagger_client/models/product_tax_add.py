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


class ProductTaxAdd(object):
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
        'product_id': 'str',
        'name': 'str',
        'tax_rates': 'list[ProductTaxAddTaxRates]'
    }

    attribute_map = {
        'product_id': 'product_id',
        'name': 'name',
        'tax_rates': 'tax_rates'
    }

    def __init__(self, product_id=None, name=None, tax_rates=None):  # noqa: E501
        """ProductTaxAdd - a model defined in Swagger"""  # noqa: E501

        self._product_id = None
        self._name = None
        self._tax_rates = None
        self.discriminator = None

        if product_id is not None:
            self.product_id = product_id
        self.name = name
        self.tax_rates = tax_rates

    @property
    def product_id(self):
        """Gets the product_id of this ProductTaxAdd.  # noqa: E501

        Defines products specified by product id  # noqa: E501

        :return: The product_id of this ProductTaxAdd.  # noqa: E501
        :rtype: str
        """
        return self._product_id

    @product_id.setter
    def product_id(self, product_id):
        """Sets the product_id of this ProductTaxAdd.

        Defines products specified by product id  # noqa: E501

        :param product_id: The product_id of this ProductTaxAdd.  # noqa: E501
        :type: str
        """

        self._product_id = product_id

    @property
    def name(self):
        """Gets the name of this ProductTaxAdd.  # noqa: E501

        Defines tax class name where tax has to be added  # noqa: E501

        :return: The name of this ProductTaxAdd.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ProductTaxAdd.

        Defines tax class name where tax has to be added  # noqa: E501

        :param name: The name of this ProductTaxAdd.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def tax_rates(self):
        """Gets the tax_rates of this ProductTaxAdd.  # noqa: E501

        Defines tax rates of specified tax classes  # noqa: E501

        :return: The tax_rates of this ProductTaxAdd.  # noqa: E501
        :rtype: list[ProductTaxAddTaxRates]
        """
        return self._tax_rates

    @tax_rates.setter
    def tax_rates(self, tax_rates):
        """Sets the tax_rates of this ProductTaxAdd.

        Defines tax rates of specified tax classes  # noqa: E501

        :param tax_rates: The tax_rates of this ProductTaxAdd.  # noqa: E501
        :type: list[ProductTaxAddTaxRates]
        """
        if tax_rates is None:
            raise ValueError("Invalid value for `tax_rates`, must not be `None`")  # noqa: E501

        self._tax_rates = tax_rates

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
        if issubclass(ProductTaxAdd, dict):
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
        if not isinstance(other, ProductTaxAdd):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other