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


class ResponseCustomerListResult(object):
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
        'customers_count': 'int',
        'customer': 'list[Customer]',
        'additional_fields': 'object',
        'custom_fields': 'object'
    }

    attribute_map = {
        'customers_count': 'customers_count',
        'customer': 'customer',
        'additional_fields': 'additional_fields',
        'custom_fields': 'custom_fields'
    }

    def __init__(self, customers_count=None, customer=None, additional_fields=None, custom_fields=None):  # noqa: E501
        """ResponseCustomerListResult - a model defined in Swagger"""  # noqa: E501

        self._customers_count = None
        self._customer = None
        self._additional_fields = None
        self._custom_fields = None
        self.discriminator = None

        if customers_count is not None:
            self.customers_count = customers_count
        if customer is not None:
            self.customer = customer
        if additional_fields is not None:
            self.additional_fields = additional_fields
        if custom_fields is not None:
            self.custom_fields = custom_fields

    @property
    def customers_count(self):
        """Gets the customers_count of this ResponseCustomerListResult.  # noqa: E501


        :return: The customers_count of this ResponseCustomerListResult.  # noqa: E501
        :rtype: int
        """
        return self._customers_count

    @customers_count.setter
    def customers_count(self, customers_count):
        """Sets the customers_count of this ResponseCustomerListResult.


        :param customers_count: The customers_count of this ResponseCustomerListResult.  # noqa: E501
        :type: int
        """

        self._customers_count = customers_count

    @property
    def customer(self):
        """Gets the customer of this ResponseCustomerListResult.  # noqa: E501


        :return: The customer of this ResponseCustomerListResult.  # noqa: E501
        :rtype: list[Customer]
        """
        return self._customer

    @customer.setter
    def customer(self, customer):
        """Sets the customer of this ResponseCustomerListResult.


        :param customer: The customer of this ResponseCustomerListResult.  # noqa: E501
        :type: list[Customer]
        """

        self._customer = customer

    @property
    def additional_fields(self):
        """Gets the additional_fields of this ResponseCustomerListResult.  # noqa: E501


        :return: The additional_fields of this ResponseCustomerListResult.  # noqa: E501
        :rtype: object
        """
        return self._additional_fields

    @additional_fields.setter
    def additional_fields(self, additional_fields):
        """Sets the additional_fields of this ResponseCustomerListResult.


        :param additional_fields: The additional_fields of this ResponseCustomerListResult.  # noqa: E501
        :type: object
        """

        self._additional_fields = additional_fields

    @property
    def custom_fields(self):
        """Gets the custom_fields of this ResponseCustomerListResult.  # noqa: E501


        :return: The custom_fields of this ResponseCustomerListResult.  # noqa: E501
        :rtype: object
        """
        return self._custom_fields

    @custom_fields.setter
    def custom_fields(self, custom_fields):
        """Sets the custom_fields of this ResponseCustomerListResult.


        :param custom_fields: The custom_fields of this ResponseCustomerListResult.  # noqa: E501
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
        if issubclass(ResponseCustomerListResult, dict):
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
        if not isinstance(other, ResponseCustomerListResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
